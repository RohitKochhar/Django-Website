from django.db import models

class Category(models.Model):
    s_Name = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.s_Name}"

class Post(models.Model):
    s_Title         = models.CharField(max_length=255)
    s_Body          = models.TextField()
    d_Creation      = models.DateTimeField(auto_now_add=True)
    d_Modified      = models.DateTimeField(auto_now=True)
    o_Categories    = models.ManyToManyField('Category', related_name='posts')
    def __str__(self):
        return f"{self.s_Title}"

class Comment(models.Model):
    s_Author        = models.CharField(max_length=60)
    s_Body          = models.TextField()
    d_Creation      = models.DateTimeField(auto_now_add=True)
    o_Post          = models.ForeignKey('Post', on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.s_Author} on {self.d_Creation}"
