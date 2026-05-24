import cv2
import time

cap = cv2.VideoCapture(0)

printed = False

if not cap.isOpened():
    print("Camera not accessible")

else:
    print("Camera is active")

    while True:
        ret, frame = cap.read()

        if ret:

            if not printed:
                print("Webcam is being used")

                with open("log.txt", "a") as f:
                    f.write(f"Accessed at {time.ctime()}\n")

                printed = True

            cv2.imshow('Webcam Monitor', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
