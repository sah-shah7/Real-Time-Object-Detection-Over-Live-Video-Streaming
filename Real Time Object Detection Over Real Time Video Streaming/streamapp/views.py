from django.shortcuts import render
from django.http.response import StreamingHttpResponse,HttpResponse
from streamapp.camera import VideoCamera, OgCameraVideo, OgCameraPhone, IPWebCam, VideoCameravariables, VideoCameraPhonevariables
import logging
import datetime
from django.http import JsonResponse
from .models import Index
# Create your views here.


def index(request):
	return render(request, 'home.html')


def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def video_feed(request):
	obj = StreamingHttpResponse(gen(VideoCamera()),
					content_type='multipart/x-mixed-replace; boundary=frame')
	return obj
def OgCamera_video(request):
	obj = StreamingHttpResponse(gen(OgCameraVideo()),
					content_type='multipart/x-mixed-replace; boundary=frame')
	return obj	
def OgCamera_Phone(request):
	obj = StreamingHttpResponse(gen(OgCameraPhone()),
					content_type='multipart/x-mixed-replace; boundary=frame')
	return obj	
def webcam_feed(request):
	return StreamingHttpResponse(gen(IPWebCam()),
					content_type='multipart/x-mixed-replace; boundary=frame')

def index_data(request):
    # here you return whatever data you need updated in your template
	return StreamingHttpResponse(gen(VideoCameravariables()),
					content_type='multipart/x-mixed-replace; boundary=frame')

def index_data_phone(request):
    # here you return whatever data you need updated in your template
	return StreamingHttpResponse(gen(VideoCameraPhonevariables()),
					content_type='multipart/x-mixed-replace; boundary=frame')
def checkNickName(request):
    # request should be ajax and method should be GET.
	if request.is_ajax and request.method == "GET":
        # get the nick name from the client side.
        # check for the nick name in the database.
		if request.is_ajax:
            # if nick_name found return not valid new friend
			return StreamingHttpResponse(gen(VideoCameravariables()),
					content_type='multipart/x-mixed-replace; boundary=frame')
		else:
            # if nick_name not found, then user can creatgen(IPWebCam()e a new friend.
			return JsonResponse({"valid":True}, status = 200)

	return JsonResponse({}, status = 400)


# def variables_feed(request):

# 	now = datetime.datetime.now() 

# 	msg = f'Today is {now}'

    
# 	return render('home.html', {'now':msg})





