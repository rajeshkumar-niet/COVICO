# Importing dependencies
import numpy as np
import cv2
import os
from cvzone.HandTrackingModule import HandDetector

# Folder containing presentation images
folderPath = "PPT/img"

# Setup for video capture and display window dimensions
width, height = 1200, 720
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

# Get the images from the folder
pathImages = os.listdir(folderPath)

# Parameters for resizing the webcam feed
ratio = 0.15
ws, hs = int(width * ratio), int(height * ratio)

# Hand detector initialization
detector = HandDetector(detectionCon=0.7, maxHands=1)

# Initialize button press variables
buttonPressed = False
buttonCounter = 0
buttonDelay = 15

# Resizing the presentation images (optimized)
resizedImages = []
for imgPath in pathImages:
    imgCurrent = cv2.imread(os.path.join(folderPath, imgPath))
    aspectRatio = imgCurrent.shape[1] / imgCurrent.shape[0]
    newWidth, newHeight = 720, int(720 / aspectRatio)
    resizedImages.append(cv2.resize(imgCurrent, (newWidth, newHeight)))

# Initialize variables for presentation and annotations
imgNumber = 0
annotations = [[]]
annotationsNumber = -1
annotationsStart = False

def handle_gestures(fingers, imgNumber, annotations, annotationsNumber, annotationsStart):
    global buttonPressed

    if fingers == [1, 0, 0, 0, 0] and imgNumber > 0:
        print("Left")
        buttonPressed = True
        return imgNumber - 1, [[]], -1, False
    
    if fingers == [0, 0, 0, 0, 1] and imgNumber < len(pathImages) - 1:
        print("Right")
        buttonPressed = True
        return imgNumber + 1, [[]], -1, False
    
    return imgNumber, annotations, annotationsNumber, annotationsStart

def update_annotations(fingers, annotations, annotationsNumber, indexFinger):
    global annotationsStart

    if fingers == [0, 1, 0, 0, 0]:
        print("Pointer")
        cv2.circle(resizedCurrent, indexFinger, 15, (0, 0, 255), cv2.FILLED)
    
    elif fingers == [0, 1, 1, 0, 0]:
        print("Draw")
        if not annotationsStart:
            annotationsStart = True
            annotationsNumber += 1
            annotations.append([])

        cv2.circle(resizedCurrent, indexFinger, 15, (0, 0, 255), cv2.FILLED)
        annotations[annotationsNumber].append(indexFinger)
    
    elif fingers == [0, 1, 1, 1, 0]:
        print("Erase")
        if annotations and annotationsNumber >= 0:
            annotations.pop()
            annotationsNumber -= 1
    
    return annotations, annotationsNumber

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)  # Mirror the webcam feed
    imgH, imgW = img.shape[:2]

    # Draw a green line in the middle of the webcam feed
    cv2.line(img, (0, int(imgH / 2)), (int(imgW), int(imgH / 2)), (0, 255, 0), 2)

    # Resize the webcam feed and overlay it onto the presentation
    videoSmall = cv2.resize(img, (ws, hs))
    resizedCurrent = resizedImages[imgNumber].copy()
    resizedCurrent[0:hs, -ws:] = videoSmall

    # Detect hands in the webcam feed
    hands, img = detector.findHands(img, flipType=False)

    if hands and not buttonPressed:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        lmList = hand['lmList']

        # Interpolate and constrain finger positions
        xVal = np.clip(int(np.interp(lmList[8][0], [width // 2 - 100, width - 100], [50, 600])), 0, 720)
        yVal = np.clip(int(np.interp(lmList[8][1], [150, height - 150], [0, height])), 0, height)
        indexFinger = (xVal, yVal)

        # Handle gestures for switching slides
        imgNumber, annotations, annotationsNumber, annotationsStart = handle_gestures(fingers, imgNumber, annotations, annotationsNumber, annotationsStart)
        
        # Update annotations (draw, erase, pointer)
        annotations, annotationsNumber = update_annotations(fingers, annotations, annotationsNumber, indexFinger)
    
    # Draw saved annotations on the presentation
    for annotation in annotations:
        for i in range(1, len(annotation)):
            cv2.line(resizedCurrent, annotation[i-1], annotation[i], (0, 200, 0), 10)

    # Button press delay to avoid multiple actions
    if buttonPressed:
        buttonCounter += 1
        if buttonCounter > buttonDelay:
            buttonCounter = 0
            buttonPressed = False

    # Display the slides and webcam feed
    cv2.imshow("Presentation", resizedCurrent)
    cv2.imshow("Img", img)

    # Exit on 'q' key press
    if cv2.waitKey(1) == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
