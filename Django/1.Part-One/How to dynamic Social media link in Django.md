# 4. How to dynamic Social media link in Django?


```python 
1. app/models.py


class Profile(models.Model):

	...
	facebook = models.URLField(null=True, blank=True)
	twitter  = models.URLField(null=True, blank=True)
	linkedin = models.URLField(null=True, blank=True)
```

```python
2. templates/app/authors.html

...
{% for author in authors %}
...
<div class="social">
  <a href="{{ author.facebook }}" class="facebook"><img src="/static/img/social/facebook.png" alt=""></a>

  <a href="{{ author.twitter }}" class="twitter"><img src="/static/img/social/twitter.png" alt=""></a>

  <a href="{{ author.linkedin }}" class="linked-in"><img src="/static/img/social/linked-in.png" alt=""></a>
</div>
...
{% endfor %}
```


