from django.db import models

# Create your models here.
# SQL
#ORM 
class Blog(models.Model):
    title = models.CharField( max_length=150)
    owner = models.CharField(max_length=50)
    post = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title