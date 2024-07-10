from django.db import models



class Todoitem(models.Model):
    def __str__(self):
        return f'{self.item}'  

    item = models.CharField(max_length=300)
    complete = models.BooleanField(default=False)
    todolist = models.ForeignKey(
        "todolist.Todolist",
        related_name="todoitem",
        on_delete=models.CASCADE,
       
    )
    