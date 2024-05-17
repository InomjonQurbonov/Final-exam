from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    organization = models.CharField(max_length=100, blank=True)
    scientific_degree = models.CharField(max_length=100, blank=True)
    another_information = models.TextField(blank=True)

    def __str__(self):
        return self.user.email

    class Meta:
        ordering = ['user']
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        db_table = 'profile'


class PasswordResets(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reset_code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'password_resets'
        unique_together = (('user', 'created_at'),)
        index_together = (('user', 'created_at'),)
        verbose_name = 'Password Reset'
        verbose_name_plural = 'Password Resets'


class ContactUs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    message = models.TextField(blank=True)
    address = models.CharField(max_length=250, blank=True)
    phone = models.CharField(max_length=250, blank=True)
    admin_email = models.EmailField(max_length=250, blank=True)

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = 'contact_us'
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us'
