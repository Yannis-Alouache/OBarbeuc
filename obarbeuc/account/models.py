from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.


class MyAccountManager(BaseUserManager):
    def create_user(self, email, last_name, first_name, phone, password=None):
        if not email:
            raise ValueError("Veuillez entrez un mail")
        if not first_name:
            raise ValueError("Veuillez entrez un prénom")
        if not last_name:
            raise ValueError("Veuillez entrez un nom de famille")
        
        user = self.model(
            email = self.normalize_email(email),
            last_name = last_name,
            first_name = first_name,
            phone = phone
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, last_name, first_name, phone, password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            last_name = last_name,
            first_name = first_name,
            phone = phone,
            password = password
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=255, unique=True, error_messages={'unique':'Un compte existe déjà avec cette email'})
    last_name = models.CharField(max_length=50, blank=False, null=False)
    first_name = models.CharField(max_length=50, blank=False, null=False)
    phone = models.CharField(max_length=10, blank=False, null=False, default=None)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['last_name', 'first_name', 'phone']

    objects = MyAccountManager()

    def __str__(self):
        return self.last_name + " " + self.first_name

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True

