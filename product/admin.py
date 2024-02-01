from django.contrib import admin
from . models import OrderPlaced, Payment, Product,Customer,Cart, Wishlist
from django.utils.html import format_html
from django.urls import reverse
from django.contrib.auth.models import Group

# Register your models here.

admin.site.site_header = 'Aji Misty Moo'

@admin.register(Product)
class  ProductModelAdmin(admin.ModelAdmin):
    list_display= ['id', 'title', 'discounted_price', 'category', 'product_image']


@admin.register(Customer)
class  CustomerModelAdmin(admin.ModelAdmin):
    list_display= ['id', 'user', 'address', 'city', 'state','pincode']
    

@admin.register(Cart)
class  CartModelAdmin(admin.ModelAdmin):
    list_display= ['id', 'user', 'product', 'quantity']
    def products(self,obj):
        link = reverse("admin:app_product_change",args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>',link, obj.product.title)
    

@admin.register(Payment)
class  PaymentModelAdmin(admin.ModelAdmin):
    list_display= ['id', 'user', 'amount', 'razorpay_order_id','razorpay_payment_status','razorpay_payment_id','paid']
    
    
@admin.register(OrderPlaced)
class  OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display= ['id', 'user', 'customer', 'product','quantity','ordered_date','status','payment']
    

@admin.register(Wishlist)
class WishlistModelAdmin(admin.ModelAdmin):
    list_display= ['id', 'user', 'product']
    
    
admin.site.unregister(Group)
