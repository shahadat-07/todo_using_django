from django.db import models

# Create your models here.


class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=30)
    taskDescription = models.CharField(max_length=200)
    is_completed = models.BooleanField(
        default=False)

    class Meta:
        ordering = ["taskTitle"]

    def __str__(self):
        return self.taskTitle
