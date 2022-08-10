from django.db import models

from apps.users.models import CustomUser


class Phone(models.Model):
    CD = 'consideration'
    IN_PROGRESS = 'in_progress'
    DONE = 'done'

    status_choices = [
        (CD, 'consideration',),
        (IN_PROGRESS, 'in progress',),
        (DONE, 'done',),
    ]
    brand = models.CharField(max_length=255)
    problem = models.TextField()
    status = models.CharField(max_length=255, choices=status_choices, blank=True, null=True)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.brand


class Invoice(models.Model):
    description = models.CharField(max_length=255)
    price = models.FloatField()
    phone_id = models.ForeignKey(Phone, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.description
