from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Extend if needed, e.g., is_admin, is_support
    is_support = models.BooleanField(default=False)

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Competition(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    prize = models.CharField(max_length=200, blank=True)
    registrations_count = models.IntegerField(default=0)  # For "Most Registered" view
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'competition')
