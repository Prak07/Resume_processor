from django.db import models

# Create your models here.

class Candidate(models.Model):
    first_name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)

    def __str__(self):
        return self.first_name
