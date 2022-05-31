from ast import Delete, Str
from distutils.command.upload import upload
import email
from tkinter import CASCADE
from django.db import models
from tinymce import models as tinymce_models
from django.contrib.auth.models import User


class PostModel(models.Model):
    post_title = models.CharField(max_length=100, null=False)
    post_text = models.TextField()
    post_body =  tinymce_models.HTMLField()
    post_image= models.ImageField(upload_to='post_images/',null=True)
    
    def __str__(self) -> str:
        return self.post_title


class CommentModel(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel,on_delete=models.CASCADE)
    comment_body = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.comment_body

class ContactModel(models.Model):
    name = models.CharField( max_length=100,null=False)
    email = models.CharField( max_length=100,null=False)
    number = models.IntegerField()
    message = models.CharField( max_length=200,null=False)    

    def __str__(self) -> str:
        return self.name





