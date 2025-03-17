# AXD Digital Report

[![Ardalis.GuardClauses on YouTube](http://img.youtube.com/vi/Smdt0wwmDsk/0.jpg)](http://www.youtube.com/watch?v=Smdt0wwmDsk)

Motion Capture stuff:

Simple handlandmark detection and gesture recognition using mediapipe in python

Also sets up a UDP server that you can get the data from

For a university project.

### Before running:

```
pip install mediapipe
```
```
pip install opencv-python
```
```
pip install python-osc
```

To run:
```
python hand_recognition.py
```
Press q to quit

## UDP Server data format

There are 4 endpoints to get hand data from:

- ```/numHands -> [n]``` - Where ```n``` is an integer containing to number of hands currently being detected.
Currently max is set to 2, feel free to increase it in ```options = GestureRecognizerOptions( ... num_hands=2)```


- ```/handedness_<n> -> [h]``` - Where ```h``` is an string containing either ```right``` or ```left``` for hand id ```n```


- ```/gesture_<n> -> [g]```  - Where ```g``` is a string containing the name of the current gesture and ```n``` is the hand id.
Possible names are ```"None", "Closed_Fist", "Open_Palm", "Pointing_Up", "Thumb_Down", "Thumb_Up", "Victory", "ILoveYou"```


- ```/<landmark name>_<n> -> [x, y, z]``` - Where ```x```, ```y``` and ```z``` are the screen space coordinates (normalised from 0 - 1000) of the hand landmark with a name of ```<landmark name>```.
```n``` is the hand id.
e.g. ```/wrist``` would give you the coordinates of the wrist landmark.
Possible landmark names (use lowercase):
![](./hand_landmarks.png)
Image from: https://ai.google.dev/edge/mediapipe/solutions/vision/hand_landmarker
