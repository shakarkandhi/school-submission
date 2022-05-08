import mediapipe as mp
import cv2
import numpy as np
import uuid
import os
from matplotlib import pyplot as plt


def draw_finger_angles(image, results):
    joint_list = [[7, 6, 5], [11, 10, 9], [15, 14, 13],
                  [19, 18, 17], [4, 3, 2], [3, 2, 1]]
    fingers1 = 0
    fingers2 = 0
    angle1 = []
    angle2 = []

    hand1 = results.multi_hand_landmarks[0]
    # for first hand
    for joint in joint_list:
        # First coord
        a = np.array([hand1.landmark[joint[0]].x,
                     hand1.landmark[joint[0]].y])
        # Second coord
        b = np.array([hand1.landmark[joint[1]].x,
                     hand1.landmark[joint[1]].y])
        # Third coord
        c = np.array([hand1.landmark[joint[2]].x,
                     hand1.landmark[joint[2]].y])

        radians = np.arctan2(c[1] - b[1], c[0]-b[0]) - \
            np.arctan2(a[1]-b[1], a[0]-b[0])
        angle1.append(np.abs(radians*180.0/np.pi))

    for i in range(0, 4):
        if angle1[i] > 160:
            fingers1 += 1
    cv2.putText(image, "hand1-"+str(fingers1), (10, 50), cv2.FONT_HERSHEY_SIMPLEX,
                2, (255, 255, 255), 2, cv2.LINE_AA)
    try:
        hand2 = results.multi_hand_landmarks[1]
        # for second hand
        for joint in joint_list:
            # First coord
            a = np.array([hand2.landmark[joint[0]].x,
                          hand2.landmark[joint[0]].y])
            # Second coord
            b = np.array([hand2.landmark[joint[1]].x,
                          hand2.landmark[joint[1]].y])
            # Third coord
            c = np.array([hand2.landmark[joint[2]].x,
                          hand2.landmark[joint[2]].y])

            radians = np.arctan2(c[1] - b[1], c[0]-b[0]) - \
                np.arctan2(a[1]-b[1], a[0]-b[0])
            angle2.append(np.abs(radians*180.0/np.pi))

        for i in range(0, 4):
            if angle2[i] > 160:
                fingers2 += 1
        cv2.putText(image, "hand2-"+str(fingers2), (10, 150), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 255, 255), 2, cv2.LINE_AA)

    except:
        pass

    return image


mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read()

        # BGR 2 RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (1024, 576))

        # Flip on horizontal
        image = cv2.flip(image, 1)

        # Set flag
        image.flags.writeable = False

        # Detections
        results = hands.process(image)

        # Set flag to true
        image.flags.writeable = True

        # RGB 2 BGR
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Number of fingers

        # Rendering results
        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS,
                                          mp_drawing.DrawingSpec(
                                              color=(121, 22, 76), thickness=2, circle_radius=4),
                                          mp_drawing.DrawingSpec(
                                              color=(250, 44, 250), thickness=2, circle_radius=2),
                                          )
            draw_finger_angles(image, results)

        # Save our image
        cv2.imwrite(os.path.join('Output Images',
                    '{}.jpg'.format(uuid.uuid1())), image)
        cv2.imshow('Hand Tracking', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
