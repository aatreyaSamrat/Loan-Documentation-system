from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from .models import Loan, Customer
from .forms import LoanForm, CustomerForm

@login_required
def home(request):
    return render(request, 'loans/home.html')

@login_required
@permission_required('loans.add_customer', raise_exception=True)
def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_customers')
    else:
        form = CustomerForm()
    return render(request, 'loans/add_customer.html', {'form': form})

@login_required
@permission_required('loans.view_customer', raise_exception=True)
def view_customers(request):
    customers = Customer.objects.all()
    return render(request, 'loans/view_customers.html', {'customers': customers})

@login_required
@permission_required('loans.view_loan', raise_exception=True)
def view_loans(request):
    loans = Loan.objects.all()
   
    return render(request, 'loans/loan_list.html', {'loans': loans})

@login_required
@permission_required('loans.add_loan', raise_exception=True)
def add_loan(request):
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_loans')
    else:
        form = LoanForm()
    return render(request, 'loans/loan_form.html', {'form': form})

@login_required
@permission_required('loans.change_loan', raise_exception=True)
def loan_edit(request, pk):
    loan = get_object_or_404(Loan, pk=pk)
    if request.method == 'POST':
        form = LoanForm(request.POST, instance=loan)
        if form.is_valid():
            form.save() 
            return redirect('view_loans')
    else:
        form = LoanForm(instance=loan)
    return render(request, 'loans/loan_form.html', {'form': form})
