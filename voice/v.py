import cv2

def Camera():
    cap = cv2.VideoCapture(0)
    print("Camera On")
    while True:
        _, frame = cap.read()

        cv2.imshow("Camera", frame)

        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def recognize_speech_from_mic():
    pass

def load_translations():
    pass

def main():
    pass

if __name__ == '__main__':
    Camera()
    main()
