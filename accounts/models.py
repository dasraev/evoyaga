from django.db import models
from django.contrib.auth.models import Group
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext as _
from info.models import Markaz, MarkazTuman


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, username, first_name, password, login, **other_fields):
        if not email:
            raise ValueError('User must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, first_name=first_name, login=login)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save()

        return user

    def create_user(self, email, password, **other_fields):
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_staff', True)

        if not email:
            raise ValueError(_('You must provide an email address'))
        username = email

            
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **other_fields)
        user.set_password(password)
        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    login = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=200, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    father_name = models.CharField(max_length=150, blank=True)
    photo = models.ImageField(upload_to="users/", blank=True, null=True, max_length=None)
    birth_date = models.DateField(null=True)
    markaz = models.ForeignKey(
        Markaz, on_delete=models.CASCADE, null=True, blank=True, related_name="markaz")
    markaz_tuman = models.ForeignKey(
        MarkazTuman, on_delete=models.CASCADE, null=True, blank=True, related_name="markaz_tuman")

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    
    objects = CustomAccountManager()

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['username', 'first_name', 'email']
    def save(self, *args, **kwargs):
        print('admin', kwargs,args)
        try:
            if kwargs['password']:
                self.set_password(kwargs['password'])
        except Exception:
            pass
        finally:
            super(CustomUser, self).save(*args, **kwargs)
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.father_name}"

    class Meta:
        db_table = 'user'


Group.add_to_class('code', models.PositiveSmallIntegerField(null=True, blank=True))
