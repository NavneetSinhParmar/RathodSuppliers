# appname/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about', views.about_view, name='about'),
    path('contact', views.contact_view, name='contact'),
    path('register', views.register_view, name='register'),
    path('do_register', views.do_register, name='do_register'),
    path('contact', views.contact_view, name='contact'),
    # path('pre_wedding', views.pre_wedding_view, name='pre_wedding'),
    # path('meternity', views.meternity_view, name='meternity'),
    # path('baby_born', views.baby_born_view, name='baby_born'),
    # path('baby_photoshoot', views.baby_photoshoot_view, name='baby_photoshoot'),
    # path('album', views.album_view, name='album'),
    # path('video', views.video_view, name='video'),
    # path('contact/', views.contact_us, name='contact_us'),
    # path('youtube/', views.youtube_view, name='youtube_view'),

    # Define other URL patterns here
]
