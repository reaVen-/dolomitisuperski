from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.conf import settings
from django.core.urlresolvers import reverse
from upload.models import Image

def handle_uploaded_file(f):
    with open(settings.MEDIA_ROOT+"images/"+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def index(request):
    if request.method=="POST":
        images = request.FILES.getlist('file_field')
        for image in images:
            handle_uploaded_file(image)
            try:
                Image(filename=image.name).save()
            except:
                pass

    total = len(Image.objects.all())
    return render(request,'upload/index.html',{'total':total})



