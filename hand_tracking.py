import cv2
import mediapipe as mp

# Start camera
cap = cv2.VideoCapture(0)

# Mediapipe setup
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

# Finger tip IDs
tipIds = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()

    # Convert image to RGB
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    lmList = []

    # If hand detected
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:

            # Get landmark positions
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append((id, cx, cy))

            # Draw hand
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    # If landmarks exist
    if len(lmList) != 0:
        fingers = []

        # Thumb (special case)
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # Other 4 fingers
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        # Count fingers
        totalFingers = fingers.count(1)

        # Display count
        cv2.putText(img, f'Fingers: {totalFingers}', (50, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)

    # Show output
    cv2.imshow("Hand Tracking", img)

    # Exit on ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Release camera
cap.release()
cv2.destroyAllWindows()