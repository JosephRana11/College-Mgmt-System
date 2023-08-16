from django.db import models
from users.models import CustomUser

class Student(models.Model):
  user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  age = models.IntegerField()
  date_joined = models.DateField(auto_now_add=True)

  def __str__(self):
      return f"{self.first_name}{self.last_name}--{self.user.email}"
  