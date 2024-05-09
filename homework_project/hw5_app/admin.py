from django.contrib import admin
from .models import Client, Product, Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'total_amount', 'order_date')
    inlines = [OrderItemInline]
    readonly_fields = ('total_amount', 'order_date')


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'address', 'registration_date')
    search_fields = ('name', 'email')
    readonly_fields = ('registration_date',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'date_added', 'image')
    search_fields = ('name',)
    readonly_fields = ('date_added',)


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
