from django.db import models

class jadval(models.Model):
    name = models.CharField(max_length=190, default='')
    nechtaligi = models.PositiveIntegerField(default=1)
    def __str__(self) -> str:
        return self.name


class phone(models.Model):
    name = models.CharField(max_length=201, default='')
    number = models.PositiveIntegerField(default=1)
    def __str__(self) -> str:
        return self.name