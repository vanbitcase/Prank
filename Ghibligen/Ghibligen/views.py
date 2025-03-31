from django.http import HttpResponse
from django.shortcuts import render,redirect
import time
from django.core.files.storage import default_storage

def ghibli(request):
    return render(request,'gen.html')

def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        file_path = default_storage.save('generated_image.jpg', image)
        
        time.sleep(5)  # Simulate processing delay

        return redirect('view_image')  # Redirect to view image page

    return render(request, 'gen.html')

def view_image(request):
    return render(request, 'view_image.html', {'image_url': '/media/generated_image.jpg'})

