from django.db import models

# Create your models here.
class Post(models.Model):
    major = models.CharField(max_length=50)
    post_num = models.IntegerField()
    title = models.CharField(max_length=200)
    url = models.TextField(unique="true")
    pub_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
