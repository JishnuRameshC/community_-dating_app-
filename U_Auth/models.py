from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    country_code = models.CharField(max_length=3)

    def __str__(self):
        return f'{self.name} - ({self.country_code})'
    

class User(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    SMOKE = (
        ('N','No'),
        ('Y','Yes'),
        ('P','Plan to Quit')
    )
    REL_STATAS = (
        ('S','Single'),
        ('M','Married'),
        ('W','Widow'),
        ('D','Divorced'),
    )
    DRINKING = (
        ('T','Yes'),
        ('F','No'),
        ('P','Plan to Quit'),
    )
    phone = models.CharField(max_length=15, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    smoke = models.CharField(max_length=1,choices=SMOKE,default='N')
    drinking = models.CharField(max_length=1,choices=DRINKING,default='T')
    rel_status = models.CharField(max_length=1, choices=REL_STATAS,default='S')
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def __str__(self) -> str:
        return self.username
    
    
class ProfilePic(models.Model):
    id = models.BigAutoField(primary_key=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Address(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address_line_1 = models.CharField(max_length=250)
    address_line_2 = models.CharField(max_length=250)
    address_line_3 = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=6)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    is_default = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user', 'name']

    def __str__(self) -> str:
        return f'''
            {self.address_line_1}
            {self.address_line_2}
            {self.address_line_3}
            {self.city}
            {self.state}
            {self.country}
        '''
    

class EmployeeEmployer(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - {self.company_name}"


class JobSeeker(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    job_field = models.CharField(max_length=100)
    experience = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.job_field}"