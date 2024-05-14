from django.db import models

# Create your models here.
# Create your models here.
class item(models.Model):
    photo = models.ImageField(upload_to='', blank=True, null=True)
    item_name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, blank=True, null=True)
    price = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item_name


class invoice_heading(models.Model):
    photo = models.ImageField(upload_to='', blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)


class invoice(models.Model):
    customer = models.CharField(max_length=255, blank=True, null=True)
    total = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}"

class invitem(models.Model):
    inv = models.ForeignKey(invoice, on_delete=models.CASCADE)
    item = models.CharField(max_length=255)
    qty = models.PositiveIntegerField(default=0)
    rate = models.PositiveIntegerField(default=0)
    amount = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item

