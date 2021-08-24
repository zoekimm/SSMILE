import cv2 #openCV

def read_image():
    path = input('Type the full path for your image\n')
    img = cv2.imread(path) #read the image
    cv2.imshow("Selected image", img) #display the image
    cv2.waitKey(0)

def read_video():
    path = input('Type the full path for your video\n')
    vid = cv2.VideoCapture(path)  # read the image
    if not vid.isOpened():
        print('The program failed to open the video\n')

    while vid.isOpened():
        ret, frame = vid.read()
        if ret:
            cv2.imshow("Selected video", frame)  # display the image
            cv2.waitKey(0)
