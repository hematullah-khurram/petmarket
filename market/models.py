from django.db import models
from django.contrib.auth.models import User

class Pet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pets')
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=50)
    breed = models.CharField(max_length=100, blank=True)
    color = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='pets/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.owner.username})"
