from django.db import models
from django.core.exceptions import ValidationError


class Category(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300, unique=True)
    parent = models.ForeignKey('self',
                               on_delete=models.PROTECT,
                               related_name='children',
                               blank=True,
                               null=True)
    icon = models.ImageField(upload_to='categories/icons/%Y/%m/%d/',
                             blank=True,
                             null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        #  =============== Check parent limit. Parent MUST BE MAX 3   ========================
        try:
            if not self.pk and self.parent.parent.parent:
                raise ValidationError({'parent': 'Category must be 3 category degree'})
        except AttributeError:
            pass

    def __str__(self):
        return self.name