import json
from django.contrib import admin
from .models import Inventory, FileUpload
from pyxlsb import open_workbook


class InventoryAdmin(admin.ModelAdmin):
    list_display = ('serial_number', 'quantity', 'price')
    pass


class FileUploadAdmin(admin.ModelAdmin):
    list_display = ('filename', 'file_date', 'field', 'calculate_field')
    fields = ('filename', 'file_date', 'field')

    def save_model(self, request, obj, form, change):
        xls = form.cleaned_data['field']
        qty = 0
        total_price = 0
        with open_workbook(xls) as wb:
            row_generator = wb.get_sheet(1).rows()
            row_generator.__next__()
            for row in row_generator:
                item_inventory = [item.v for item in row]
                onj_inventory = Inventory()
                onj_inventory.serial_number = item_inventory[0]
                onj_inventory.quantity = item_inventory[1]
                onj_inventory.price = item_inventory[2]
                onj_inventory.save()

                for cell in row:
                    if cell.c == 1:
                        qty += int(cell.v)
                    elif cell.c == 2:
                        total_price += float(cell.v)

        prom = total_price / qty

        # obj.calculate_field = json.dumps({'elementos': qty, 'precio promedio': prom})
        obj.calculate_field = {'elementos': qty, 'precio promedio': prom}
        super().save_model(request, obj, form, change)


admin.site.register(Inventory, InventoryAdmin)
admin.site.register(FileUpload, FileUploadAdmin)
