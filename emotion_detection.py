import cv2
from fer import FER

# Initialize the emotion detector
emotion_detector = FER()

# Open webcamm
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Webcam started successfully. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Could not read the frame.")
        break

    # Detect emotions in the frame
    emotion, score = emotion_detector.top_emotion(frame)

    # Display detected emotion
    if emotion:
        cv2.putText(frame, f"{emotion} ({score:.2f})", (50, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('Real-Time Emotion Detection', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
