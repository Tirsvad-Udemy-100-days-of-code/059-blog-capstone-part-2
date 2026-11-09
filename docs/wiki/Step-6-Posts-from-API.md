**English** · [Dansk](Step-6-Posts-from-API-da) · [Bahasa Malaysia](Step-6-Posts-from-API-ms)

# Step 6: posts from an API

The posts are no longer typed into the HTML. They are JSON served by an API and shown with a Jinja `for` loop.

![The home page listing the posts][step-6]

```html
{% for post in posts %}
  <a href="{{ url_for('show_post', index=post.id) }}">
    <h2 class="post-title">{{ post.title }}</h2>
    <h3 class="post-subtitle">{{ post.subtitle }}</h3>
  </a>
  <p class="post-meta">Posted by {{ post.author }} on {{ post.date }}</p>
{% endfor %}
```

The data is read with the standard library (`urllib`), so the project needs no `requests`. If the API cannot be reached, the copy of the sample posts that ships with the package is used, so the site and the tests work offline. The posts are parsed in one place into a `Post`, and the use case `get_posts` hands them to the route.

## What we gained

- Dot notation in Jinja (`post.title`) reads naturally; the same loop works for any number of posts.
- Reading from an API is a separate concern: the route does not know where posts come from, so tests inject a fake repository.
- A fallback and a timeout (`REQUEST_TIMEOUT_SECONDS` in `constants.py`) keep the page working when the network does not.

---

[step-6]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2/raw/branch/main/docs/screenshots/step-6-home-posts.png
