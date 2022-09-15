from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)


class Post(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    header1 = models.CharField(max_length=100)
    image1 = models.FileField(upload_to='static/images/gallery', blank=True)
    text1 = models.TextField()
    header2 = models.CharField(max_length=100, blank=True)
    image2 = models.FileField(upload_to='static/images/gallery', blank=True)
    text2 = models.TextField(blank=True)
    header3 = models.CharField(max_length=100, blank=True)
    image3 = models.FileField(upload_to='static/images/gallery', blank=True)
    text3 = models.TextField(blank=True)
    header4 = models.CharField(max_length=100, blank=True)
    image4 = models.FileField(upload_to='static/images/gallery', blank=True)
    text4 = models.TextField(blank=True)
    header5 = models.CharField(max_length=100, blank=True)
    image5 = models.FileField(upload_to='static/images/gallery', blank=True)
    text5 = models.TextField(blank=True)
    header6 = models.CharField(max_length=100, blank=True)
    text6 = models.TextField(blank=True)
    header7 = models.CharField(max_length=100, blank=True)
    text7 = models.TextField(blank=True)
    header8 = models.CharField(max_length=100, blank=True)
    text8 = models.TextField(blank=True)
    header9 = models.CharField(max_length=100, blank=True)
    text9 = models.TextField(blank=True)
    header10 = models.CharField(max_length=100, blank=True)
    text10 = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.author
