from django.contrib.auth.models import AbstractUser, Group
from django.db import models


class User(AbstractUser):
    ROLES = [('MANAGEMENT', 'Gestion'),
             ('SUPPORT', 'Support'),
             ('COMMERCIAL', 'Vente')
            ]
    role = models.CharField(max_length=20, choices=ROLES, blank=True)

    def save(self, *args, **kwargs):
        if self.role == 'MANAGEMENT':
            self.is_staff = True
            management_group = Group.objects.get(name='Management')  # Get the Management group
            self.groups.add(management_group)
        super(User, self).save(*args, **kwargs)
