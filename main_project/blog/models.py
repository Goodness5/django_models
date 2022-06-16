from django.db import models
class Members(models.Model):
Title = models.CharField(max_length=200)
Text = models.TextField()
author = models.ForeignKey(get_user_model())
created_date = models.DateTimeField(auto_now_add=True)
published_date = models.DateTimeField(auto_now_add=True)