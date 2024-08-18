from django.db import migrations
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

def create_user_groups(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')

    # Create Groups
    rm_group, created = Group.objects.get_or_create(name='Relationship Manager')
    bm_group, created = Group.objects.get_or_create(name='Branch Manager')
    gm_group, created = Group.objects.get_or_create(name='General Manager')

    # Define permissions
    permissions = {
        'Relationship Manager': [
            'add_customer',  'view_customers',
            'add_loan', 'change_loan', 'view_loan'
        ],
        'Branch Manager': [
            'view_customer', 'view_loan', 'change_loan'
        ],
        'General Manager': [
            'view_customer', 'view_loan', 'change_loan'
        ],
    }

    # Get the content types for the Customer and Loan models
    customer_content_type = ContentType.objects.get(app_label='loans', model='customer')
    loan_content_type = ContentType.objects.get(app_label='loans', model='loan')

    # Assign permissions to groups
    for group_name, perms in permissions.items():
        group = Group.objects.get(name=group_name)
        for perm in perms:
            # Find the permission object
            if 'customer' in perm:
                permission = Permission.objects.get(codename=perm, content_type=customer_content_type)
            elif 'loan' in perm:
                permission = Permission.objects.get(codename=perm, content_type=loan_content_type)
            else:
                continue
            group.permissions.add(permission)

def remove_user_groups(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Group.objects.filter(name__in=['Relationship Manager', 'Branch Manager', 'General Manager']).delete()

class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0001_initial'),  # replace with your initial migration if different
    ]

    operations = [
        migrations.RunPython(create_user_groups, remove_user_groups),
    ]
