from django.shortcuts import reverse
from django.db import models

class Inventory(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)
    cost_per_item =models.DecimalField( max_digits=20,decimal_places=2, null=False,blank=False)
    quantity_in_stock=models.CharField(max_length=100,null=False,blank=False)
    quantity_sold=models.IntegerField(null=False,blank=False)
    sales=models.DecimalField(max_digits=20,decimal_places=2,null=False,blank=False)
    stock_date=models.DateField(auto_now=True)
    last_sales_date=models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse("myapp:per_product", kwargs={
            'pk': self.id
        })
    
    def delete_item(self):
        return reverse("myapp:delete_inventory", kwargs={
            'pk': self.id
        })
    
    def update_item(self):
        return reverse("myapp:update_inventory", kwargs={
            'pk': self.id
        })




# Create your models here.

# Create your models here.
