from django.db import models
from django.conf import settings

# Create your models here.

class Todolist(models.Model):
    def __str__(self):
        return f'{self.title}'
     
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        "jwt_auth.User",
        related_name="todolist",
        on_delete=models.CASCADE,
       
    )
  
    class Meta:
        ordering = ['complete']