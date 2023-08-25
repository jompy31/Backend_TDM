from django.contrib import admin
from .models import Product, Characteristic

class CharacteristicInline(admin.TabularInline):  # or admin.StackedInline
    model = Product.characteristics.through  # Many-to-many through model
    extra = 1
    verbose_name_plural = "Characteristics"

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "characteristic":
            kwargs["queryset"] = Characteristic.objects.all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'characteristic':
            formfield.label_from_instance = lambda obj: f'{obj.name} - {obj.description}'
        return formfield

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'created_at')  # Fields to display in the list of objects
    list_filter = ('user', 'created_at')  # Fields for filtering the objects
    search_fields = ('name', 'user__username')  # Fields for search
    date_hierarchy = 'created_at'  # Date hierarchy for quick navigation
    inlines = [CharacteristicInline]  # Display associated characteristics inline

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('characteristics')  # Prefetch characteristics

admin.site.register(Product, ProductAdmin)
admin.site.register(Characteristic)
