from django.db import models
from django.utils import timezone

# Extend the built-in User model if you need custom fields, or use the default User model
class CustomUser(models.Model):
    # You can add custom fields here if necessary
    email = models.EmailField(unique=True)  # Ensures that email is unique
    password = models.CharField(max_length=128)  # Password field (though using Django's default User model is sufficient for most use cases)
    created_at = models.DateTimeField(default=timezone.now)  # Account creation timestamp
    updated_at = models.DateTimeField(auto_now=True)  # Updated at timestamp


class GoogleAuth(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    google_id = models.CharField(max_length=255, unique=True)  # Unique identifier for Google sign-in
    access_token = models.CharField(max_length=255)  # Google OAuth2 access token

    def __str__(self):
        return f"GoogleAuth for {self.user.username}"

    def save(self, *args, **kwargs):
        # Optionally, you can handle token expiration or refresh logic here
        super().save(*args, **kwargs)
