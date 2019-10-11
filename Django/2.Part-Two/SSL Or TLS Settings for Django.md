# SSL/TLS Settings for Django

Let's make your Django project's settings exactly what we do here. Once you do that, you'll have a production.py file. 
That's where we'll be working.

    Make sure your host has the ability to secure sites like these do: Heroku, Elastic Beanstalk, 
        Linode, Webfaction, and Digital Ocean.
    You have your SSL/TLS Security Certificate installed (on one of those services)
    
Update production.py with:

```python
CORS_REPLACE_HTTPS_REFERER      = True
HOST_SCHEME                     = "https://"
SECURE_PROXY_SSL_HEADER         = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT             = True
SESSION_COOKIE_SECURE           = True
CSRF_COOKIE_SECURE              = True
SECURE_HSTS_INCLUDE_SUBDOMAINS  = True
SECURE_HSTS_SECONDS             = 1000000
SECURE_FRAME_DENY               = True
```

Update local.py & base.py to:

```python
CORS_REPLACE_HTTPS_REFERER      = False
HOST_SCHEME                     = "http://"
SECURE_PROXY_SSL_HEADER         = None
SECURE_SSL_REDIRECT             = False
SESSION_COOKIE_SECURE           = False
CSRF_COOKIE_SECURE              = False
SECURE_HSTS_SECONDS             = None
SECURE_HSTS_INCLUDE_SUBDOMAINS  = False
SECURE_FRAME_DENY               = False
```

