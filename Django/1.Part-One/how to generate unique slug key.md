# 1. How to image fields work in django?



```python
1.project/apps/models.py

from django.db import models
from django.db.models.signals import pre_save,post_save

from .utils import unique_slug_generator

class Product(models.Model):
    title = models.CharField(max_length = 104)
    slug = models.SlugField(blank=True,unique=True)
    

    def __str__(self):
        return str(self.title)


** slug receiver signals **
def product_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver,sender=Product)

```

```python
2.project/apps/admin.py

from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__','slug']
    class Meta:
        model = Product

admin.site.register(Product,ProductAdmin)

```

```python
3.project/apps/utils.py

from django.utils.text import slugify
import random
import string

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug
```

```python
4.project/urls.py

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

```

> Please inbox **[me](https://www.facebook.com/mostafijur.rahman299)** if you've any questions.
