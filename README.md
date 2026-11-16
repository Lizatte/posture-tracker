# Ergonomic Buddy

Ergonomic Buddy is a desk posture monitor in development. The planned system will use a camera, MediaPipe body landmarks, and rule-based ergonomic thresholds to detect poor posture and alert the user with an LED and buzzer. Processing is intended to happen locally on the device.

The hardware platform is still undecided. A Raspberry Pi Zero 2 W was considered, but no model has been selected. Development so far has used a laptop webcam and OpenCV.

## Team

- [Your name]
- [Partner's name]

## Setup

Run these commands from the project folder. The activation command below is for Windows Command Prompt.

1. Create a virtual environment:
   ```cmd
   python -m venv venv
   ```
2. Activate the virtual environment:
   ```cmd
   venv\Scripts\activate.bat
   ```
3. Install the required libraries:
   ```cmd
   pip install -r requirements.txt
   ```
4. Run the webcam program:
   ```cmd
   python webcam.py
   ```

Press **Q** while the webcam window is active to exit.

## Current Status

- **Stage 1 — Live webcam feed: Completed.** The laptop webcam feed displays continuously, supports quitting with Q, and releases the camera and closes the window when finished.
- **Stage 2 — MediaPipe body landmark detection: Next.** Integrate MediaPipe to detect and display body landmarks in real time.
- **Hardware selection: Undecided.**

## Progress Log

Newest entries appear first. The November 16 notes are combined under one date because their recorded times conflict.

### November 16, 2026 — Stage 1 Completed

- **Did:** Created `webcam.py` using OpenCV. Opened the laptop webcam with `cv2.VideoCapture(0)` and used a `while True` loop to continuously capture and display live video. Added a keypress condition to exit the program.
- **Problem:** The initial webcam window showed nothing. Needed to understand why `cap.read()` returns two values and why `cv2.waitKey()` is necessary for the webcam window to function properly.
- **Fix/Decision:** Added `cv2.waitKey()` so the window could display and process events. Used `ret`, the success flag returned alongside the frame by `cap.read()`, to check whether each frame was captured successfully before displaying it. Used `cv2.waitKey(1)` to process window events and detect when Q is pressed. Added `cap.release()` and `cv2.destroyAllWindows()` to release the camera and close the window properly. Tested the program successfully, completing Stage 1.
- **Next:** Stage 2 — integrate MediaPipe to detect and display body landmarks in real time.

### October 18, 2026 — Project Setup

- **Did:** Created the `posture-tracker` project folder, set up a virtual environment, installed OpenCV and MediaPipe, wrote `check.py` to confirm both libraries import, set up Git, and made the first commit (`b968bed`).
- **Problem:** `check.py` initially ran with no output because the file was empty; the code had not been saved. Windows also saved `.gitignore` as `.gitignore.txt`, so Git did not recognize it as the ignore file.
- **Fix/Decision:** Saved `check.py`, which then printed `OpenCV: 5.0.0` and `MediaPipe imported OK`. Renamed the ignore file in the terminal with `ren .gitignore.txt .gitignore`.
- **Next:** Stage 1 — create a live webcam feed in `webcam.py`.

## Hardware Parts Log

Hardware selection is pending. Add selected parts and their order and arrival dates here as they are confirmed.

## Test Results

The Stage 1 webcam program was tested successfully, as recorded in the progress log. Add posture-detection accuracy and latency measurements here when available.

## References

- MediaPipe documentation
- OpenCV documentation
- OSHA Computer Workstations eTool
