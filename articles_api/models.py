from django.db import models
from django.urls import reverse


class Article(models.Model):
    athour = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateField()
    updated_at = models.DateField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
