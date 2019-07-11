# 1. How to image fields work in django?

```python
1.project/apps/models.py

from django.db import models
import os
import random

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name,ext

def upload_file_path(instance,filename):
    new_filename = random.randint(1,3464565773498)
    name,ext=get_filename_ext(filename)
    final_filename = f'{new_filename}{ext}'
    return f'{new_filename}/{final_filename}'


class Product(models.Model):
    ....
    image = models.ImageField(upload_to=upload_file_path)

    def __str__(self):
        return str(self.title)
```

```python
2.project/url.py

from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += \
                static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += \
                static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
```

```python
3. project/settings.py

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]


MEDIA_URL = '/media-file/'

MEDIA_ROOT = os.path.join(BASE_DIR,'media-storage')
```


> Please inbox **[me](https://www.facebook.com/mostafijur.rahman299)** if you've any questions.
