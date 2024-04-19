from collections.abc import Iterator

from django.db.models import Max

from simple_media_manager.domain.repository.image import ImageReadRepository, ImageWriteRepository
from simple_media_manager.infrastructure.models import Image


class DjangoImageWriteRepository(ImageWriteRepository):

    def save(self, file: bytes, name: str = '') -> Image:
        return Image.objects.create(file=file, name=name)

    def bulk_save(self, files: list) -> Iterator[Image]:
        # Get the maximum ID value currently present in the database
        max_id = Image.objects.aggregate(max_id=Max('id'))['max_id'] or 0

        # Generate new instances of Image models with unique IDs starting from max_id + 1
        new_images = []
        for idx, data in enumerate(files, start=max_id + 1):
            new_image = Image(id=idx, image=data.get('image'), name=data.get('name'))
            new_images.append(new_image)

        # Use bulk_create() to insert the new instances into the database
        return Image.objects.bulk_create(new_images)

    def delete(self, id: int):
        Image.objects.get(id=id).delete()


class DjangoImageReadRepository(ImageReadRepository):
    def all(self) -> Iterator[Image]:
        return Image.objects.all()

    def get(self, pk: int) -> Image:
        return Image.objects.get(pk=pk)

    def find(self, name: str) -> Iterator[Image]:
        return Image.objects.filter(name__icontains=name)
