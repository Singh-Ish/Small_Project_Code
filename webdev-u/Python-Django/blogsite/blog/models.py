from django.db import models

# adding the packages

from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self): # its the link to button or function
        self.published_date = timezone.now
        self.save()


    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self): # once you create a instance of the post where should the siute go
        return reverse("post_detail" ,kwargs={'pk':self.pk}) # goint to the post_detail page for the specific post lidentified as pk the primary key


    def __str__():
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post',related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self): # once you create a instance of the post where should the siute go
        return reverse("post_list" ,kwargs={'pk':self.pk}) # home page is gonna be the list of post


    def __str__(self):
        return self.text
