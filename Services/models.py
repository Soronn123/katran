from django.db import models
from django.core.files.storage import FileSystemStorage
from django.core.files.storage import default_storage

class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        # Удаляет файл если он уже существует
        if self.exists(name):
            self.delete(name)
        return name


class IconModel(models.Model):
    name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class TypeModel(models.Model):
    TYPE_CHOICES = [
        (1, 'for ItemModel'),
        (2, 'for ServiceModel'), 
    ]

    name = models.CharField(max_length=50, blank=True) 
    text = models.TextField(blank=True)
    typeResource = models.IntegerField(choices=TYPE_CHOICES, default=1)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        db_table = 'types'


class ItemModel(models.Model):
    name = models.CharField(max_length=50, blank=True)
    price = models.IntegerField(blank=True)
    text = models.TextField(blank=True)
    image = models.ImageField(blank=True, upload_to='products/', storage=OverwriteStorage(), default="default/s1.png")
    dateCreated = models.DateField(auto_now_add=True)
    typeId = models.ForeignKey(TypeModel, on_delete=models.CASCADE, limit_choices_to={'typeResource': 1}, related_name='items')


    def __str__(self):
        return f"{self.name} + {self.price}"

    class Meta:
        db_table = 'items'

    def save(self, *args, **kwargs):
        if self.pk:
            old = ItemModel.objects.get(pk=self.pk)
            if old.image and old.image != self.image:
                old.image.delete(save=False)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        super().delete(*args, **kwargs)

    def image_url(self):
        if self.image and default_storage.exists(self.image.name):
            return self.image.url
        return '/media/default/s1.png'


class ServiceModel(models.Model):
    name = models.CharField(max_length=50, blank=True)
    price = models.IntegerField(blank=True)
    text = models.TextField(blank=True)
    typeId = models.ForeignKey(TypeModel, on_delete=models.CASCADE, limit_choices_to={'typeResource': 2}, related_name='services')
    iconId = models.ForeignKey(IconModel, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return f"{self.name} + {self.price}"

    class Meta:
        db_table = 'services'