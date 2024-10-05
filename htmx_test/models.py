from django.db import models


class Opera(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Singer(models.Model):
    opera = models.ForeignKey(Opera,
                              on_delete=models.CASCADE,
                              blank=True,
                              null=True)
    voice = models.CharField(max_length=20)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
