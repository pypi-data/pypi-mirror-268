from django import template
from django.contrib.auth.models import AnonymousUser
from djangocms_blog.models import Post


register = template.Library()


@register.filter()
def can_view_post(user, post):
    if not isinstance(post, Post) or isinstance(user, AnonymousUser):
        return False

    is_user_granted = post.view_restrictions_extensions.filter(user=user).exists()
    is_group_granted = post.view_restrictions_extensions.filter(
        group__in=user.groups.all()
    ).exists()
    if is_user_granted or is_group_granted or user.is_superuser:
        return True

    return False
