from django.db import models

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=254)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")