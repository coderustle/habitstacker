from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from guardian.models import GroupObjectPermissionBase, UserObjectPermissionBase


class Habit(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created",)
        get_latest_by = "created"
        indexes = [models.Index(fields=["-created"])]
        default_permissions = ("add", "change", "delete")
        permissions = (("view_habit", "View Habit Objects"),)

    def get_absolute_url(self):
        return reverse("budget:details", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return self.title


class HabitLog(models.Model):
    date = models.DateField(auto_now_add=True)
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ["date", "habit"]
        indexes = [models.Index(fields=["-date"])]

    def __str__(self) -> str:
        return f"{self.habit.title} on {self.date}"


class HabitUserObjectPermission(UserObjectPermissionBase):
    content_object = models.ForeignKey(Habit, on_delete=models.CASCADE)


class HabitGroupObjectPermission(GroupObjectPermissionBase):
    content_object = models.ForeignKey(Habit, on_delete=models.CASCADE)


class HabitLogUserObjectPermission(UserObjectPermissionBase):
    content_object = models.ForeignKey(HabitLog, on_delete=models.CASCADE)


class HabitLogGroupObjectPermission(GroupObjectPermissionBase):
    content_object = models.ForeignKey(HabitLog, on_delete=models.CASCADE)
