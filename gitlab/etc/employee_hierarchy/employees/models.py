from django.contrib.auth.models import User
from django.db import models

class Employee(models.Model):
    # Связь OneToOneField с моделью User
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=100)
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='employee_photos/', null=True, blank=True)

    def __str__(self):
        return self.full_name