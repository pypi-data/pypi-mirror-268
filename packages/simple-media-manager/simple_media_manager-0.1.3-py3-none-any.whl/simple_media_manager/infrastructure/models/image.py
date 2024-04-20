from django.db import models

from ..models.file import File


class Image(File):
    image = models.ImageField(upload_to='media/simple_media_manager/images', null=True)
