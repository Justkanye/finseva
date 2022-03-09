from django.db import models
from django.contrib.auth.models import User, AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(_('email address'), unique=True)
    has_verified_email = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

STATE_CHOICES = (
		("Andhra Pradesh", "Andhra Pradesh"),
		("Andaman and Nicobar (UT)", "Andaman and Nicobar (UT)"),
		("Arunachal Pradesh", "Arunachal Pradesh"),
		("Assam", "Assam"),
		("Bihar", "Bihar"),
		("Chandigarh (UT)", "Chandigarh (UT)"),
		("Chhattisgarh", "Chhattisgarh"),
		("Dadra and Nagar Haveli (UT)", "Dadra and Nagar Haveli (UT)"),
		("Daman and Diu (UT)", "Daman and Diu (UT)"),
		("Delhi", "Delhi"),
		("Goa", "Goa"),
		("Gujarat", "Gujarat"),
		("Haryana", "Haryana"),
		("Himachal Pradesh", "Himachal Pradesh"),
		("Jammu and Kashmir", "Jammu and Kashmir"),
		("Jharkhand", "Jharkhand"),
		("Karnataka", "Karnataka"),
		("Kerala", "Kerala"),
		("Lakshadweep (UT)", "Lakshadweep (UT)"),
		("Madhya Pradesh", "Madhya Pradesh"),
		("Maharashtra", "Maharashtra"),
		("Manipur", "Manipur"),
		("Meghalaya", "Meghalaya"),
		("Mizoram", "Mizoram"),
		("Nagaland", "Nagaland"),
		("Orissa", "Orissa"),
		("Puducherry (UT)", "Puducherry (UT)"),
		("Punjab", "Punjab"),
		("Rajasthan", "Rajasthan"),
		("Sikkim", "Sikkim"),
		("Tamil Nadu", "Tamil Nadu"),
		("Telangana", "Telangana"),
		("Tripura", "Tripura"),
		("Uttar Pradesh", "Uttar Pradesh"),
		("Uttarakhand", "Uttarakhand"),
		("West Bengal", "West Bengal"),
	)

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	business_name = models.CharField(max_length=220)
	mobile_number = models.CharField(max_length=220)
	shop_address = models.CharField(max_length=220)
	state = models.CharField(choices=STATE_CHOICES, max_length=220)
	pin_code = models.BigIntegerField()
	district = models.CharField(max_length=220)
	

	def __str__(self):
		return f'Profile for {self.user.email}'
