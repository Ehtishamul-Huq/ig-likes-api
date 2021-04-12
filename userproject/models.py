import uuid
from django.db import models
from user.models import User
from datetime import datetime

# Create your models here.
class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)

class Experience(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    company_name = models.CharField(max_length=100)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)

class Education(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    degree = models.CharField(max_length=100)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
