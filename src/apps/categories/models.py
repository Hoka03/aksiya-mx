from django.db import models
from django.core.exceptions import ValidationError

from src.apps.general.validate_file_size import validate_logo_size
from src.apps.general.normalize_text import normalize_text


class Category(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300, unique=True)
    parent = models.ForeignKey('self',
                               on_delete=models.PROTECT,
                               related_name='children',
                               blank=True,
                               null=True)
    icon = models.ImageField(upload_to='categories/icons/%Y/%m/%d/',
                             validators=[validate_logo_size],
                             blank=True,
                             null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_normalize_fields(self):
        return [
            'name',
            'slug'
        ]

    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)

    def clean(self):
        #  =============== Check parent limit. Parent MUST BE MAX 3   ========================
        try:
            if not self.pk and self.parent.parent.parent:
                raise ValidationError({'parent': 'Category must be 3 category degree'})
        except AttributeError:
            pass

    def __str__(self):
        return self.name