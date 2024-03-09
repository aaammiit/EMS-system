from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
class Employe_attendence(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    present=models.BooleanField(default=False)
    absent=models.BooleanField(default=False)
    date_time=models.DateTimeField(auto_now=True)

    def __str__(self):
        u=self.user.first_name+'-'+self.user.last_name
        return u