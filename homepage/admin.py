from django.contrib import admin
from  .models import PastorsQuote,Grid

# Register your models here.



class Pastors_quote(admin.ModelAdmin):
    list_display = ('title','short_description','pastors_quote','posted_date','posted_by','pastors_picture')


admin.site.register(PastorsQuote, Pastors_quote)


class GridImages(admin.ModelAdmin):
    list_display = ('image', 'posted_date')

admin.site.register(Grid, GridImages)


