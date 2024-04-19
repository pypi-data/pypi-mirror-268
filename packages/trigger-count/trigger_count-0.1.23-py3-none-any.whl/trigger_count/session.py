"""
Class to organize all triggers in one go.
"""
from pathlib import Path

import numpy as np
import pandas as pd
import polars as pl
from tqdm import tqdm

from trigger_count.files import get_n_frames_from_tif, find_csv_files, find_mp4_files, get_n_frames_from_mp4

RENAME_COLUMNS = {
    "i_flip": "i_stim_flip",
    "elapsed": "stim_flip_interval",
}
DEFAULT_COLUMNS = ["i_epoch", "epoch_name", "epoch_time", "i_trial"]


class RecordingSession:
    """Class to process triggers of one recording session."""
    def __init__(self, source_folder: Path, stim_columns: list) -> None:
        # params
        self.source_folder = source_folder
        self.stim_columns = stim_columns

        # state
        self.daq_df: pl.DataFrame | None = None  # use polars to speed this up
        self.flip_info: pd.DataFrame | None = None
        self.vitals_df: pd.DataFrame | None = None

        self.n_daq_samples = None
        self.n_stim_flips = None
        self.n_twophoton_frames = None
        self.n_widefield_frames = None
        self.n_vitals_samples = None
        self.n_eyetracking_frames = None

        self.frame_info: pd.DataFrame | None = None

        self.main_trigger = None
        self.start_offsets = {}
        self.end_offsets = {}

        self.all_columns = None

        # go!
        self.check_dtypes()

    def check_dtypes(self) -> None:
        """
        Check which dtypes are available:
        - stim
        - 2p
        - widefield
        - eyetracking (LE, RE)
        - vitals
        """
        self.check_twophoton()
        self.check_widefield()
        self.check_daq()
        self.check_stim()
        self.check_vitals()
        self.check_eyetracking()

    def check_twophoton(self) -> None:
        """Check what 2p related files exist."""
        suite2p_folder = self.source_folder / "suite2p"
        if suite2p_folder.is_dir():
            # print(f"2p data available: {suite2p_folder}")
            traces_file = suite2p_folder / "F.npy"
            if traces_file.is_file():
                traces = np.load(traces_file)
                self.n_twophoton_frames = traces.shape[1]
                print(f"Twophoton frames: {self.n_twophoton_frames:,}")

    def check_widefield(self) -> None:
        """Check what widefield-related files exist."""
        widefield_file = self.source_folder / "dataset" / "recording.tif"
        if widefield_file.is_file():
            print(f"Widefield data available: {widefield_file}")
            self.n_widefield_frames = get_n_frames_from_tif(widefield_file)
            print(f"{self.n_widefield_frames:,} frames in widefield TIFF")

    def check_stim(self) -> None:
        stim_file = self.source_folder / "stim" / "flip_info.csv"
        if stim_file.is_file():
            # print(f"Stim data available: {stim_file}")
            self.flip_info = pd.read_csv(stim_file)
            self.n_stim_flips = self.flip_info.shape[0]
            print(f"Stim flips: {self.n_stim_flips:,}")

    def check_daq(self) -> None:
        """Check what stim-related files exist."""
        stim_folder = self.source_folder / "stim"
        if stim_folder.is_dir():
            # print(f"Stim data available: {stim_folder}")
            daq_file = stim_folder / "daq.csv"
            if daq_file.is_file():
                self.daq_df = pl.read_csv(daq_file)  # pd.read_csv(daq_file)
                self.n_daq_samples = self.daq_df.shape[0]
                print(f"DAQ samples: {self.n_daq_samples:,}")

    def check_vitals(self) -> None:
        """Check what vitals-related files exist."""
        vitals_folder = self.source_folder / "vitals"
        if vitals_folder.is_dir():
            # print(f"Vitals data available: {vitals_folder}")
            csv_files = find_csv_files(vitals_folder)
            if len(csv_files) == 1:
                self.vitals_df = pd.read_csv(csv_files[0])
                self.n_vitals_samples = self.vitals_df.shape[0]
                print(f"{self.n_vitals_samples:,} vitals samples")
            else:
                raise ValueError(f"{len(csv_files)} CSV files in vitals folder.")

    def check_eyetracking(self) -> None:
        """Check what eye tracking related files exist."""
        eyetracking_folder = self.source_folder / "eyetracking"
        if eyetracking_folder.is_dir():
            # print(f"Eye tracking data available: {eyetracking_folder}")
            left_eye_folder = eyetracking_folder / "left_eye"
            right_eye_folder = eyetracking_folder / "right_eye"
            self.n_eyetracking_frames = {}
            for name, folder in {"left": left_eye_folder, "right": right_eye_folder}.items():
                mp4_file = find_mp4_files(folder)
                if len(mp4_file) == 1:
                    mp4_file = mp4_file[0]
                    n_frames = get_n_frames_from_mp4(mp4_file)
                    self.n_eyetracking_frames[name] = n_frames
                    print(f"{name.capitalize()} eye tracking frames: {n_frames:,}")
                else:
                    raise ValueError(f"{len(mp4_file)} mp4 files in {folder}")

    def make_frame_info(self, overwrite: bool = False) -> pd.DataFrame:
        """
        Main method to call.
        Creates a table with info for each 2p or WF frame.
        """
        frame_info_file = self.source_folder / "dataset" / "frame_info.csv"
        if frame_info_file.is_file() and not overwrite:
            raise FileExistsError(f"Frame info file already exists: {frame_info_file}")
        else:
            if isinstance(self.daq_df, (pd.DataFrame, pl.DataFrame)):
                self.make_frame_info_from_daq()
            else:
                print("No DAQ file - is this an older session?")
                raise NotImplementedError()

        if self.n_stim_flips:
            self.add_stim_info()
        if self.n_eyetracking_frames:
            self.add_eye_tracking_triggers()
        self.apply_offsets()
        self.add_elapsed()
        return self.frame_info

    def make_frame_info_from_daq(self) -> None:
        """Get frame info by subsampling DAQ file."""
        trigger_source = None
        if self.n_twophoton_frames:
            self.main_trigger = "twophoton_scanner"
        elif self.n_widefield_frames:
            self.main_trigger = "widefield_camera"
        subset = self.subsample_daq(self.main_trigger)
        self.quality_check(subset, self.main_trigger)

        prefix = self.main_trigger.split("_")[0]
        frame_info = {}
        frame_info["datetime"] = subset["datetime"]
        frame_info[f"i_{prefix}_frame"] = subset[self.main_trigger] - 1
        frame_info[f"{prefix}_frame_interval"] = subset[f"interval_{self.main_trigger}"]
        frame_info = pd.DataFrame(frame_info)
        self.frame_info = frame_info

    def subsample_daq(self, trigger_source: str) -> pl.DataFrame:
        """Subsample DAQ file to only rows where a new trigger was received."""
        column = f"interval_{trigger_source}"
        if column not in self.daq_df.columns:
            print("DAQ table columns:")
            for col in self.daq_df.columns:
                print(f"\t{col}")
            raise KeyError(f"{column=} not in DAQ table.")

        is_selected = self.daq_df[column].is_not_null()
        subset = self.daq_df.filter(is_selected)
        n_triggers = subset.shape[0]
        print(f"{trigger_source}: {n_triggers:,} triggers")
        subset = subset.to_pandas()
        return subset

    def quality_check(self, triggers: pd.DataFrame, trigger_source) -> None:
        """Check whether a certain trigger source has consistent trigger intervals."""
        print(f"---Quality check: {trigger_source}---")
        self.print_first_last_triggers(triggers, trigger_source)
        self.print_slowest_fastest_triggers(triggers, trigger_source)
        self.check_intermediates(triggers, trigger_source)
        self.zscore_triggers(triggers, trigger_source)

    def add_stim_info(self) -> None:
        self.all_columns = [*DEFAULT_COLUMNS, *self.stim_columns]
        stim_info = []
        n_total = self.frame_info.shape[0]
        for i_row, row in tqdm(self.frame_info.iterrows(), total=n_total):
            trigger = row[f"i_twophoton_frame"] + 1
            is_trigger = self.flip_info["counter"] == trigger
            details = {}
            if np.any(is_trigger):
                for old_col, new_col in RENAME_COLUMNS.items():
                    details[new_col] = self.flip_info.loc[is_trigger, old_col].values[0]
                for col in self.all_columns:
                    details[col] = self.flip_info.loc[is_trigger, col].values[0]
            stim_info.append(details)
        stim_info = pd.DataFrame(stim_info)
        self.frame_info = pd.concat([self.frame_info, stim_info], axis=1).reset_index(drop=True)

    def print_first_last_triggers(self, triggers: pd.DataFrame, trigger_source: str) -> None:
        """Print the first and last trigger intervals."""
        for ascending in [True, False]:
            prefix = "first" if ascending else "last"
            print(f"-{trigger_source}: {prefix.capitalize()} triggers-")
            sorted_df = triggers.sort_values(by="count", ascending=ascending)
            sorted_df = sorted_df.reset_index(drop=True)
            for i_row, row in sorted_df.iterrows():
                if i_row == 5:
                    break
                frame_interval = row[f"interval_{trigger_source}"]
                frame_interval = float(frame_interval)
                print(f"({i_row}) {trigger_source}: {row[trigger_source]} -> {frame_interval * 1000:.1f} ms")

    def print_slowest_fastest_triggers(self, triggers: pd.DataFrame, trigger_source: str) -> None:
        """Print the slowest and fastest trigger intervals."""
        for ascending in [True, False]:
            prefix = "fastest" if ascending else "slowest"
            print(f"-{trigger_source}: {prefix.capitalize()} trigger intervals-")
            sorted_df = triggers.sort_values(by=f"interval_{trigger_source}", ascending=ascending)
            sorted_df = sorted_df.reset_index(drop=True)
            for i_row, row in sorted_df.iterrows():
                if i_row == 5:
                    break
                frame_interval = row[f"interval_{trigger_source}"]
                frame_interval = float(frame_interval)
                print(f"({i_row}) {trigger_source}: {row[trigger_source]} -> {frame_interval * 1000:.1f} ms")

    def zscore_triggers(self, triggers, trigger_source: str, threshold: float = 10) -> None:
        """Z-score trigger intervals to check for irregularieties."""
        intervals = triggers[f"interval_{trigger_source}"].values.astype(float)
        zscores = self.zscore_with_median(intervals)
        is_deviant = np.abs(zscores) > threshold
        n_deviant = np.sum(is_deviant)
        print(f"-{trigger_source}: {n_deviant} outliers-")
        for i_row, row in triggers.loc[is_deviant].iterrows():
            frame_interval = row[f"interval_{trigger_source}"]
            frame_interval = float(frame_interval)
            z = zscores[i_row]
            print(f"({i_row}) {trigger_source}: {row[trigger_source]} -> {frame_interval * 1000:.1f} ms ({z=:.1f})")
        start_offset, end_offset = self.determine_offsets(zscores)
        self.start_offsets[trigger_source] = start_offset

    @staticmethod
    def zscore_with_median(some_values: np.ndarray) -> np.ndarray:
        """Z-score a series of values but take median and median absolute deviation instead of mean and standard deviation."""
        median_val = np.median(some_values)
        # print(f"Median: {median_val * 1000:.1f} ms")
        deviations = some_values - median_val
        absolute_deviations = np.abs(deviations)
        median_deviation = np.median(absolute_deviations)
        # print(f"Median deviation: {median_deviation * 1000:.1f} ms")
        z_values = (some_values - median_val) / median_deviation
        return z_values

    def add_eye_tracking_triggers(self) -> None:
        """Add eye tracking info to frame info."""
        for eye in ["left", "right"]:
            trigger_source = f"{eye}_eye_camera"
            subset = self.subsample_daq(trigger_source)
            self.quality_check(subset, trigger_source)

            subset = self.subsample_daq(self.main_trigger)
            self.frame_info[f"i_{eye}_eye_frame"] = subset[trigger_source] - 1

    def determine_offsets(self, zscores: np.ndarray, threshold: float = 10) -> tuple:
        """
        Determine how many extra triggers could have occured at the start or end of a recording.
        Somtimes, components can send extra triggers when turned on or off.
        These are detectable by having noticably longer or shorter intervals to regular triggers.
        """
        start_offset = 0
        for i, z in enumerate(zscores):
            if i == 5:
                break
            if z > threshold:
                start_offset += 1

        end_offset = 0
        for i, z in enumerate(zscores[::-1]) :
            if i == 5:
                break
            if z > threshold:
                end_offset += 1
        return start_offset, end_offset

    def check_intermediates(self, triggers: pd.DataFrame, trigger_source: str) -> None:
        """Check whether intermediate triggers were missed by the computer (but not the labjack)."""
        numbers = triggers[trigger_source].values
        min_val = np.min(numbers)
        max_val = np.max(numbers)
        all_possible = np.arange(min_val, max_val)
        is_there = np.isin(all_possible, numbers)
        is_missing = np.logical_not(is_there)
        n_missing = np.sum(is_missing)
        print(f"-{trigger_source}: {n_missing} missed intermediates-")
        if np.any(is_missing):
            missing_vals = all_possible[is_missing]
            for missed in missing_vals:
                is_before = triggers[trigger_source] == (missed - 1)
                is_after = triggers[trigger_source] == (missed + 1)
                if np.sum(is_before):
                    previous_interval = triggers.loc[is_before, f"interval_{trigger_source}"].values[0]
                    previous_interval = float(previous_interval)
                    previous_str = f"{previous_interval * 1000:.1f} ms"
                else:
                    previous_str = "none"
                if np.sum(is_after):
                    following_interval = triggers.loc[is_after, f"interval_{trigger_source}"].values[0]
                    following_interval = float(following_interval)
                    following_str = f"{following_interval * 1000:.1f} ms"
                else:
                    following_str = "none"
                print(f"{trigger_source}: {missed} (previous: {previous_str}, following: {following_str})")
        else:
            print(f"{trigger_source}: No intermediate triggers missing.")

    def apply_offsets(self) -> None:
        print("---Applying offsets---")
        for trigger_source, start_offset in self.start_offsets.items():
            if trigger_source == self.main_trigger:
                if trigger_source == "twophoton_scanner":
                    col = "i_twophoton_frame"
                elif trigger_source == "widefield_camera":
                    col = "i_widefield_frame"
                else:
                    raise ValueError(f"{trigger_source}")
                self.frame_info[col] = self.frame_info[col] - start_offset
                is_negative = self.frame_info[col] < 0
                if np.any(is_negative):
                    n_removed = np.sum(is_negative)
                    print(f"Removing {n_removed} rows from frame info")
                    is_positive = self.frame_info[col] >= 0
                    self.frame_info = self.frame_info.loc[is_positive].reset_index(drop=True)
            else:
                if trigger_source == "left_eye_camera":
                    col = "i_left_eye_frame"
                elif trigger_source == "right_eye_camera":
                    col = "i_right_eye_frame"
                else:
                    raise ValueError(f"{trigger_source}")
                self.frame_info[col] = self.frame_info[col] - start_offset

    def add_elapsed(self) -> None:
        timestamps = pd.to_datetime(self.frame_info["datetime"], format="%Y-%m-%d %H:%M:%S.%f")
        relative_time = timestamps - timestamps.min()
        relative_time = [x.total_seconds() for x in relative_time]
        self.frame_info["elapsed"] = relative_time
