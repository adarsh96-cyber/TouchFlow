import cv2
import mediapipe as mp
import csv
import time

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

label = input("Enter Gesture Name: ")

file = open("gesture_data.csv", "a", newline="")
csv_writer = csv.writer(file)

last_save_time = time.time()

sample_count = 0

MAX_SAMPLES = 100

while True:

    success, img = cap.read()

    img = cv2.flip(img, 1)

    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    result = hands.process(rgb)

    if result.multi_hand_landmarks:

        for handLms in result.multi_hand_landmarks:

            mp_draw.draw_landmarks(
                img,
                handLms,
                mp_hands.HAND_CONNECTIONS
            )

            current_time = time.time()

            if current_time - last_save_time > 0.3:

                row = []

                for lm in handLms.landmark:

                    row.append(lm.x)
                    row.append(lm.y)

                row.append(label)

                csv_writer.writerow(row)

                sample_count += 1

                print("Saved:", sample_count)

                last_save_time = current_time

    cv2.putText(
        img,
        f"Samples: {sample_count}",
        (20,50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        2
    )

    cv2.imshow("Data Collection", img)

    if sample_count >= MAX_SAMPLES:
        print("Completed")
        break

cap.release()
file.close()
cv2.destroyAllWindows()