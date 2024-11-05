from django.db import models

class MyModel(models.Model):
  def get_upload_path(instance, filename):
        # This will save the image in a folder named after the blood group
        return f'images/{instance.blood_group}/{filename}'

  image = models.ImageField(upload_to=get_upload_path)
  blood_group = models.CharField(max_length=5, default="")
  sex = models.CharField(max_length=5, default="")
  blood_pressure = models.CharField(max_length=5, default="")
  hormonal_issue = models.CharField(max_length=5, default="")
  bmi = models.FloatField(default=0)


    

# Create your models here.
class Student(models.Model):
  name = models.CharField(max_length=70)
  date_of_birth = models.DateField()
  matric_no = models.CharField(max_length=16)
  fingerprint = models.ImageField(upload_to='finger-print')

  fprint_base64 = models.TextField()
  profile_pic = models.ImageField(upload_to='profile-pic')


  def __str__(self):
    return self.name


class Tracker(models.Model):
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  time_in = models.DateTimeField(blank=True, null=True)
  time_out = models.DateTimeField(blank=True, null=True)
  where = models.CharField(default="FSSE", max_length=4)

  def __str__(self):
    return f"{self.student.name} {self.pk}"