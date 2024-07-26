from django import forms
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import MyModel


class CollectFPrint(forms.Form):
  finger_img = forms.ImageField()
  # file_data = {'img': SimpleUploadedFile('test.png', <file data>)}
  # form = ImageForm({}, file_data)


class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['image']
