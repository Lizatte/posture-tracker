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



\## Progress Log

(Newest first)

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

