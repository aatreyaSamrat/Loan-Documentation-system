from django import forms
from .models import Customer, Loan

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [ 'name', 'address', 'contact_number']

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['customer', 'loan_type', 'amount', 'status', 'relationship_manager']
