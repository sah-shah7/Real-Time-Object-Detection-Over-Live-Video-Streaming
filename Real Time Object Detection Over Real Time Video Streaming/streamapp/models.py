from django.db import models

# Create your models here.
# Create your models here.
class Index(models.Model):
    # NICK NAME should be unique
    objects_detected = models.CharField(max_length=100)
    latency = models.CharField(max_length=100)
    fps = models.CharField(max_length=100)
    accuracy = models.CharField(max_length = 100)


    def __str__(self):
        return self.Index