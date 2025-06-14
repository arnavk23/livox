import numpy as np
import time
from camera.base_camera import Camera

# Hypothetical Python binding or ctypes wrapper
from livoxsdk import LivoxDevice, LivoxHub


class LivoxCamera(Camera):
    def __init__(self, name: str, device_serial: str):
        super().__init__(name)
        self._serial = device_serial
        self.device = None
        self._last_cloud = None

    @property
    def serial(self) -> str:
        return self._serial

    def _validate_point_cloud(self, point_cloud: np.ndarray) -> bool:
        non_zeros = point_cloud[~np.all(point_cloud == 0.0, axis=1)]
        z_mean = np.mean(non_zeros[:, 2])
        return z_mean < 2

    def _on_point_cloud_callback(self, data: np.ndarray) -> None:
        # Livox point cloud format is assumed to be Nx3 or Nx6
        points = data[:, :3]
        mask = np.bitwise_and(points[:, 2] < 0.6, 0.05 < points[:, 2])
        filtered_points = points[mask]

        if self._validate_point_cloud(filtered_points):
            self._last_cloud = filtered_points

    def start(self) -> None:
        if self._running:
            return

        # Connect to device (LivoxHub or standalone)
        self.device = LivoxHub().get_device_by_serial(self._serial)
        if self.device is None:
            raise Exception(f"Device with serial {self._serial} not found.")

        self.device.set_callback(self._on_point_cloud_callback)
        self.device.start()
        super().start()

    def stop(self) -> None:
        if not self._running:
            return

        if self.device:
            self.device.stop()
        super().stop()

    def get(self, timeout_ms: int = 200) -> np.ndarray:
        if not self._running:
            raise Exception("Livox pipeline is not running.")

        # Wait for new frame to be set by callback
        t_start = time.time()
        while self._last_cloud is None:
            if (time.time() - t_start) * 1000 > timeout_ms:
                raise Exception("No valid frame received.")
            time.sleep(0.01)

        cloud = self._last_cloud
        self._last_cloud = None  # Reset for next frame

        return cloud

