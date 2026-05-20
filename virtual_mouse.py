import cv2
import mediapipe as mp
import pyautogui
import math
import time

# Camera
cap = cv2.VideoCapture(0)

# Screen size
screen_width, screen_height = pyautogui.size()

# Mediapipe setup
mpHands = mp.solutions.hands

hands = mpHands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

mpDraw = mp.solutions.drawing_utils

# Smoothening variables
prev_x = 0
prev_y = 0

smoothening = 5

# Click delay
last_click = 0

while True:

    success, img = cap.read()

    if not success:
        continue

    # Flip image
    img = cv2.flip(img, 1)

    h, w, c = img.shape

    # RGB
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Process hand
    results = hands.process(imgRGB)

    lmList = []

    if results.multi_hand_landmarks:

        for handLms in results.multi_hand_landmarks:

            mpDraw.draw_landmarks(
                img,
                handLms,
                mpHands.HAND_CONNECTIONS
            )

            # Get landmarks
            for id, lm in enumerate(handLms.landmark):

                cx = int(lm.x * w)
                cy = int(lm.y * h)

                lmList.append((id, cx, cy))

    # ================= MAIN ================= #

    if len(lmList) != 0:

        # Index finger tip
        x1, y1 = lmList[8][1], lmList[8][2]

        # Thumb tip
        x2, y2 = lmList[4][1], lmList[4][2]

        # ================= SMOOTH MOUSE ================= #

        screen_x = screen_width * x1 / w
        screen_y = screen_height * y1 / h

        # Smooth movement
        curr_x = prev_x + (screen_x - prev_x) / smoothening
        curr_y = prev_y + (screen_y - prev_y) / smoothening

        pyautogui.moveTo(curr_x, curr_y)

        prev_x = curr_x
        prev_y = curr_y

        # Show mode
        cv2.putText(
            img,
            "MOVE",
            (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            3
        )

        # ================= CLICK ================= #

        distance = math.hypot(x2 - x1, y2 - y1)

        # Draw line
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)

        # Click gesture
        if distance < 35:

            current_time = time.time()

            # Delay to avoid multiple clicks
            if current_time - last_click > 1:

                pyautogui.click()

                last_click = current_time

                cv2.putText(
                    img,
                    "CLICK",
                    (20, 100),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 255),
                    3
                )

    # Show window
    cv2.imshow("Virtual Mouse", img)

    # ESC to exit
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()