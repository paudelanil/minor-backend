from django.db import models
import os

# Create your models here.
class Img(models.Model):
    image=models.ImageField(upload_to="imguploader/uploaded/")

    def filename(self):
        return os.path.basename(self.image.name)