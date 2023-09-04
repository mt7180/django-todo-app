from django.db import models

# Create your models here.
class ToDoEntry(models.Model):

    text = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)
    completion_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.text
    
    class Meta: 
        ordering = ["creation_date"]    #todo ordering for completed todos
