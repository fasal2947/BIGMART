from django.db import models

# Create your models here.
class addadmindb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    User = models.CharField(max_length=100, null=True, blank=True)
    Password = models.CharField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to="profile", null=True, blank=True)

class addcategorydb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Description = models.CharField(max_length=500, null=True, blank=True)
    Image = models.ImageField(upload_to="profile", null=True, blank=True)

class producpagedb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Prize = models.IntegerField(null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to="profile", null=True, blank=True)
    Category = models.CharField(max_length=100, null=True, blank=True)




class admincontactdb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Subject = models.CharField(max_length=100, null=True, blank=True)
    Message = models.CharField(max_length=100, null=True, blank=True)
