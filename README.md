AXD Digital Report: Motion-Controlled Audio Interaction


Overview
This project explores the use of real-time hand tracking and gesture recognition to control audio elements interactively. Using MediaPipe, Max/MSP Jitter, and UDP communication, this system enables users to manipulate musical components (e.g., toggling instruments, generating drum beats) using motion gestures.

This work was developed as part of the Audio Experience Design (AXD) module at the Dyson School of Design Engineering. The final deliverable contributes to an interactive audio experience installation, where users engage with music through intuitive gesture-based interactions.

Project Features
✅ Hand Tracking & Gesture Recognition: Uses Google’s MediaPipe to track hand landmarks and classify gestures.
✅ UDP Server for Real-Time Data Transmission: Sends hand position, gestures, and detected motion via OSC (Open Sound Control).
✅ Max/MSP Integration: Controls audio-reactive visuals and generates drum beats in real-time.
✅ Gesture-Based Instrument Control: Allows users to toggle musical components on and off.
✅ Grid-Based Interaction: Maps hand positions to an 8×3 grid to trigger drum sounds dynamically.

Installation & Dependencies
Before Running:
Ensure you have Python installed (recommended: Python 3.7 - 3.10). Install the necessary libraries:

bash
Copy
Edit
pip install mediapipe
pip install opencv-python
pip install python-osc
Running the Script:
To start hand tracking and UDP communication:

bash
Copy
Edit
python hand_recognition.py
Press 'q' to quit the program.

UDP Server: Data Format
The hand recognition script transmits data over UDP using Open Sound Control (OSC). The following endpoints are available:

1. Number of Hands Detected
/numHands -> [n]

n: Integer representing the number of hands detected (max: 2).
2. Handedness (Left/Right Hand Identification)
/handedness_<n> -> [h]

h: "right" or "left" for hand ID n.
3. Gesture Recognition
/gesture_<n> -> [g]

g: Recognized gesture (e.g., "Open_Palm", "Closed_Fist", "Victory", "Thumb_Up").
4. Hand Landmark Coordinates
/<landmark name>_<n> -> [x, y, z]

x, y, z: Normalized hand landmark coordinates (0-1000).
n: Hand ID.
📌 Example:
/wrist_0 -> [500, 300, 20] (Wrist coordinates for hand 0)


Image Source: Google AI MediaPipe

Technical Details
Hand Tracking & Motion Capture
Landmark Detection: MediaPipe extracts hand joints (wrist, fingertips, knuckles).
Gesture Recognition: A pre-trained model classifies gestures for real-time input.
Grid Mapping: Converts hand positions into a grid-based drum sequencer (8×3).
Max/MSP Integration
Drum Sequencer: Gestures trigger kick, snare, and hi-hat sounds based on position.
Visual Feedback: Uses Jitter to create audio-reactive visuals.
Dynamic Sound Control: Users can modify beats via hand movement and gestures.
Use Case: Interactive Music Performance
🎵 Drum Beat Generation:

Moving cubes trigger the kick drum.
Still cubes activate the snare drum.
Hi-hat follows the metronome.
🎶 Live Gesture-Based Audio Control:

Users toggle instruments on/off with gestures.
The grid system allows for dynamic beat sequencing.
Future Enhancements
📡 Multi-User Interaction: Support for multiple users controlling different instruments.
🎛️ Extended Gesture Library: More gesture-based audio effects.
🔊 Sound Spatialization: 3D positioning for immersive audio experiences.
🎨 Advanced Visuals: More complex generative graphics in Max/MSP Jitter.
Credits & Contributors
🎓 Developed for: Dyson School of Design Engineering – Audio Experience Design (AXD).
👨‍💻 Project Lead: Your Name
🔗 Repository: [GitHub Project Link]

