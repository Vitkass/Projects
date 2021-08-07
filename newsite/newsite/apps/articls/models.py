import datetime
from django.db import models

from django.utils import timezone


class Articl(models.Model):
    
    articl_title = models.CharField('Article name', max_length = 200)
    articl_text = models.TextField('Article text')
    pub_date = models.DateTimeField('Date of Publication')
    
    def __str__(self):
        return self.articl_title
    
    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))

class Comment(models.Model):
    articl = models.ForeignKey(Articl, on_delete = models.CASCADE)
    autor_name = models.CharField('Autor name', max_length = 70)
    comment_text = models.CharField('Comment text', max_length = 200)

    def __str__(self):
        return self.autor_name
