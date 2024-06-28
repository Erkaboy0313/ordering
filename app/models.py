from django.db import models
from parler.models import TranslatableModel,TranslatedFields

class Table(models.Model):
    number =models.IntegerField()

    def __str__(self):
        return f"{self.number}"

class Order(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    peple_count =models.IntegerField()
    price_v1 =models.FloatField(blank=True, null=True)
    price_v2 =models.FloatField(blank=True, null=True)
    total_price =models.FloatField(blank=True, null=True)


class Category(TranslatableModel):
    translations = TranslatedFields(
        name =models.CharField(max_length=100),
    )

    def __str__(self):
        return f"{self.safe_translation_getter('name')}"

class MenuItem(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=100),
        description = models.TextField()
    )
    image = models.ImageField(upload_to='Food/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)    
    price = models.FloatField()


    def __str__(self):
        return f"{self.safe_translation_getter('name')}"

class OrderItem(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.order.name}"
    
data = {
    "table":'id',
    "peple_count":5,
    "order_items":[
        {
            "menu_item":'id',
            "count":3
        },
        {
            "menu_item":'id',
            "count":3
        },
        {
            "menu_item":'id',
            "count":3
        },
    ]
}


