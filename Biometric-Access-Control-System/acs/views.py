from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from .models import Student, Tracker
from os.path import isfile, join
from PIL import Image
from os import listdir
from io import BytesIO
import random, pytz, base64, imagehash

def base64_to_jpeg(pic):
  """
  Accepts a picture in base64 string, 
  encodes that string,
  converts it to a .jpeg image 
  and saves it on the file system
  """

  # converts the base 64 string to bytes and decodes those bytes
  image_64_decode = base64.decodebytes(pic.encode())   
  # create a writable image 
  image_result = open('media/buffer/fprint_check.jpeg', 'wb') 
  # and write the decoding result
  image_result.write(image_64_decode)
  

def check_similarity(img1_rel_path, img2_rel_path):
  """
  Arguments: 
  img1_rel_path -- the relative path to the location of the first image
  img2_rel_path -- the relative path to the location of the second image

  Accepts two images, compares them,
  and returns the difference between them -> int
  
  """

  hash0 = imagehash.average_hash(Image.open(img1_rel_path)) 
  hash1 = imagehash.average_hash(Image.open(img2_rel_path)) 

  return hash0 - hash1


# Create your views here.
def index(request):
  # img_base64 = request.POST.get('img-base64')
  #       # Process the captured fingerprint data here as needed
  #       # Example: Save to database, perform authentication, etc.
  #       return render(request, 'acs/index.html')
  #   else:
  #       return render(request, 'acs/index.html')
  return render(request, 'acs/index.html')

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import base64
from django.core.files.base import ContentFile
from .models import MyModel
 

# @csrf_exempt
# def auth(request):
#     if request.method == 'POST':
#         base64_fprint = request.POST.get('img_base64')
#         bloodGroup = request.POST.get('bloodGroup')
#         if base64_fprint:
#             # Splitting the base64 string to get the image data
#             _, imgstr = base64_fprint.split(';base64,')
#             img_data = base64.b64decode(imgstr)

#             # Open the image using Pillow
#             img = Image.open(BytesIO(img_data))

#             # Convert the image to PNG format
#             img_io = BytesIO()
#             img.save(img_io, format='PNG')
#             img_io.seek(0)  # Seek to the beginning of the stream

#             # Create a new instance of MyModel and save it to get the ID
#             instance = MyModel()
#             instance.save()

#             # Generate the filename using the instance ID and PNG extension
#             filename = f'{instance.id}.png'

#             # Save the image with the generated filename in PNG format
#             instance.image.save(filename, ContentFile(img_io.getvalue()))
#             instance.save()

#             return HttpResponse("Image saved successfully")

#     else:
#         return HttpResponse("Image isn't saved successfully")

#     return render(request, 'acs/index.html')

@csrf_exempt
def auth(request):
    if request.method == 'POST':
        base64_fprint = request.POST.get('img_base64')
        bloodGroup = request.POST.get('bloodGroup')
        print(bloodGroup)
        if base64_fprint:
            # Splitting the base64 string to get the image data
            _, imgstr = base64_fprint.split(';base64,')
            img_data = base64.b64decode(imgstr)

            # Open the image using Pillow
            img = Image.open(BytesIO(img_data))

            # Convert the image to PNG format
            img_io = BytesIO()
            img.save(img_io, format='PNG')
            img_io.seek(0)  # Seek to the beginning of the stream

            # Create a new instance of MyModel and set the blood group
            instance = MyModel(blood_group=bloodGroup)
            instance.save()

            # Generate the filename using the instance ID and PNG extension
            filename = f'{instance.id}.png'

            # Save the image with the generated filename in the appropriate blood group folder
            instance.image.save(filename, ContentFile(img_io.getvalue()))
            instance.save()


            return HttpResponse("Image saved successfully")

    else:
        return HttpResponse("Image isn't saved successfully")

    return render(request, 'acs/index.html')

    

def develop(request): 
  return render(request, 'acs/develop.html', {
    # 'status':'Error 404: Unrecognised Fingerprint',
  })
