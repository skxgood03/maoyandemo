from django.db import models

class Movies(models.Model):
    name = models.CharField(max_length=100,null=False)
    Starring = models.CharField(max_length=100,null=False)
    imgs = models.CharField(max_length=100,null=False)
    a = models.CharField(max_length=100,null=False)
    class Meta:
        db_table = 'movies'

    def __str__(self):
        return u"Movies:%s" % self.name
