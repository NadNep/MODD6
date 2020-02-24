import json
from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User


# модель автора.
class Author(models.Model):
    full_name = models.TextField()  # str
    birth_year = models.SmallIntegerField()  # int
    country = models.CharField(max_length=2)  # ограничение 2 симв


def __str__(self):
    return self.full_name


# модель книги
class Book(models.Model):
    ISBN = models.CharField(max_length=13)  # ограничение в 13 симв
    title = models.TextField()
    image = models.ImageField(help_text='20x20px', blank=True)
    description = models.TextField()
    year_release = models.SmallIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # поле внешнего ключа
    copy_count = models.SmallIntegerField(default=1, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=' ')
    redaction = models.ForeignKey('Publish', on_delete=models.CASCADE, null=True, blank=True, related_name='books')
    reader = models.ForeignKey('Reader', on_delete=models.CASCADE, null=True, blank=True, related_name='books')


# модель издательства
class Publish(models.Model):
    name = models.CharField(max_length=100)


def __str__(self):
    return self.name


# модель читатель
class Reader(models.Model):
    full_name = models.TextField()  # str
    birth_year = models.SmallIntegerField()  # int
    # картинки


@property
def image_img(self):
    if self.image and hasattr(self.image, 'url'):
        return self.image.url


class UserProfile(models.Model):
    age = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    def save(self, *args, **kwargs):
            ## загрузить текущую строку и
            ## преобразовать строку в словарь Python
        extra_data = json.loads(self.data)

            ## сделать что-нибудь со словарем
        for something in somethings:
            extra_data [something] = some_function(something)

            ## если он пуст, сохраните его обратно в строку '{}',
            ## если он не пустой, преобразовать словарь обратно в строку json
        if not extra_data:
            self.data = '{}'
        else:
            self.data = json.dumps(extra_data)

        super(UserProfile, self).save(*args, **kwargs)
