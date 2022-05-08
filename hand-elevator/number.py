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

        cv2.putText(image, str(round(angle1[-1], 2)), tuple(np.multiply(b, [1024, 576]).astype(int)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

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

            cv2.putText(image, str(round(angle2[-1], 2)), tuple(np.multiply(b, [1024, 576]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
        for i in range(0, 4):
            if angle2[i] > 160:
                fingers2 += 1
        cv2.putText(image, "hand2-"+str(fingers2), (10, 150), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 255, 255), 2, cv2.LINE_AA)

    except:
        pass

    return image
