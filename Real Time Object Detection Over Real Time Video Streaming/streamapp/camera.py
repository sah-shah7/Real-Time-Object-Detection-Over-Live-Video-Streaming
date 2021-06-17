
from imutils.video import VideoStream
import imutils
import cv2,os,urllib.request
import numpy as np
from django.conf import settings
import datetime
import time
import json
import jsonpickle
from json import JSONEncoder
from PIL import Image

face_detection_videocam = cv2.CascadeClassifier(os.path.join(
			settings.BASE_DIR,'opencv_haarcascade_data/haarcascade_frontalface_default.xml'))
face_detection_webcam = cv2.CascadeClassifier(os.path.join(
			settings.BASE_DIR,'opencv_haarcascade_data/haarcascade_frontalface_default.xml'))
# load our serialized face detector model from disk
prototxtPath = os.path.sep.join([settings.BASE_DIR, "face_detector/deploy.prototxt"])
weightsPath = os.path.sep.join([settings.BASE_DIR,"face_detector/res10_300x300_ssd_iter_140000.caffemodel"])
faceNet = cv2.dnn.readNet(prototxtPath, weightsPath)

video = cv2.VideoCapture(0)

class VideoCamera(object):
	def __init__(self):
		self.video = video


	def get_frame(self):
		success, image = self.video.read()
		# We are using Motion JPEG, but OpenCV defaults to capture raw images,
		# so we must encode it into JPEG in order to correctly display the
		# video stream.

		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		faces_detected = face_detection_videocam.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
		k = 0
		for (x, y, w, h) in faces_detected:
			cv2.rectangle(image, pt1=(x, y), pt2=(x + w, y + h), color=(255, 0, 0), thickness=2)
			k = k+1
			cv2.putText(image, 'face num' + str(k), (x-10, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
		frame_flip = cv2.flip(image,1)
		ret, jpeg1 = cv2.imencode('.jpg', image)
		ret, jpeg = cv2.imencode('.jpg', image)
		d = dict()
		d['og'] = jpeg1.tobytes()
		d['new'] = jpeg.tobytes()
		return jpeg.tobytes()

class OgCameraVideo(object):
	def __init__(self):
		self.video = video


	def get_frame(self):
		success, image = self.video.read()
	
		# We are using Motion JPEG, but OpenCV defaults to capture raw images,
		# so we must encode it into JPEG in order to correctly display the
		# video stream.

		ret, jpeg1 = cv2.imencode('.jpg', image)

		return jpeg1.tobytes()




class VideoCameravariables(object):
	def __init__(self):
		self.video = video
		self.urll = "https://i.ibb.co/8dNHJc9/Plain-White-Wallpaper.png"

	def get_frame(self):
		success, imagek = self.video.read()
		# We are using Motion JPEG, but OpenCV defaults to capture raw images,
		# so we must encode it into JPEG in order to correctly display the
		# video stream.
		imgResp1 = urllib.request.urlopen(self.urll)
		imgNp1 = np.array(bytearray(imgResp1.read()),dtype=np.uint8)
		imgnew= cv2.imdecode(imgNp1,-1)
		gray = cv2.cvtColor(imagek, cv2.COLOR_BGR2GRAY)
		faces_detected = face_detection_videocam.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
		k = 0
		for (x, y, w, h) in faces_detected:
			k = k+1
		cv2.putText(imgnew, str(k), (6, 28),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
		frame_flip = cv2.flip(imgnew,1)
		ret, jpeg = cv2.imencode('.jpg', imgnew)
		return jpeg.tobytes()


class IPWebCam(object):
	def __init__(self):

		self.url = "http://192.168.0.32:8080/shot.jpg"

	def __del__(self):
		cv2.destroyAllWindows()

	def get_frame(self):
		imgResp = urllib.request.urlopen(self.url)
		imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)
		img= cv2.imdecode(imgNp,-1)
		# We are using Motion JPEG, but OpenCV defaults to capture raw images,
		# so we must encode it into JPEG in order to correctly display the
		# video stream
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		faces_detected = face_detection_webcam.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
		k = 0
		for (x, y, w, h) in faces_detected:
			cv2.rectangle(img, pt1=(x, y), pt2=(x + w, y + h), color=(255, 0, 0), thickness=2)
			k = k+1
			cv2.putText(img, 'face num' + str(k), (x-10, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
		resize = cv2.resize(img, (640, 480), interpolation = cv2.INTER_LINEAR) 
		frame_flip = cv2.flip(resize,1)
		ret, jpeg = cv2.imencode('.jpg', frame_flip)
		return jpeg.tobytes()

class OgCameraPhone(object):
	def __init__(self):
		self.urlk ="http://192.168.0.32:8080/shot.jpg"


	def get_frame(self):
		imgResp = urllib.request.urlopen(self.urlk)
		imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)
		img= cv2.imdecode(imgNp,-1)
		# We are using Motion JPEG, but OpenCV defaults to capture raw images,
		# so we must encode it into JPEG in order to correctly display the
		# video stream.

	
		ret, jpeg1 = cv2.imencode('.jpg', img)
	

		return jpeg1.tobytes()

class VideoCameraPhonevariables(object):
	def __init__(self):
		self.urlo ="http://192.168.0.32:8080/shot.jpg"
		self.urlp = "https://i.ibb.co/8dNHJc9/Plain-White-Wallpaper.png"

	def get_frame(self):

		# We are using Motion JPEG, but OpenCV defaults to capture raw images,
		# so we must encode it into JPEG in order to correctly display the
		# video stream.
		imgResp3 = urllib.request.urlopen(self.urlo)
		imgNp3 = np.array(bytearray(imgResp3.read()),dtype=np.uint8)
		imgnew2= cv2.imdecode(imgNp3,-1)
		imgResp2 = urllib.request.urlopen(self.urlp)
		imgNp2 = np.array(bytearray(imgResp2.read()),dtype=np.uint8)
		imgnew1= cv2.imdecode(imgNp2,-1)
		gray = cv2.cvtColor(imgnew2, cv2.COLOR_BGR2GRAY)
		faces_detected = face_detection_videocam.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
		k = 0
		for (x, y, w, h) in faces_detected:
			k = k+1
		cv2.putText(imgnew1, str(k), (6, 28),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
		frame_flip = cv2.flip(imgnew1,1)
		ret, jpeg = cv2.imencode('.jpg', imgnew1)
		return jpeg.tobytes()
