from __future__ import annotations

import os

from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    display_name = models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.display_name


class Module(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.id


def create_file_path(instance: Package, _) -> str:
    return f'{instance.module.id}/{instance.file_name}'


class Package(models.Model):
    date_uploaded = models.DateTimeField(auto_now_add=True)
    date_published = models.DateTimeField(null=True, blank=True)
    file_name = models.CharField(max_length=128, primary_key=True)
    file = models.FileField(upload_to=create_file_path)

    module = models.ForeignKey(to=Module, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    version = models.CharField(max_length=32)
    license = models.CharField(max_length=64)
    authors = models.JSONField(blank=True)
    requirements = models.JSONField(blank=True)
    permissions = models.PositiveBigIntegerField()

    def __str__(self) -> str:
        return f'{self.module.id} {self.version}'
