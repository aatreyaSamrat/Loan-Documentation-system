from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
     path('add_loan/', views.add_loan, name='add_loan'),
    path('view_loans/', views.view_loans, name='view_loans'),
    path('<int:pk>/edit/', views.loan_edit, name='loan_edit'),
    path('customers/', views.view_customers, name='view_customers'),
    path('customers/add/', views.add_customer, name='add_customer'),
    path('home/', views.home, name='home'),
]
