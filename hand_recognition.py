#https://github.com/Sousannah/hand-tracking-using-mediapipe
import cv2
import mediapipe as mp
#import numpy as np
from pythonosc.udp_client import SimpleUDPClient
import time
from pathlib import Path

pTime = 0
cTime = 0

lmkNames = ["wrist", "thumb_cmc", "thumb_mcp", "thumb_ip", "thumb_tip",
            "index_finger_mcp", "index_finger_pip", "index_finger_dip", "index_finger_tip",
            "middle_finger_mcp", "middle_finger_pip", "middle_finger_dip", "middle_finger_tip",
            "ring_finger_mcp", "ring_finger_pip", "ring_finger_dip", "ring_finger_tip",
            "pinky_mcp", "pinky_pip", "pinky_dip", "pinky_tip"]

lmksToDraw = [0, 4, 8, 12, 16, 20]

# Set the IP and port (MaxMSP listens on port 7400)
ip = "127.0.0.1"
port = 7400

BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
GestureRecognizerResult = mp.tasks.vision.GestureRecognizerResult
VisionRunningMode = mp.tasks.vision.RunningMode

# Create a gesture recognizer instance with the image mode:
# TODO why would I use live stream mode vs image mode?

with open(str(Path("./gesture_recognizer.task").resolve()), 'rb') as file:
    model_data = file.read()

    options = GestureRecognizerOptions(
        base_options=BaseOptions(model_asset_buffer=model_data),
        running_mode=VisionRunningMode.IMAGE,
        num_hands=2)
    with GestureRecognizer.create_from_options(options) as recognizer:

        cap = cv2.VideoCapture(0)

        client = SimpleUDPClient(ip, port) # Create an OSC client

        while True:
            success, img = cap.read()
            h, w, c = img.shape
            img = cv2.flip(img, 1)
            imgRGBified = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=imgRGBified)
            awaitResult = True
            result = recognizer.recognize(mp_image)

            #img = np.zeros((h, w, 3), np.uint8)

            client.send_message("/numHands", [len(result.hand_world_landmarks)])

            handID = 0
            for hand in result.hand_landmarks:
                id = 0
                for landmark in hand:
                    #print(landmark.x)
                    client.send_message("/" + lmkNames[id] + "_" + str(handID), [int(landmark.x * 1000), int(landmark.y * 1000), int(landmark.z * 1000)])

                    if id in lmksToDraw:
                        cx, cy = int(landmark.x * w), int(landmark.y * h)
                        cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)


                    id = id + 1
                handID = handID + 1

            handID = 0
            for hand in result.gestures:
                #print(hand[0].category_name)
                client.send_message("/gesture" + "_" + str(handID), [hand[0].category_name])
                cv2.putText(img, hand[0].category_name, (10, (handID + 1) * 80), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
                handID = handID + 1

            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime

            cv2.putText(img, str(int(fps)), (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 3)
            cv2.imshow("Image", img)

            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break

cap.release()
cv2.destroyAllWindows()
