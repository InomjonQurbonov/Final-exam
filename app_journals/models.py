from django.db import models
from ckeditor.fields import RichTextField


class Journal(models.Model):
    journal_title_uz = models.CharField(max_length=250)
    journal_title_ru = models.CharField(max_length=250)
    journal_title_en = models.CharField(max_length=250)
    journal_description_uz = RichTextField(blank=True, null=True)
    journal_description_ru = RichTextField(blank=True, null=True)
    journal_description_en = RichTextField(blank=True, null=True)
    journal_image = models.ImageField(upload_to='journal_images/%Y/%m/%d')
    journal_tegs = models.CharField(max_length=250)
    journal_file = models.FileField(upload_to='journal_files/')

    def __str__(self):
        return self.journal_title_uz

    class Meta:
        db_table = 'journal'
        verbose_name = 'Journal'
        verbose_name_plural = 'Journals'
