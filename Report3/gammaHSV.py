import cv2
from grayscale import readImage
from gammaCV import gammaLUT

winRes = 'Result'
tracks = ('R', 'G', 'B')


def changeGamma(val):
    global img, lookUpTable
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    planes = cv2.split(imgHSV)
    for i in range(len(tracks)):
        val = cv2.getTrackbarPos(tracks[i], winRes)
        planes[i] = cv2.LUT(planes[i], lookUpTable[val])
    imgHSV = cv2.merge(planes)
    cv2.imshow(winRes, cv2.cvtColor(imgHSV, cv2.COLOR_HSV2BGR))


def main():
    global img, lookUpTable
    img = readImage()
    trackHalf = 128
    trackMax = trackHalf * 2
    lookUpTable = gammaLUT(trackHalf, trackMax)
    cv2.namedWindow(winRes)
    for i in range(len(tracks)):
        cv2.createTrackbar(tracks[i], winRes, 0, trackMax, changeGamma)
        cv2.setTrackbarPos(tracks[i], winRes, trackHalf)

    changeGamma(trackHalf)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
