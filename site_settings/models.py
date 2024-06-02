from django.db import models
from django.db import connection

class SiteSetting(models.Model):
    key = models.CharField(max_length=50, null=True, blank=True)
    value = models.TextField(null=True, blank=True)
    class Meta:
        db_table = "site_settings"

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE {format(cls._meta.db_table)};')
