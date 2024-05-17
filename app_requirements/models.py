from django.db import models


class Requirements(models.Model):
    req_name_uzb = models.CharField(max_length=100)
    req_name_rus = models.CharField(max_length=100)
    req_name_eng = models.CharField(max_length=100)
    req_description_uzb = models.TextField()
    req_description_rus = models.TextField()
    req_description_eng = models.TextField()

    def __str__(self):
        return f"{self.req_name_uzb} + {self.req_description_uzb}"

    class Meta:
        db_table = 'requirements'
        verbose_name = 'Requirements'
        verbose_name_plural = 'Requirements'
