from django.contrib import admin

from apps.discounts.models import Discount


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('company', 'category', 'status',
                    'discount_type', 'currency', 'title', 'old_price',
                    'description', 'video', 'id_generate', 'in_stock',
                    'available', 'views', 'likes', 'dislikes', 'start_date',
                    'end_date', 'delivery', 'installment', 'is_active', 'created_at',
                    'discount_value', 'discount_value_is_percent', 'min_quantity',
                    'bonus_quantity', 'bonus_discount_value', 'bonus_discount_value_is_percent',
                    'service')