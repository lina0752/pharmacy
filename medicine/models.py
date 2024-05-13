from django.contrib.auth.models import User
from django.db import models

class Medicine(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    submitter = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ("can_delete", "Can delete!!!!"),
        ]
    def __str__(self):
        return self.title