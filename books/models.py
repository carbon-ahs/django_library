from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Book(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    subtitle = models.CharField(_("Subtitle"), max_length=50)
    author = models.CharField(_("Author"), max_length=50)
    isbn = models.CharField(_("ISBN"), max_length=13)

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Book_detail", kwargs={"pk": self.pk})
