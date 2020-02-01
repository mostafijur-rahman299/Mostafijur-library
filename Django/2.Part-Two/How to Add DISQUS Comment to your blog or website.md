## 10. How to Add DISQUS Comment to your blog or website?

1. Go to [DISQUS](https://disqus.com/) & Click on **GET STARTED**

```python
2. Signup & Login

Name: xxxx

Email: xxx@gmail.com

Pass: ********
```
3. Now click on: **I want to install Disqus on my site**

4. Now give your **Website Name** like: ```xxx.com```

* Now select **Category** like: ```Tech```

* Now click on: **Create Site**

5. Now see **Basic** & click on: **subscribe Now**

6. Now click on (end of the page): **I don't see my platform listed, install manually with Universal Code**

7. Now copy the code of **(1) Place the following code where you'd like Disqus to load:** & past on the end of **post_detail.html_page**

```python
# blog/post_detail.html

# add this code to the end of post_detail.hmtl
<div id="disqus_thread"></div>
<script>

/**
*  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
*  LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables*/
/*
var disqus_config = function () {
this.page.url = PAGE_URL;  // Replace PAGE_URL with your page's canonical URL variable
this.page.identifier = PAGE_IDENTIFIER; // Replace PAGE_IDENTIFIER with your page's unique identifier variable
};
*/
(function() { // DON'T EDIT BELOW THIS LINE
var d = document, s = d.createElement('script');
s.src = 'https://banglai-django.disqus.com/embed.js';
s.setAttribute('data-timestamp', +new Date());
(d.head || d.body).appendChild(s);
})();
</script>
<noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
```
**Now Reload your post_detail_page & see It's working**


