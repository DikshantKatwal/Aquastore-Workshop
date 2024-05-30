import os
from django.db import models
from django_softdelete.models import SoftDeleteModel
from django.conf import settings
# Create your models here.

class Fish(SoftDeleteModel, models.Model):
    created_by = models.IntegerField(null=True)
    updated_by = models.IntegerField(null=True)
    deleted_by = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    image = models.FileField(max_length=255, blank=True, null=True, upload_to='fish/')
    def save(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        if user:
            if not self.pk:  # If the object is being created
                self.created_by = user.id
            else:
                self.updated_by = user.id
                old_icon = Fish.objects.get(pk=self.pk).image
                if old_icon and old_icon != self.image:
                    old_icon_path = os.path.join(settings.MEDIA_ROOT, str(old_icon))
                    if os.path.isfile(old_icon_path):
                        os.remove(old_icon_path)
        super(Fish, self).save(*args, **kwargs)

    class Meta:
        db_table = "db_fish"