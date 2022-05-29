from django.db import models
import datetime as dt
import pyperclip
# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='photo/',null=True)
    image_name=models.CharField(max_length=20)
    image_description=models.TextField()
    image_location=models.ForeignKey('Location',on_delete=models.DO_NOTHING,null=True)
    image_category=models.ForeignKey('Category',on_delete=models.DO_NOTHING,null=True)
    published=models.DateTimeField(auto_now_add=True)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        self.save()

    @classmethod
    def get_image_by_id(cls,id):
        image=cls.objects.get(id=id)
        return image

    @classmethod
    def search_image(cls,category):
        image=cls.objects.filter(category__icontains=category) 
        return image

    @classmethod
    def copy_image(cls,id):
        image=cls.objects.get(id=id)
        pyperclip.copy(image.image)

    def __str__(self):
        return self.image_name

class Location(models.Model):
    place= models.CharField(max_length=30,null=True)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        self.save()

    def __str__(self):
        return self.place

class Category(models.Model):
    category=models.CharField(max_length=20,null=True)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        self.save()

    def __str__(self):
        return self.category