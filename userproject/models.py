import uuid
from django.db import models
from user.models import User
from datetime import datetime

# Create your models here.
class Like(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    likes = models.IntegerField(blank=False)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)