from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User

from django import forms
from django.contrib import admin
from .models import Blog,Category,FeaturedPosts




class Categories(admin.ModelAdmin):

    list_display = ('category',)
admin.site.register(Category,Categories)



#Create custom form with specific queryset:
class CustomBlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CustomBlogModelForm, self).__init__(*args, **kwargs)

        self.fields['posted_by'].queryset = User.objects.filter(is_superuser=True)



class BlogPost(admin.ModelAdmin):
    form=CustomBlogModelForm
admin.site.register(Blog,BlogPost)



class CustomBlogFeaturedModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CustomBlogFeaturedModelForm, self).__init__(*args, **kwargs)

        self.fields['posted_by'].queryset = User.objects.filter(is_superuser=True)


class BlogPostFeatured(admin.ModelAdmin):
    form = CustomBlogFeaturedModelForm
admin.site.register(FeaturedPosts,BlogPostFeatured)
