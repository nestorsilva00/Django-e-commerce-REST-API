from django.contrib import admin

from .models import Product
from .models import Product_Inventary
from .models import Category
from .models import Discount
from .models import Product_Image



admin.site.register(Product)
admin.site.register(Product_Inventary)
admin.site.register(Category)
admin.site.register(Discount)
admin.site.register(Product_Image)
