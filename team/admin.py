from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from team.models import *


class SocialNetwork(admin.TabularInline):
    model = SocialNetwork
    extra = 0
    show_change_link = True


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Member
        fields = ('email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Member
        fields = ('email', 'password', 'is_active', 'is_admin', )

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    inlines = (SocialNetwork,)
    list_display = ('get_full_name', 'email', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Персональная информация', {'fields': ('profile_image', 'first_name', 'last_name', 'description', 'contact_link')}),
        ('Права пользователя', {'fields': ('is_admin', 'is_active', 'groups')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(Member, UserAdmin)


class SEOAdmin(admin.StackedInline):
    model = SEO
    extra = 0
    fields = (
        'seo_description',
        'key_words',
    )
    show_change_link = True


class ArticleAdmin(admin.StackedInline):
    model = Article
    extra = 0
    fields = (
        'title', 'main_image', 'short_description', 'description')

    class Media:
        js = ['js/FB_CKEditor.js',
              'js/ckeditor.js']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


class ProjectAdmin(admin.ModelAdmin):
    model = Project
    prepopulated_fields = {'slug': ('name',)}

    fields = (
        'name','sub_name','card_name','image' ,'git', 'description', 'members')
    inlines = (ArticleAdmin, SEOAdmin)

    class Media:
        js = ['js/FB_CKEditor.js',
              'js/ckeditor.js']


admin.site.register(Project, ProjectAdmin)


class PatnerAdmin(admin.ModelAdmin):
    model = Partner
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        (None, {'fields': ('name', 'type_partner', 'slug', 'image',)}),
        ('Описание', {'fields': ('description',)}),
        ('Контакты', {'fields': ('address', 'site', 'phone')}),
    )

    class Media:
        js = ['js/FB_CKEditor.js',
              'js/ckeditor.js']


admin.site.register(Partner, PatnerAdmin)
admin.site.register(Tag)
