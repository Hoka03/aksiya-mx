from django.contrib import admin

from apps.companies.models.company import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'get_categories', 'last_name', 'first_name',
                    'father_name', 'logo', 'video', 'banner', 'country',
                    'district', 'name', 'username', 'slogan', 'address',
                    'phone_number', 'delivery', 'installment', 'description',
                    'web_site', 'longitude', 'latitude', 'balance', 'created_at')
    list_display_links = list_display
    list_filter = ('country', 'district', 'delivery', 'installment')
    search_fields = ('name', 'username', 'first_name')
    ordering = ('-created_at',)
    prepopulated_fields = {'username': ['name']}
    readonly_fields = ('created_at',)

    def get_categories(self, obj):
        """
        Here check for view category field, because this field is M2MField
        """
        return ", ".join([category.name for category in obj.category.all()]) if obj.category.exists() else 'None'
    get_categories.short_description = 'Categories'  # Sets column name in admin
