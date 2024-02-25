from django.db import models

# Create your models 
class RfidTags(models.Model):
    tag_no = models.CharField(max_length = 40, unique = True)
    pupil_name = models.CharField(max_length = 30, default = 'john')

    def __str__(self):
        return self.tag_no