from django.db import models
from django.shortcuts import reverse


# Create your models here.
class StudentModel(models.Model):
    name = models.CharField(max_length=150)
    roll = models.IntegerField(unique=True)
    status = models.CharField(max_length=10, default='Inactive')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('student-edit', kwargs={'pk': self.pk})
