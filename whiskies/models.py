from django.conf import settings
from django.db import models
from django.urls import reverse

STATUS_CHOICES = (
    ('reading', 'Reading'),
    ('finishes', 'Finished')
)


class Whisky(models.Model):
    title = models.CharField(max_length=150)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="whiskies"
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("whisky_detail", kwargs={
            "pk": self.id
        })
