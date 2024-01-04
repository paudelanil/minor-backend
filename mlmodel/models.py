from django.db import models

# Create your models here.
class MlModel(models.Model):
    category = models.TextField(max_length=50)

    def __str__(self):
        return self.category