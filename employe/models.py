from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Employe(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    contact=models.CharField(max_length=100,null=True)
    dob=models.DateField(null=True)
    Ecode=models.IntegerField(unique=True)
    dig=models.CharField(max_length=100,null=True)
    img=models.ImageField(upload_to='profile',default='employe/static/image/apng.avif')
    dept=models.CharField(max_length=100,null=True)
    gender=models.CharField(max_length=100,null=True)
    join_data=models.DateField(null=True)

    def __str__(self):
        u=self.user.first_name+'-'+self.user.last_name
        return u
    

class Emp_Edu(models.Model):
   
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.TextField()
    
    first_edu=models.CharField(max_length=100,null=True)
    first_p_year=models.CharField(max_length=100,null=True)
    first_col=models.CharField(max_length=100,null=True)

    sec_edu=models.CharField(max_length=100,null=True)
    sec_p_year=models.CharField(max_length=100,null=True)
    sec_col=models.CharField(max_length=100,null=True)

    thrd_edu=models.CharField(max_length=100,null=True)
    thrd_p_year=models.CharField(max_length=100,null=True)
    thrd_col=models.CharField(max_length=100,null=True)

    four_edu=models.CharField(max_length=100,null=True)
    four_p_year=models.CharField(max_length=100,null=True)
    four_col=models.CharField(max_length=100,null=True)
    def __str__(self):
        u=self.user.first_name+'-'+self.user.last_name
        return u


class Emp_Exp(models.Model):
   
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    fresher=models.BooleanField(default=False)

    job_title1=models.CharField(max_length=100,null=True)
    company1=models.CharField(max_length=100,null=True)
    years1=models.CharField(max_length=100,null=True)

    job_title2=models.CharField(max_length=100,null=True)
    company2=models.CharField(max_length=100,null=True)
    years2=models.CharField(max_length=100,null=True)
    
    job_title3=models.CharField(max_length=100,null=True)
    company3=models.CharField(max_length=100,null=True)
    years3=models.CharField(max_length=100,null=True)
    def __str__(self):
        u=self.user.first_name+'-'+self.user.last_name
        return u


class Leave_user(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    aprov=models.BooleanField(default=False)
    reject=models.BooleanField(default=False)
    lstartdate=models.DateField(null=True)
    lenddate=models.DateField(null=True)
    ltype=models.CharField(max_length=100,null=True)
    purpos=models.CharField(max_length=100,null=True)

    def __str__(self):
        u=self.user.first_name+'-'+self.user.last_name
        return u


    



    
