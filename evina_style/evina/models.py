from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=30)
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Image(models.Model):
    title = models.CharField(max_length=50)
    image = models.FileField(upload_to='images/gallery')
    image_min = models.FileField(upload_to='images/gallery')
    alt = models.CharField(max_length=100)

    def __str__(self):
        return self.title


# class Contact(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)
#     phone = models.CharField(max_length=20)
#     message = models.TextField(max_length=300)
#
#     def __str__(self):
#         return self.email
