from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    # account_number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact_number = models.CharField(max_length=15)

class Loan(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    loan_type = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.CharField(max_length=20, default='Pending')
    relationship_manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='managed_loans')
