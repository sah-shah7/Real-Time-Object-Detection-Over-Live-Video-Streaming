from django.urls import path, include
from streamapp import views


urlpatterns = [
    path('', views.index, name='index'),
    path('og_feed_video', views.OgCamera_video, name='og_feed_video'),
    path('variable_feed', views.index_data, name='variable_feed'),
    path('video_feed', views.video_feed, name='video_feed'),
    path('og_feed_phone', views.OgCamera_Phone, name='og_feed_phone'),
    path('webcam_feed', views.webcam_feed, name='webcam_feed'),
    path('get/index', views.checkNickName, name = "get_index"),
    path('variable_feed_phone', views.index_data_phone, name='variable_feed_phone'),
    ]
