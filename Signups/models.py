from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class SignupsManager(BaseUserManager):
    def create_user(self, username, useremail, userimage, password):
        user = self.model(
            username = username,
            useremail = useremail,
            userimage = userimage,
            password = password
        )
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, username, useremail, userimage, password):
        user = self.create_user(
            username = username,
            useremail = useremail,
            userimage = userimage,
            password = password
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True

        user.save(using = self._db)
        return user

class Signups(AbstractBaseUser):
    username = models.CharField(max_length=200, null=True)
    useremail = models.EmailField(max_length=300, unique=True)
    userimage = models.ImageField(upload_to = 'uploads/',null=True)
    password = models.CharField(max_length=300)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "useremail"
    REQUIRED_FIELDS = ['username','userimage', 'password']
    objects = SignupsManager()
    class Meta:
        db_table = "Signups"

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj = None):
        return True

    def has_module_perms(self, app_label):
        return True