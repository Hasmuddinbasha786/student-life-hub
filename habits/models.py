from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    streak = models.IntegerField(default=0)
    last_completed = models.DateField(null=True, blank=True)

    def mark_done(self):
        today = date.today()
        if self.last_completed == today:
            return

        if self.last_completed and (today - self.last_completed).days == 1:
            self.streak += 1
        else:
            self.streak = 1

        self.last_completed = today
        self.save()

    def __str__(self):
        return self.name
