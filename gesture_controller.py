import cv2
import mediapipe as mp
import pyautogui
import numpy as np

# ================= SCREEN SIZE ================= #

screen_width, screen_height = pyautogui.size()

# ================= CAMERA ================= #

cap = cv2.VideoCapture(0)

# ================= MEDIAPIPE ================= #

mpHands = mp.solutions.hands

hands = mpHands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

mpDraw = mp.solutions.drawing_utils

tipIds = [4, 8, 12, 16, 20]

# ================= AIR CANVAS ================= #

canvas = None

prev_x = 0
prev_y = 0

draw_color = (255, 0, 255)

# ================= MODE ================= #

mode = "HAND TRACKING"

# ================= FINGER DETECTION ================= #

def fingers_up(lmList):

    fingers = []

    # Thumb
    if lmList[4][1] > lmList[3][1]:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other fingers
    for id in range(1, 5):

        if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
            fingers.append(1)

        else:
            fingers.append(0)

    return fingers

# ================= MAIN LOOP ================= #

while True:

    success, img = cap.read()

    if not success:
        continue

    img = cv2.flip(img, 1)

    h, w, c = img.shape

    if canvas is None:
        canvas = np.zeros_like(img)

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = hands.process(imgRGB)

    lmList = []

    if results.multi_hand_landmarks:

        for handLms in results.multi_hand_landmarks:

            mpDraw.draw_landmarks(
                img,
                handLms,
                mpHands.HAND_CONNECTIONS
            )

            for id, lm in enumerate(handLms.landmark):

                cx = int(lm.x * w)
                cy = int(lm.y * h)

                lmList.append((id, cx, cy))

    if len(lmList) != 0:

        fingers = fingers_up(lmList)

        # ================= MODES ================= #

        # ☝️ Mouse Mode
        if fingers == [0, 1, 0, 0, 0]:
            mode = "MOUSE MODE"

        # ✌️ Air Canvas
        elif fingers == [0, 1, 1, 0, 0]:
            mode = "AIR CANVAS"

        # 🤟 Volume Mode
        elif fingers == [0, 1, 1, 1, 0]:
            mode = "VOLUME MODE"

        # ✋ Hand Tracking
        elif fingers == [1, 1, 1, 1, 1]:
            mode = "HAND TRACKING"

        # 👍 Clear Canvas
        elif fingers == [1, 0, 0, 0, 0]:
            canvas = np.zeros_like(img)

        # 👊 Pause
        elif fingers == [0, 0, 0, 0, 0]:
            mode = "PAUSED"

        # ================= SHOW MODE ================= #

        cv2.putText(
            img,
            f"MODE: {mode}",
            (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 255),
            3
        )

        # ================= MOUSE MODE ================= #

        if mode == "MOUSE MODE":

            x1, y1 = lmList[8][1], lmList[8][2]

            screen_x = int(screen_width * x1 / w)
            screen_y = int(screen_height * y1 / h)

            pyautogui.moveTo(screen_x, screen_y)

        # ================= AIR CANVAS ================= #

        elif mode == "AIR CANVAS":

            x = lmList[8][1]
            y = lmList[8][2]

            cv2.circle(img, (x, y), 10, draw_color, -1)

            if prev_x == 0 and prev_y == 0:
                prev_x, prev_y = x, y

            cv2.line(
                canvas,
                (prev_x, prev_y),
                (x, y),
                draw_color,
                5
            )

            prev_x = x
            prev_y = y

        else:
            prev_x = 0
            prev_y = 0

        # ================= VOLUME MODE ================= #

        if mode == "VOLUME MODE":

            x1, y1 = lmList[4][1], lmList[4][2]
            x2, y2 = lmList[8][1], lmList[8][2]

            length = np.hypot(x2 - x1, y2 - y1)

            # Volume Up
            if length > 100:
                pyautogui.press("volumeup")

            # Volume Down
            if length < 50:
                pyautogui.press("volumedown")

            cv2.putText(
                img,
                "VOLUME CONTROL",
                (20, 100),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                3
            )

    # ================= MERGE CANVAS ================= #

    img = cv2.add(img, canvas)

    # ================= TITLE ================= #

    cv2.putText(
        img,
        "AI HAND GESTURE CONTROL",
        (20, 450),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        3
    )

    # ================= SHOW WINDOW ================= #

    cv2.imshow("Gesture Controller", img)

    key = cv2.waitKey(1)

    # ESC to Exit
    if key & 0xFF == 27:
        break

# ================= RELEASE ================= #

cap.release()

cv2.destroyAllWindows()