from django.db import models


class PhoneCode(models.Model):
    country = models.CharField(verbose_name="Country", max_length=255)
    code = models.CharField(verbose_name="Code", max_length=255)

    def __str__(self):
        return f"{self.country} {self.code}"

    class Meta:
        app_label = "shared"
        verbose_name = "Phone Code"
        verbose_name_plural = "Phone Codes"
        ordering = ["country"]
