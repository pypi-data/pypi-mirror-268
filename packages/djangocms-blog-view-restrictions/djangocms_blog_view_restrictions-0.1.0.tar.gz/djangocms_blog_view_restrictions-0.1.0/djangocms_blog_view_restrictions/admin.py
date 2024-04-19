from django.contrib import admin
from django.utils.translation import gettext as _
import djangocms_blog.admin as blog_admin

from .models import ViewRestrictionExtension


class ViewRestrictionExtensionInline(admin.TabularInline):
    model = ViewRestrictionExtension
    fields = ["post", "user", "group"]
    classes = ["collapse"]
    can_delete = True
    extra = 1
    verbose_name = _("View restriction")
    verbose_name_plural = _("View restrictions")


blog_admin.register_extension(ViewRestrictionExtensionInline)
