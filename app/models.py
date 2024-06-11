from django.db import models

class Data (models.Model):
    name=models.CharField(max_length=100)
    address=models.TextField(max_length=500)
    def __str__(self):
        return self.name