from django.contrib.auth import get_user_model
from django.db import models
from ckeditor.fields import RichTextField
from app_journals.models import Journal

User = get_user_model()


class Papers(models.Model):
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    paper_title_uz = models.CharField(max_length=250)
    paper_title_ru = models.CharField(max_length=250)
    paper_title_en = models.CharField(max_length=250)
    paper_description_uz = RichTextField(blank=True, null=True)
    paper_description_ru = RichTextField(blank=True, null=True)
    paper_description_en = RichTextField(blank=True, null=True)
    paper_date = models.DateField(auto_now_add=True)
    paper_views = models.IntegerField(default=0)
    paper_content_uz = RichTextField(blank=True, null=True)
    paper_content_ru = RichTextField(blank=True, null=True)
    paper_content_en = RichTextField(blank=True, null=True)
    paper_tegs = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return f"{self.paper_title_uz} + {self.paper_description_uz}"

    class Meta:
        db_table = 'papers'
        verbose_name = 'Papers'
        verbose_name_plural = 'Papers'


class References(models.Model):
    paper = models.ForeignKey(Papers, on_delete=models.CASCADE)
    url = models.URLField(max_length=250)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.url

    class Meta:
        db_table = 'references'
        verbose_name = 'References'
        verbose_name_plural = 'References'


class Reviews(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    paper = models.ForeignKey(Papers, on_delete=models.CASCADE)
    review_text = RichTextField(blank=True, null=True)
    review_date = models.DateField(auto_now_add=True)
    review_file = models.FileField(upload_to='review_files', blank=True, null=True)

    def __str__(self):
        return self.review_text

    class Meta:
        db_table = 'reviews'
        verbose_name = 'Reviews'
        verbose_name_plural = 'Reviews'
