# 11. How to Deploy your Django application on Heroku?

* You can deploy your django application on heroku to follow: [Getting Started on Heroku with Python](https://devcenter.heroku.com/articles/getting-started-with-python) or 

1. Go to: [www.heroku.com](https://www.heroku.com/)

2. Now: **Sign up & Log in** 

3. Now go to: [The Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) 

for **Ubuntu 16+**
```python
* Run the following command from your terminal:

$ sudo snap install --classic heroku

$ heroku --version 
```
```python
4. $ (venv) user@sdshoriot:~/Desktop/s$ heroku login
```

5. Create: ```Procfile``` on project directory (beside the .gitignore file).

* now on ```Procfile``` write: ```web : gunicorn (your project name).wsgi --log-file -```
```python
$ pip install gunicorn
```
```python
6. project/setting.spy

ALLOWED_HOSTS = ['*']
```
```python
7. Now you’re ready to create your first Heroku app:

$ heroku create or $ heroku create 'give your app name as you want like shoriot'

* app name: warm-fortress-99059

$ heroku git:remote -a (app name)
```
```python
8. $ git status

$ git add .

$ git commit -m "added heroku"

$ git push heroku master

then see: remote:        https://(your app name).herokuapp.com/
```

```python
9. $ heroku ps:scale web=1

Finally, check that everything is working:

$ heroku open
```



