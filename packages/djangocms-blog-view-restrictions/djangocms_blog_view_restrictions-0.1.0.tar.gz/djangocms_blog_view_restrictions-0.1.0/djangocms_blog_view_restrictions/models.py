from django.conf import settings
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from djangocms_blog.models import Post


class ViewRestrictionExtension(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="view_restrictions_extensions"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_("user"),
        blank=True,
        null=True,
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        verbose_name=_("group"),
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _("View restriction")
        verbose_name_plural = _("View restrictions")

    def __str__(self):
        return _("View restriction for post #{post_id}").format(post_id=self.post.id)

    def clean(self):
        super().clean()

        if not self.user and not self.group:
            raise ValidationError(_("Please select user or group."))

        if self.user and self.group:
            raise ValidationError(_("Please select user or group, but not both."))
