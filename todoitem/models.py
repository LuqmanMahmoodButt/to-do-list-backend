from django.db import models



class Todoitem(models.Model):
    def __str__(self):
        return f'{self.item}'  

    item = models.CharField(max_length=300)
    
    
