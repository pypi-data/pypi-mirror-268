__author__ = "Simon Nilsson"

from copy import deepcopy
from typing import Dict, Optional

import numpy as np
import pandas as pd
from numba import jit, prange

from simba.mixins.config_reader import ConfigReader
from simba.mixins.feature_extraction_mixin import FeatureExtractionMixin
from simba.roi_tools.ROI_analyzer import ROIAnalyzer
from simba.utils.read_write import get_fn_ext


class DirectingROIAnalyzer(ConfigReader, FeatureExtractionMixin):
    """
    Compute aggregate statistics for animals directing towards ROIs.

    :param str config_path: Path to SimBA project config file in Configparser format
    :param Optional[dict] settings: If dict, the animal body-parts and the probability threshold. If None, then the data is read from the
        project_config.ini. Defalt: None.

    .. note::
       `ROI tutorials <https://github.com/sgoldenlab/simba/blob/master/docs/ROI_tutorial_new.md>`__.

    Examples
    ----------
    >>> settings = {'body_parts': {'Simon': 'Ear_left_1', 'JJ': 'Ear_left_2'}, 'threshold': 0.4}
    >>> _ = DirectingROIAnalyzer(config_path='MyProjectConfig', settings=settings).run()
    """

    def __init__(
        self,
        config_path: str,
        data_path: Optional[str] = None,
        settings: Optional[dict] = None,
    ):
        ConfigReader.__init__(self, config_path=config_path)
        FeatureExtractionMixin.__init__(self, config_path=config_path)
        self.roi_analyzer = ROIAnalyzer(
            ini_path=config_path,
            data_path="outlier_corrected_movement_location",
            settings=settings,
        )
        self.files_found = deepcopy(self.roi_analyzer.files_found)
        self.direct_bp_dict = self.check_directionality_cords()

    def __format_direction_data(self):
        x_min = np.minimum(self.direction_data[:, 1], self.nose_arr[:, 0])
        y_min = np.minimum(self.direction_data[:, 2], self.nose_arr[:, 1])
        delta_x = abs((self.direction_data[:, 1] - self.nose_arr[:, 0]) / 2)
        delta_y = abs((self.direction_data[:, 2] - self.nose_arr[:, 1]) / 2)
        x_middle, y_middle = np.add(x_min, delta_x), np.add(y_min, delta_y)
        direction_data = np.concatenate(
            (y_middle.reshape(-1, 1), self.direction_data), axis=1
        )
        direction_data = np.concatenate(
            (x_middle.reshape(-1, 1), direction_data), axis=1
        )
        direction_data = np.delete(direction_data, [2, 3, 4], 1)
        bp_data = pd.DataFrame(
            direction_data, columns=["Eye_x", "Eye_y", "Directing_BOOL"]
        )
        bp_data["ROI_x"] = self.center_cord[0]
        bp_data["ROI_y"] = self.center_cord[1]
        bp_data = bp_data[["Eye_x", "Eye_y", "ROI_x", "ROI_y", "Directing_BOOL"]]
        bp_data.insert(loc=0, column="ROI", value=self.shape_info["Name"])
        bp_data.insert(loc=0, column="Animal", value=self.animal_name)
        bp_data.insert(loc=0, column="Video", value=self.video_name)
        bp_data = bp_data.reset_index().rename(columns={"index": "Frame"})
        bp_data = bp_data[bp_data["Directing_BOOL"] == 1].reset_index(drop=True)
        return bp_data

    @staticmethod
    @jit(nopython=True, fastmath=True)
    def ccw(roi_lines: np.array, eye_lines: np.array, shape_type: str):
        def calc(A, B, C):
            return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])

        results = np.full((eye_lines.shape[0], 4), -1)
        for i in prange(eye_lines.shape[0]):
            eye, roi = eye_lines[i][0:2], eye_lines[i][2:4]
            min_distance = np.inf

            if shape_type == "Circle":
                reversed_roi_lines = roi_lines[::-1]
                for j in prange(roi_lines.shape[0]):
                    dist_1 = np.sqrt(
                        (eye[0] - roi_lines[j][0]) ** 2
                        + (eye[1] - roi_lines[j][1]) ** 2
                    )
                    dist_2 = np.sqrt(
                        (eye[0] - roi_lines[j][2]) ** 2
                        + (eye[1] - roi_lines[j][3]) ** 2
                    )
                    if (dist_1 < min_distance) or (dist_2 < min_distance):
                        min_distance = min(dist_1, dist_2)
                        results[i] = reversed_roi_lines[j]

            else:
                for j in prange(roi_lines.shape[0]):
                    line_a, line_b = roi_lines[j][0:2], roi_lines[j][2:4]
                    center_x, center_y = (
                        line_a[0] + line_b[0] // 2,
                        line_a[1] + line_b[1] // 2,
                    )
                    if calc(eye, line_a, line_b) != calc(roi, line_a, line_b) or calc(
                        eye, roi, line_a
                    ) != calc(eye, roi, line_b):
                        distance = np.sqrt(
                            (eye[0] - center_x) ** 2 + (eye[1] - center_y) ** 2
                        )
                        if distance < min_distance:
                            results[i] = roi_lines[j]
                            min_distance = distance

        return results

    def __find_roi_intersections(self):
        eye_lines = self.bp_data[["Eye_x", "Eye_y", "ROI_x", "ROI_y"]].values.astype(
            int
        )
        roi_lines = None
        if self.shape_info["Shape_type"] == "Rectangle":
            top_left_x, top_left_y = (
                self.shape_info["topLeftX"],
                self.shape_info["topLeftY"],
            )
            bottom_right_x, bottom_right_y = (
                self.shape_info["Bottom_right_X"],
                self.shape_info["Bottom_right_Y"],
            )
            top_right_x, top_right_y = top_left_x + self.shape_info["width"], top_left_y
            bottom_left_x, bottom_left_y = (
                bottom_right_x - self.shape_info["width"],
                bottom_right_y,
            )
            roi_lines = np.array(
                [
                    [top_left_x, top_left_y, bottom_left_x, bottom_left_y],
                    [bottom_left_x, bottom_left_y, bottom_right_x, bottom_right_y],
                    [bottom_right_x, bottom_right_y, top_right_x, top_right_y],
                    [top_right_x, top_right_y, top_left_x, top_left_y],
                ]
            )

        elif self.shape_info["Shape_type"] == "Polygon":
            roi_lines = np.full((self.shape_info["vertices"].shape[0], 4), np.nan)
            roi_lines[-1] = np.hstack(
                (self.shape_info["vertices"][0], self.shape_info["vertices"][-1])
            )
            for i in range(self.shape_info["vertices"].shape[0] - 1):
                roi_lines[i] = np.hstack(
                    (self.shape_info["vertices"][i], self.shape_info["vertices"][i + 1])
                )

        elif self.shape_info["Shape_type"] == "Circle":
            center = self.shape_info[["centerX", "centerY"]].values.astype(int)
            roi_lines = np.full((2, 4), np.nan)
            roi_lines[0] = np.array(
                [
                    center[0],
                    center[1] - self.shape_info["radius"],
                    center[0],
                    center[1] + self.shape_info["radius"],
                ]
            )
            roi_lines[1] = np.array(
                [
                    center[0] - self.shape_info["radius"],
                    center[1],
                    center[0] + self.shape_info["radius"],
                    center[1],
                ]
            )

        return self.ccw(
            roi_lines=roi_lines,
            eye_lines=eye_lines,
            shape_type=self.shape_info["Shape_type"],
        )

    def run(self):
        """
        Method to calculate directing-towards ROI data
        """

        self.results_lst = []
        for file_cnt, file_path in enumerate(self.files_found):
            _, self.video_name, _ = get_fn_ext(file_path)
            self.roi_analyzer.files_found = [file_path]
            self.roi_analyzer.run()
            video_data_df = self.roi_analyzer.data_df
            for animal_name in self.roi_analyzer.multi_animal_id_list:
                self.animal_name = animal_name
                animal_bp_names = (
                    self.animal_bp_dict[animal_name]["X_bps"]
                    + self.animal_bp_dict[animal_name]["Y_bps"]
                )
                animal_data_df = video_data_df[animal_bp_names]
                animal_direct_bps = self.direct_bp_dict[animal_name]
                self.ear_left_arr = animal_data_df[
                    [
                        animal_direct_bps["Ear_left"]["X_bps"],
                        animal_direct_bps["Ear_left"]["Y_bps"],
                    ]
                ].to_numpy()
                self.ear_right_arr = animal_data_df[
                    [
                        animal_direct_bps["Ear_right"]["X_bps"],
                        animal_direct_bps["Ear_right"]["Y_bps"],
                    ]
                ].to_numpy()
                self.nose_arr = animal_data_df[
                    [
                        animal_direct_bps["Nose"]["X_bps"],
                        animal_direct_bps["Nose"]["Y_bps"],
                    ]
                ].to_numpy()
                for _, row in self.roi_analyzer.video_recs.iterrows():
                    self.shape_info = row
                    center_cord = (
                        (int(row["topLeftX"] + (row["width"] / 2))),
                        (int(row["topLeftY"] + (row["height"] / 2))),
                    )
                    self.center_cord = np.asarray(center_cord)
                    self.direction_data = self.jitted_line_crosses_to_static_targets(
                        left_ear_array=self.ear_left_arr,
                        right_ear_array=self.ear_right_arr,
                        nose_array=self.nose_arr,
                        target_array=self.center_cord,
                    )
                    self.bp_data = self.__format_direction_data()
                    eye_roi_intersections = pd.DataFrame(
                        self.__find_roi_intersections(),
                        columns=[
                            "ROI_edge_1_x",
                            "ROI_edge_1_y",
                            "ROI_edge_2_x",
                            "ROI_edge_2_y",
                        ],
                    )
                    self.bp_data = pd.concat(
                        [self.bp_data, eye_roi_intersections], axis=1
                    )
                    self.results_lst.append(self.bp_data)
                for _, row in self.roi_analyzer.video_circs.iterrows():
                    self.shape_info = row
                    self.center_cord = np.asarray((row["centerX"], row["centerY"]))
                    self.direction_data = self.jitted_line_crosses_to_static_targets(
                        left_ear_array=self.ear_left_arr,
                        right_ear_array=self.ear_right_arr,
                        nose_array=self.nose_arr,
                        target_array=self.center_cord,
                    )
                    self.bp_data = self.__format_direction_data()
                    eye_roi_intersections = pd.DataFrame(
                        self.__find_roi_intersections(),
                        columns=[
                            "ROI_edge_1_x",
                            "ROI_edge_1_y",
                            "ROI_edge_2_x",
                            "ROI_edge_2_y",
                        ],
                    )
                    self.bp_data = pd.concat(
                        [self.bp_data, eye_roi_intersections], axis=1
                    )
                    self.results_lst.append(self.bp_data)
                for _, row in self.roi_analyzer.video_polys.iterrows():
                    self.shape_info = row
                    self.center_cord = np.asarray((row["Center_X"], row["Center_Y"]))
                    self.direction_data = self.jitted_line_crosses_to_static_targets(
                        left_ear_array=self.ear_left_arr,
                        right_ear_array=self.ear_right_arr,
                        nose_array=self.nose_arr,
                        target_array=self.center_cord,
                    )
                    self.bp_data = self.__format_direction_data()
                    eye_roi_intersections = pd.DataFrame(
                        self.__find_roi_intersections(),
                        columns=[
                            "ROI_edge_1_x",
                            "ROI_edge_1_y",
                            "ROI_edge_2_x",
                            "ROI_edge_2_y",
                        ],
                    )
                    self.bp_data = pd.concat(
                        [self.bp_data, eye_roi_intersections], axis=1
                    )
                    self.results_lst.append(self.bp_data)
        self.results_df = pd.concat(self.results_lst, axis=0)


#
# test = DirectingROIAnalyzer(config_path='/Users/simon/Desktop/envs/simba_dev/tests/test_data/mouse_open_field/project_folder/project_config.ini')
# test.run()
#
