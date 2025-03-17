# AXD Digital Report: Motion-Controlled Audio Interaction

[![Hand Tracking and Gesture Recognition](http://img.youtube.com/vi/Smdt0wwmDsk/0.jpg)](http://www.youtube.com/watch?v=Smdt0wwmDsk)

## Overview  
This project explores the use of **real-time hand tracking and gesture recognition** to control audio elements interactively.  
Using **MediaPipe**, **Max/MSP Jitter**, and **UDP communication**, this system enables users to manipulate musical components (e.g., toggling instruments, generating drum beats) using **motion gestures**.

This work was developed as part of the **Audio Experience Design (AXD) module** at the **Dyson School of Design Engineering**.  
The final deliverable contributes to an **interactive audio experience installation**, where users engage with music through intuitive **gesture-based interactions**.

---

## **Project Features**  

✅ **Hand Tracking & Gesture Recognition** – Uses Google’s **MediaPipe** to track hand landmarks and classify gestures.  
✅ **UDP Server for Real-Time Data Transmission** – Sends hand position, gestures, and detected motion via **OSC (Open Sound Control)**.  
✅ **Max/MSP Integration** – Controls **audio-reactive visuals** and generates drum beats in real-time.  
✅ **Gesture-Based Instrument Control** – Allows users to **toggle musical components on and off**.  
✅ **Grid-Based Interaction** – Maps hand positions to an **8×3 grid** to **trigger drum sounds dynamically**.  

---

## **Installation & Dependencies**  

Before running, ensure you have **Python 3.7 - 3.10** installed. Then, install the required libraries:

```bash
pip install mediapipe
pip install opencv-python
pip install python-osc


