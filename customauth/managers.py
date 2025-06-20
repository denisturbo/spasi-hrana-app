from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
        def create_user(self, email, username, user_type, password=None, **extra_fields):
            if not email:
                raise ValueError("моля въвете email")
            email = self.normalize_email(email)
            user = self.model(email=email, username=username, user_type=user_type, **extra_fields)
            user.set_password(password)
            user.save()
            return user

        def create_superuser(self, email, username, user_type='customer', password=None, **extra_fields):
            extra_fields.setdefault('is_staff', True)
            extra_fields.setdefault('is_superuser', True)
            return self.create_user(email, username, user_type, password, **extra_fields)
