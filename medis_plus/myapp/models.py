from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', default="")

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class DoctorDetail(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', default="")
    days = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    available = models.CharField(max_length=200)
    degree = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.name


class Appointment(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    doctor = models.CharField(max_length=200)
    date = models.DateField(null=True)

    def __str__(self):
        return f"{self.name} - {self.email}"


class Contacts(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    phone = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} - {self.email}"
