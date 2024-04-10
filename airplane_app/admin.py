from django.contrib import admin
from airplane_app.models import Customer, Order, Product, OrderDetail


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "name", "email", "phone",)
    list_editable = ("email", "phone",)


admin.site.register(Customer, CustomerAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ("id_order", "id_client", "date_order", "status_order", "id_transaction")
    list_editable = ("id_client", "status_order", "id_transaction")


admin.site.register(Order, OrderAdmin)


class ProductsAdmin(admin.ModelAdmin):
    list_display = ("id_product", "name", "description", "price", "image", "stock")
    list_editable = ("name", "description", "price", "image", "stock")


admin.site.register(Product, ProductsAdmin)


class OrderDetailsAdmin(admin.ModelAdmin):
    list_display = ("id_order", "id_product", "quantity", "price")
    list_editable = ("id_product", "quantity", "price")


admin.site.register(OrderDetail, OrderDetailsAdmin)