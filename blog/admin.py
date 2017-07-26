from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import gettext_lazy as _

from blog.models import Article
from team.models import SEO


class SEO(admin.StackedInline):
    model = SEO
    extra = 0
    fields = (
        'seo_description',
        'key_words',
    )
    show_change_link = True


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('Основное', {'fields': ('title', 'sub_title', 'slug', 'post_in_vk', 'post_in_twitter', 'type', 'main_image')}),
        ('Описание', {'fields': ('tags', 'short_description', 'description')}),
    )
    inlines = (SEO,)

    class Media:
        js = ['js/FB_CKEditor.js',
              'js/ckeditor.js']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


admin.site.register(Article, ArticleAdmin)


# Define a new FlatPageAdmin
class FlatPageAdmin(FlatPageAdmin):
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites')}),
        (_('Advanced options'), {
            'classes': ('collapse',),
            'fields': (
                'enable_comments',
                'registration_required',
                'template_name',
            ),
        }),
    )


# Re-register FlatPageAdmin
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
