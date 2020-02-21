from django.db import models
from django.urls import reverse

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
                            'auth.User',
                            on_delete = models.CASCADE,
                            )
    body = models.TextField()


    def __str__(self):
        return self.title
    def get_absolute_url(self):
        # here, revese method is used to redirect the user to the
        #  desired place after the data has been saved to the database
        # return reverse('post_detail',args=[str(self.pk)])
        return reverse('Home')

