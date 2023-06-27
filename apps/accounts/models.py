from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class AccountManager(BaseUserManager):
    def create_user(self, phone, password=None, **kwargs):
        if phone is None:
            raise TypeError({"success": False, "detail": _("User should have a phone")})
        user = self.model(phone=phone, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **kwargs):
        user = self.create_user(phone=phone, password=password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.role = 0
        user.save(using=self._db)
        return user


def avatar_path(instance, filename):
    phone = instance.phone
    return 'avatars/{0}/{1}'.format(phone, filename)


class Account(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = _('Account')
        verbose_name_plural = _('Accounts')

    phone = models.CharField(max_length=12, verbose_name=_('Phone number'), unique=True, db_index=True)
    first_name = models.CharField(max_length=50, verbose_name=_('First name'), null=True)
    last_name = models.CharField(max_length=50, verbose_name=_('Last name'), null=True)
    birth_date = models.DateField(null=True, verbose_name=_('Birth data'))
    avatar = models.ImageField(upload_to=avatar_path, null=True, blank=True)
    is_superuser = models.BooleanField(default=False, verbose_name=_('Super user'))
    is_staff = models.BooleanField(default=False, verbose_name=_('Staff user'))
    is_active = models.BooleanField(default=True, verbose_name=_('Active user'))
    is_verified = models.BooleanField(default=False, verbose_name=_('Verified user'))
    modified_date = models.DateTimeField(auto_now=True, verbose_name=_('Modified date'))
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Created date'))

    objects = AccountManager()

    EMAIL_FIELD = ''
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone

    @property
    def full_name(self):
        name_list = []
        if self.last_name:
            name_list.append(self.last_name)
        if self.first_name:
            name_list.append(self.first_name)
        if name_list:
            return " ".join(name_list)
        return "-"


class Position(models.Model):
    name = models.CharField(max_length=221, blank=True)

    def __str__(self):
        return self.name


class Consultant(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, blank=True, related_name='consultants')
    bio = models.TextField()
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.full_name


