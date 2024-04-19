#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###############################################################################
# Copyright © 2023-2024 Auromix.                                              #
#                                                                             #
# Licensed under the Apache License, Version 2.0 (the "License");             #
# You may not use this file except in compliance with the License.            #
# You may obtain a copy of the License at                                     #
#                                                                             #
#     http://www.apache.org/licenses/LICENSE-2.0                              #
#                                                                             #
# Unless required by applicable law or agreed to in writing, software         #
# distributed under the License is distributed on an "AS IS" BASIS,           #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.    #
# See the License for the specific language governing permissions and         #
# limitations under the License.                                              #
#                                                                             #
# Description: Realsense camera class for auromix                             #
# Author: Herman Ye                                                           #
###############################################################################


import pyrealsense2 as rs
import numpy as np
from typing import Optional


class RealsenseCamera:
    """Class representing a RealSense camera."""

    def __init__(self):
        """Initialize the RealSense camera."""
        self.pipeline = rs.pipeline()
        self.config = rs.config()
        self.config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
        self.config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
        # Align depth frame to color frame
        self.align = rs.align(rs.stream.color)
        self.profile = self.pipeline.start(self.config)
        self.depth_scale = self.get_depth_scale()

    def __del__(self):
        """Stop the RealSense pipeline."""
        self.pipeline.stop()

    def get_color_data(self) -> np.ndarray:
        """Retrieve color data from the RealSense camera.

        Returns:
            np.ndarray: Color data as a NumPy array.
        """
        frames = self.pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()
        color_data = np.asanyarray(color_frame.get_data())
        return color_data

    def get_depth_data(
        self, clip: Optional[float] = None, scale: Optional[float] = None
    ) -> np.ndarray:
        """Retrieve depth data from the RealSense camera.

        Args:
            clip (Optional[float]): Maximum depth value to clip to in meters.
            scale (Optional[float]): Value to scale depth data by.

        Returns:
            np.ndarray: Depth data as a NumPy array.
        """
        frames = self.pipeline.wait_for_frames()
        aligned_frames = self.align.process(frames)
        aligned_depth_frame = aligned_frames.get_depth_frame()
        depth_data = np.asanyarray(aligned_depth_frame.get_data())

        if clip:
            clip = clip / self.depth_scale
            depth_data = np.clip(depth_data, 0, clip)
            depth_data[depth_data == clip] = 0

        if scale:
            depth_data = depth_data * scale

        return depth_data

    def get_camera_intrinsics(self) -> np.ndarray:
        """Retrieve camera intrinsics from the RealSense camera.

        Returns:
            np.ndarray: Camera intrinsic matrix.
        """
        profile = self.profile.get_stream(rs.stream.depth)
        intrinsics = profile.as_video_stream_profile().get_intrinsics()

        intrinsic_matrix = np.array(
            [
                [intrinsics.fx, 0, intrinsics.ppx],
                [0, intrinsics.fy, intrinsics.ppy],
                [0, 0, 1],
            ]
        )
        return intrinsic_matrix

    def get_depth_scale(self) -> float:
        """Retrieve depth scale from the RealSense camera.

        Returns:
            float: Depth scale factor.
        """
        depth_sensor = self.profile.get_device().first_depth_sensor()
        return depth_sensor.get_depth_scale()
