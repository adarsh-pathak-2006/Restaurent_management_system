from django.db import models
from booking.models import Table

class Menu(models.Model):
    item_name=models.CharField(max_length=200)
    item_price=models.PositiveIntegerField()
    stock=models.PositiveIntegerField()
    is_avaliable=models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.stock==0:
            self.is_avaliable=False
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.item_name} of {self.restaurent.name}"


class Order(models.Model):
    items=models.ForeignKey(Menu, on_delete=models.CASCADE)
    table=models.ForeignKey(Table, on_delete=models.CASCADE)
    item_quantity=models.PositiveIntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    total_price=models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        self.total_price=self.items.item_price * self.item_quantity
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.items.item_name} on table id {self.table.table_id}"

