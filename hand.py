import cv2
import mediapipe as mp
import os

# Optional: silence TF warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

# Control value
value = 50.0
VALUE_MIN = 0
VALUE_MAX = 100
MAX_SPEED = 2.5   # higher = faster change

def count_open_fingers(hand_landmarks):
    tips = [8, 12, 16, 20]   # fingertips
    pips = [6, 10, 14, 18]  # PIP joints

    count = 0
    for tip, pip in zip(tips, pips):
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[pip].y:
            count += 1
    return count

with mp_hands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
) as hands:

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_draw.draw_landmarks(
                    frame, hand_landmarks, mp_hands.HAND_CONNECTIONS
                )

                open_fingers = count_open_fingers(hand_landmarks)

                # Map fingers (0–4) → control (-1 to +1)
                control = (open_fingers - 2) / 2.0

                # Dead zone (prevents jitter)
                if abs(control) < 0.2:
                    control = 0.0

                # Proportional update
                value += control * MAX_SPEED

                # Clamp value
                value = max(VALUE_MIN, min(VALUE_MAX, value))

                cv2.putText(
                    frame,
                    f"Fingers: {open_fingers}",
                    (30, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255, 255, 0),
                    2
                )

        cv2.putText(
            frame,
            f"Value: {int(value)}",
            (30, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.4,
            (0, 255, 0),
            3
        )

        cv2.imshow("Hand Proportional Control", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
