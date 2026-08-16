from django.db import models
from django.contrib.auth.models import User

class Table(models.Model):
    table_id=models.CharField(max_length=3)
    seats=models.ValueRange(start=2, end=4)
    is_avaliable=models.BooleanField(default=True)

    def __str__(self):
        return self.table_id


class Reservation(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    table=models.OneToOneField(Table, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints=[models.UniqueConstraint(fields=['table', 'user'], name='each_table_per_reservation')]

    def save(self, *args, **kwargs):
        self.table.is_avaliable==False
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.table.table_id} -- {self.id}"

