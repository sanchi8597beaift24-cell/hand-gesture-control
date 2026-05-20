import cv2
import mediapipe as mp
import numpy as np

# ================= CAMERA ================= #

cap = cv2.VideoCapture(0)

# ================= MEDIAPIPE ================= #

mpHands = mp.solutions.hands

hands = mpHands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

mpDraw = mp.solutions.drawing_utils

# ================= CANVAS ================= #

canvas = None

# Previous coordinates
prev_x = 0
prev_y = 0

# Drawing color
draw_color = (255, 0, 255)

# Brush thickness
brush_thickness = 5

# Finger tip IDs
tipIds = [4, 8, 12, 16, 20]

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

    # Flip image
    img = cv2.flip(img, 1)

    h, w, c = img.shape

    # Create canvas
    if canvas is None:
        canvas = np.zeros_like(img)

    # RGB convert
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Hand processing
    results = hands.process(imgRGB)

    lmList = []

    # ================= COLOR BOXES ================= #

    cv2.rectangle(img, (10, 10), (110, 60), (255, 0, 0), -1)
    cv2.rectangle(img, (130, 10), (230, 60), (0, 255, 0), -1)
    cv2.rectangle(img, (250, 10), (350, 60), (0, 0, 255), -1)
    cv2.rectangle(img, (370, 10), (470, 60), (0, 255, 255), -1)
    cv2.rectangle(img, (490, 10), (590, 60), (255, 255, 255), -1)

    cv2.putText(img, "BLUE", (20, 45),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                (255, 255, 255), 2)

    cv2.putText(img, "GREEN", (135, 45),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                (255, 255, 255), 2)

    cv2.putText(img, "RED", (275, 45),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                (255, 255, 255), 2)

    cv2.putText(img, "YELLOW", (375, 45),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                (0, 0, 0), 2)

    cv2.putText(img, "ERASER", (500, 45),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                (0, 0, 0), 2)

    # ================= HAND DETECTION ================= #

    if results.multi_hand_landmarks:

        for handLms in results.multi_hand_landmarks:

            # Draw landmarks
            mpDraw.draw_landmarks(
                img,
                handLms,
                mpHands.HAND_CONNECTIONS
            )

            # Get landmark positions
            for id, lm in enumerate(handLms.landmark):

                cx = int(lm.x * w)
                cy = int(lm.y * h)

                lmList.append((id, cx, cy))

    # ================= MAIN LOGIC ================= #

    if len(lmList) != 0:

        # Index finger tip
        x = lmList[8][1]
        y = lmList[8][2]

        # Draw pointer
        cv2.circle(img, (x, y), 10, draw_color, -1)

        # Detect fingers
        fingers = fingers_up(lmList)

        # ================= CLEAR SCREEN ================= #

        if fingers == [1, 1, 1, 1, 1]:

            canvas = np.zeros_like(img)

            cv2.putText(
                img,
                "SCREEN CLEARED",
                (20, 150),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 255, 255),
                3
            )

        # ================= ERASER MODE ================= #

        elif fingers == [0, 1, 1, 1, 0]:

            draw_color = (0, 0, 0)
            brush_thickness = 30

            cv2.putText(
                img,
                "ERASER MODE",
                (20, 150),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                3
            )

        else:

            brush_thickness = 5

            # ================= COLOR SELECTION ================= #

            if y < 60:

                # Blue
                if 10 < x < 110:
                    draw_color = (255, 0, 0)

                # Green
                elif 130 < x < 230:
                    draw_color = (0, 255, 0)

                # Red
                elif 250 < x < 350:
                    draw_color = (0, 0, 255)

                # Yellow
                elif 370 < x < 470:
                    draw_color = (0, 255, 255)

                # White / Eraser
                elif 490 < x < 590:
                    draw_color = (0, 0, 0)

            # ================= DRAWING ================= #

            else:

                if prev_x == 0 and prev_y == 0:
                    prev_x, prev_y = x, y

                cv2.line(
                    canvas,
                    (prev_x, prev_y),
                    (x, y),
                    draw_color,
                    brush_thickness
                )

                prev_x = x
                prev_y = y

    else:

        prev_x = 0
        prev_y = 0

    # Merge canvas
    img = cv2.add(img, canvas)

    # Heading
    cv2.putText(
        img,
        "AIR CANVAS",
        (20, 100),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        3
    )

    # Show window
    cv2.imshow("Air Canvas", img)

    key = cv2.waitKey(1)

    # ESC to exit
    if key & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()