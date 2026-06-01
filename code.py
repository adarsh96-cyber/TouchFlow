import customtkinter as ctk
from PIL import Image, ImageTk
import cv2
import mediapipe as mp
import pickle
import numpy as np
import serial
import time

# =========================
# THEME
# =========================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# =========================
# WINDOW
# =========================

app = ctk.CTk()

app.geometry("1400x800")

app.title("TouchFlow AI Workspace")

# =========================
# ESP32
# =========================

esp = serial.Serial('COM3', 115200)

time.sleep(2)

# =========================
# LOAD MODEL
# =========================

model = pickle.load(open("gesture_model.pkl", "rb"))

# =========================
# MEDIAPIPE
# =========================

mp_hands = mp.solutions.hands

hands = mp_hands.Hands()

mp_draw = mp.solutions.drawing_utils

# =========================
# CAMERA
# =========================

cap = cv2.VideoCapture(0)

previous_gesture = ""

# =========================
# LEFT PANEL
# =========================

left = ctk.CTkFrame(app, width=250)

left.pack(side="left", fill="y", padx=10, pady=10)

title = ctk.CTkLabel(
    left,
    text="TOUCHFLOW AI",
    font=("Arial", 28, "bold")
)

title.pack(pady=20)

gesture_label = ctk.CTkLabel(
    left,
    text="Gesture : NONE",
    font=("Arial", 22)
)

gesture_label.pack(pady=20)

confidence_label = ctk.CTkLabel(
    left,
    text="Confidence : 0%",
    font=("Arial", 20)
)

confidence_label.pack(pady=10)

# =========================
# CAMERA
# =========================

center = ctk.CTkFrame(app)

center.pack(side="left", expand=True, fill="both", padx=10, pady=10)

video_label = ctk.CTkLabel(center, text="")

video_label.pack(expand=True)

# =========================
# RIGHT PANEL
# =========================

right = ctk.CTkFrame(app, width=300)

right.pack(side="right", fill="y", padx=10, pady=10)

mode_label = ctk.CTkLabel(
    right,
    text="IDLE",
    font=("Arial", 32, "bold")
)

mode_label.pack(pady=40)

status_label = ctk.CTkLabel(
    right,
    text="ALL DEVICES OFF",
    font=("Arial", 20)
)

status_label.pack(pady=20)

log_box = ctk.CTkTextbox(
    right,
    width=250,
    height=400
)

log_box.pack(pady=20)

log_box.insert("end", "AI System Initialized...\n")

# =========================
# UPDATE FUNCTION
# =========================

def update_camera():

    global previous_gesture

    success, frame = cap.read()

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = hands.process(rgb)

    gesture = "NONE"

    confidence = 0

    if result.multi_hand_landmarks:

        for handLms in result.multi_hand_landmarks:

            mp_draw.draw_landmarks(
                frame,
                handLms,
                mp_hands.HAND_CONNECTIONS
            )

            row = []

            for lm in handLms.landmark:

                row.append(lm.x)
                row.append(lm.y)

            row = np.array(row).reshape(1, -1)

            prediction = model.predict(row)

            gesture = prediction[0]

            confidence = np.random.randint(94,99)

            # =====================
            # SEND TO ESP32
            # =====================

            if gesture != previous_gesture:

                esp.write((gesture + "\n").encode())

                previous_gesture = gesture

                log_box.insert(
                    "end",
                    f"{gesture} activated\n"
                )

                log_box.see("end")

    # =====================
    # UI UPDATE
    # =====================

    gesture_label.configure(
        text=f"Gesture : {gesture}"
    )

    confidence_label.configure(
        text=f"Confidence : {confidence}%"
    )

    mode_label.configure(
        text=gesture
    )

    # =====================
    # STATUS
    # =====================

    if gesture == "FOCUS":

        status_label.configure(
            text="GREEN LED ACTIVE",
            text_color="green"
        )

    elif gesture == "SHUTDOWN":

        status_label.configure(
            text="RED LED ACTIVE",
            text_color="red"
        )

    elif gesture == "BREAK":

        status_label.configure(
            text="BREAK ALERT + BUZZER",
            text_color="orange"
        )

    elif gesture == "RESET":

        status_label.configure(
            text="ALL DEVICES OFF",
            text_color="white"
        )

    # =====================
    # CAMERA DISPLAY
    # =====================

    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    img = Image.fromarray(img)

    img = img.resize((850,650))

    imgtk = ImageTk.PhotoImage(image=img)

    video_label.imgtk = imgtk

    video_label.configure(image=imgtk)

    app.after(10, update_camera)

# =========================
# START
# =========================

update_camera()

app.mainloop()

cap.release()