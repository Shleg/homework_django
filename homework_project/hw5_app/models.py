from django.db.models import F, Sum
# Create your models here.
from django.db import models
from django.utils import timezone


class Client(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя клиента")
    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона")
    address = models.TextField(verbose_name="Адрес")
    registration_date = models.DateTimeField(default=timezone.now, verbose_name="Дата регистрации")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    quantity = models.IntegerField(verbose_name="Количество")
    date_added = models.DateTimeField(default=timezone.now, verbose_name="Дата добавления")
    image = models.ImageField(upload_to='products/', verbose_name="Изображение", null=True, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    client = models.ForeignKey(Client, related_name='orders', on_delete=models.CASCADE, verbose_name="Клиент")
    products = models.ManyToManyField(Product, through='OrderItem', verbose_name="Товары")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Общая сумма заказа", default=0)
    order_date = models.DateTimeField(default=timezone.now, verbose_name="Дата оформления заказа")

    def update_total_amount(self):
        self.total_amount = self.orderitem_set.aggregate(
            total=Sum(F('quantity') * F('product__price'))
        )['total'] or 0
        self.save()

    def __str__(self):
        return f"Order {self.id} by {self.client.name}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.order.update_total_amount()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.order.update_total_amount()

    def __str__(self):
        return f"{self.quantity} x {self.product.name} for {self.order.id}"

