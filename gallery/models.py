from django.db import models

class Gallery(models.Model):
    image = models.ImageField()
    description = models.CharField(max_length=500)
    def __str__(self):
        return self.description