from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLES = [('MANAGEMENT', 'Gestion'),
             ('SUPPORT', 'Support'),
             ('COMMERCIAL', 'Vente')
            ]
    role = models.CharField(max_length=20, choices=ROLES, blank=True)

    def save(self, *args, **kwargs):
        if self.ROLES == 'MANAGEMENT':
            self.is_admin = True
        return super(User, self).save(*args, **kwargs)
