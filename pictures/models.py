from django.db import models
import datetime as dt

class Image(models.Model):
    image = models.ImageField(upload_to = 'pictures/')
    image_name = models.CharField(max_length =30)
    image_description = models.TextField()
    image_location = models.ForeignKey(
        'Location',
        on_delete=models.CASCADE,
        )
    image_category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        )

    def __str__(self):
        return self.image

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
    
     @classmethod
    def update_image(cls, id ,name, description , image_location, image_category):
        update = cls.objects.filter(id = id).update(name = name, description = description ,image_location = image_location,image_category = image_category)

    @classmethod
    def get_image_by_id(id):
        image = cls.objects.filter(id=id)
        return image

    @classmethod
    def search_image(category):
        pictures = cls.objects.filter(image_category=category)
        return pictures

    @classmethod
    def filter_by_location(location):
        pictures = cls.objects.filter(image_location=location)
        return pictures

    

    class Meta:
        ordering = ['image_name']
