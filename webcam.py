import time
from pathlib import Path

import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision


# Find the model in the same folder as this script.
model_path = Path(__file__).parent / "pose_landmarker_lite.task"

# Configure detection for a sequence of video frames.
options = vision.PoseLandmarkerOptions(
    base_options=python.BaseOptions(model_asset_path=str(model_path)),
    running_mode=vision.RunningMode.VIDEO,
    num_poses=1,
)

with vision.PoseLandmarker.create_from_options(options) as detector:
    cap = cv2.VideoCapture(0)
    start_time = time.monotonic()
    last_timestamp = -1

    try:
        if not cap.isOpened():
            raise RuntimeError("Could not open the webcam.")

        while True:
            ret, frame = cap.read()

            if not ret:
                print("Failed to capture frame")
                break

            # OpenCV uses BGR colors; MediaPipe needs RGB.
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            mp_image = mp.Image(
                image_format=mp.ImageFormat.SRGB,
                data=rgb_frame,
            )

            # Each frame needs an increasing timestamp in milliseconds.
            timestamp = int((time.monotonic() - start_time) * 1000)
            timestamp = max(timestamp, last_timestamp + 1)
            last_timestamp = timestamp

            result = detector.detect_for_video(mp_image, timestamp)

            # Convert landmark coordinates into pixel positions.
            height, width = frame.shape[:2]

            for pose in result.pose_landmarks:
                for landmark in pose:
                    if landmark.visibility is not None:
                        if landmark.visibility < 0.5:
                            continue

                    x = int(landmark.x * width)
                    y = int(landmark.y * height)
                    cv2.circle(frame, (x, y), 4, (0, 255, 0), -1)

            cv2.imshow("Ergonomic Buddy", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    finally:
        cap.release()
        cv2.destroyAllWindows()