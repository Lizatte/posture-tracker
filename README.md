\# Ergonomic Buddy



AI-powered desk posture monitor. A camera and Raspberry Pi Zero 2 W detect poor posture using MediaPipe landmarks and rule-based ergonomic thresholds, and alert the user with an LED and buzzer. All processing happens on the device.



\## Team

\- \[Your name]

\- \[Partner's name]



\## Setup

1\. Create a virtual environment: `python -m venv venv`

2\. Activate it: `venv\\Scripts\\activate.bat`

3\. Install libraries: `pip install -r requirements.txt`

4\. Run: `python webcam.py`



\## Current Status

Stage 1: webcam feed (in progress)
Stage 2: MediaPipe body landmark detection (next)
- **Stage 2 — MediaPipe body landmark detection: In progress.** Downloaded the Lite model; integrating detection into `webcam.py` is next.

\## Progress Log
(Newest first)

### November 16, 2026 — Stage 2 Model Setup

- **Did:** Downloaded `pose_landmarker_lite.task` into the project folder using `curl.exe`.
- **Problem:** The installed MediaPipe version does not include the older `mp.solutions` interface.
- **Fix/Decision:** Use the MediaPipe Pose Landmarker API with the downloaded Lite model. The download completed successfully (5.50 MB).
- **Next:** Load the model in `webcam.py`, then detect and display body landmarks.

### 11/16/2026, ~11:30 AM

- **Did:** Created `webcam.py` using OpenCV. Wrote a `while True` loop to continuously capture and display live video from the laptop webcam. Added a keypress condition to exit the program.

- **Problem:** Needed to understand why `cap.read()` returns two values and why `cv2.waitKey()` is necessary for the webcam window to function properly.

- **Fix/Decision:** Used `ret` to check whether each frame was captured successfully before displaying it. Added `cv2.waitKey(1)` to process window events and detect when Q is pressed. Used `cap.release()` and `cv2.destroyAllWindows()` to close the camera and window properly. Tested the program successfully.

- **Next:** Stage 2, integrate MediaPipe to detect and display body landmarks in real time.

\### 10/18/2026, \~4:08 PM

\- \*\*Did:\*\* Created the posture-tracker project folder, set up a virtual environment, installed OpenCV and MediaPipe, wrote check.py to confirm both import, set up Git, and made the first commit (b968bed).

\- \*\*Problem:\*\* check.py ran with no output at first, because the file was empty (the code hadn't been saved). Windows also saved .gitignore as .gitignore.txt, so Git ignored it.

\- \*\*Fix/Decision:\*\* Saved check.py, which then printed "OpenCV: 5.0.0" and "MediaPipe imported OK". Renamed the file with `ren .gitignore.txt .gitignore`.

\- \*\*Next:\*\* Stage 1, live webcam feed (webcam.py).



\### 11/16/2026, 3:30 PM

\- \*\*Did:\*\* Started webcam.py. Opened the camera with cv2.VideoCapture(0).

\- \*\*Problem:\*\* Window showed nothing.

\- \*\*Fix/Decision:\*\* Needed cv2.waitKey() for the window to display.

\- \*\*Next:\*\* Make the feed loop and quit on 'q'.



\### 10/18/2026, 4:08 PM

\- \*\*Did:\*\* Set up venv, installed OpenCV and MediaPipe, first Git commit.

\- \*\*Problem:\*\* Windows saved .gitignore as .gitignore.txt.

\- \*\*Fix/Decision:\*\* Renamed it in the terminal with `ren`.

\- \*\*Next:\*\* Stage 1, webcam feed.



\## Hardware Parts Log

(Add dates when parts are ordered and arrive)



\## Test Results

(Add accuracy and latency numbers here later)



\## References

\- MediaPipe, OpenCV docs, OSHA Computer Workstations eTool

