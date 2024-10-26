from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse


# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, "about.html")

def contact_view(request):
    return render(request,"contact.html")

def wedding_view(request):
    image_range = range(1, 21)
    return render(request,"wedding2.html", {'image_range': image_range})

def pre_wedding_view(request):
    return render(request,"pre_wedding.html")

def meternity_view(request):
    return render(request,"meternity.html")

def baby_born_view(request):
    return render(request,"baby_born.html")

def baby_photoshoot_view(request):
    return render(request,"baby_photoshoot.html")

def album_view(request):
    return render(request,"album.html")

def youtube_view(request):
    youtube_link = request.GET.get('link', '')
    # Your logic to handle the YouTube link goes here
    return HttpResponse(f"YouTube Link: {youtube_link}")

def video_view(request):
    youtube_links = [
        "https://www.youtube.com/watch?v=pctVE40UTNA",
        # Add more links as needed
    ]

    context = {
        'youtube_links': youtube_links,
    }

    return render(request, 'video.html', context)

# def video_view(request):
#     # return render(request,"video.html")
#     youtube_links = [
#         "https://www.youtube.com/watch?v=pctVE40UTNA",
#         # Add more links as needed
#     ]

#     # Other context data you may have
#     context = {
#         'youtube_links': youtube_links,
#         # Add other context variables as needed
#     }

#     return render(request, 'video.html', context)
# image_range = range(1, 33)  # Adjust the range as needed
# video_paths = [f"Album/videos/video{i}.mp4" for i in image_range]    
# return render(request,"video.html", {'image_range': image_range, 'video_paths': video_paths})

def contact_us(request):
    if request.method == 'POST':
        # Assuming you have a form for the contact us page
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name,email,phone,message)
        
        # Send email
        send_mail(
            'Contact Us Form Submission',
            f'Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}',
            settings.EMAIL_HOST_USER,  # Sender's email
            [settings.YOUR_CONTACT_EMAIL],  # Receiver's email
            fail_silently=False,
        )
        # Redirect or render success page after sending the email
        # Add your logic here
    return render(request, 'contact_us.html')
