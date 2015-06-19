from django.db import models

from ckeditor.fields import RichTextField
from image_cropping import ImageRatioField

class Section(models.Model):
    name = models.CharField(max_length = 100)
    parent_section = models.ForeignKey('self', null = True, blank = True)
    def __str__(self):
        return self.name

class Invitation(models.Model):
    name = models.CharField(max_length = 100)
    image = models.ImageField(upload_to="user_uploads")
    cropping = ImageRatioField('image', '430x200')
    def __str__(self):
        return self.name

# class SubSection(models.Model):
#     name = models.CharField(max_length = 100)
#     section = models.ForeignKey(Section)
#     def __str__(self):
#         return self.name

class News(models.Model):
    name = models.CharField(max_length = 100)
    section = models.ForeignKey(Section)
    def __str__(self):
        return self.name

class StaticArticle(models.Model):
    name = models.CharField(max_length = 100)
    text = RichTextField()
    section = models.ForeignKey(Section)
    def __str__(self):
        return self.name

class Article(models.Model):
    name = models.CharField(max_length = 100)
    text = RichTextField()
    news = models.ForeignKey(News)
    def __str__(self):
        return self.name

class File(models.Model):
    name = models.CharField(max_length = 255)
    soubor = models.FileField(upload_to="user_uploads")
    def __str__(self):
        return self.name




