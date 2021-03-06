## 5. How to add TinyMCE Text-Editor in (admin_page) Django?

```python
1. $ pip install django-tinymce
```

```python
2. project/settings.py

INSTALLED_APPS = (
    ...
    'tinymce',
)
```

```python
3. project/urls.py

urlpatterns = [
    ...
    path(r'^tinymce/', include('tinymce.urls')),
]
```

```python
4. app/models.py

...
from tinymce.models import HTMLField

class MyModel(models.Model):
    ...
    description = HTMLField()
```

5. Now go to [Tinymce](https://www.tiny.cloud/get-tiny/) download page and download any sutiable version for your django app.


6. Now copy your downloaded Tinymce files and paste them in your project's static folder. like ```static/js/tinymce```

7. Now go to [Tinymce](https://www.tiny.cloud/docs/demo/basic-example/) demo page & Copy the content of ```JS``` file from editor.

8. Make a new file ```custom.js``` in ```static/js/tinymce``` folder and paste the copied content in it and save it.

9. Now include both ```tinymce.min.js``` & ```custom.js``` file in your desired template.

```python
* templates/base.html

...
<!--======Tinymce Text-Editor (Must be in Head Tag)=========-->
  <script src="{% static 'js/tinymce/tinymce.min.js' %}"></script>
  <script type="text/javascript" src="{% static 'js/tinymce/custom.js' %}" ></script>
...
```

```python
10. project/settings.py

...
TINYMCE_DEFAULT_CONFIG = {
    'height': 400,
    'width': 1210,
    }
...

"""
TINYMCE_DEFAULT_CONFIG = {
    'height': 360,
    'width': 1200,
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'theme': 'modern',
    'plugins': '''
            textcolor save link image media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists  charmap print  hr
            anchor pagebreak
            ''',
    'toolbar1': '''
            fullscreen preview bold italic underline | fontselect,
            fontsizeselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | codesample |
            ''',
    'toolbar2': '''
            visualblocks visualchars |
            charmap hr pagebreak nonbreaking anchor |  code |
            ''',
    'contextmenu': 'formats | link image',
    'menubar': True,
    'statusbar': True,
    }
"""
```

```python
11. templates/app/post_detail.html

...
<p>{{ post.description | safe }}</p>
...
```

* Now you can use a TinyMCE Text Editor in your django admin page.



