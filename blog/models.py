from django.db import models

# Create your models here.
"""
This blog has three models: 

- Category: Which defines the category
  the post belongs to and has just the name attribute.

-Post: the post model has the title, content (body)
 time created(with the auto_now_add stamp to automatically
 record the time the post was created) and the categories
 the post belongs(which has a many-many relationship) attributes

-Comment: This is the model for the comments of those that may be 
 willing to respond to the post. It has a many-one relationship as 
 a post can only have many comments. It has the on_delete option set to
 CASCADE so that when posts are deleted their comments are also deleted
 alongside.


"""
class Category(models.Model):
    name = models.CharField(max_length=20)

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)