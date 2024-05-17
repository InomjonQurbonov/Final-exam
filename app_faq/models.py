from django.db import models


class Faq(models.Model):
    question_uzb = models.TextField()
    question_rus = models.TextField()
    question_eng = models.TextField()
    answer_uzb = models.TextField()
    answer_rus = models.TextField()
    answer_eng = models.TextField()

    def __str__(self):
        return f"{self.question_uzb} + {self.answer_uzb}"

    class Meta:
        db_table = 'faq'
        verbose_name = 'Faq'
        verbose_name_plural = 'Faqs'
