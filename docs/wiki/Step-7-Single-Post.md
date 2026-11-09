**English** · [Dansk](Step-7-Single-Post-da) · [Bahasa Malaysia](Step-7-Single-Post-ms)

# Step 7: one page per post

Clicking a title opens `/post/<id>`, which shows the title, subtitle, author, date and body over a full-width image.

![The post page for The Life of Cactus][step-7]

```python
app.add_url_rule("/post/<int:index>", endpoint="show_post", view_func=show_post)

def show_post(index: int) -> str:
    try:
        post = get_post(posts_source, index)
    except PostNotFoundError:
        abort(404)
    return render_template("post.html", post=post)
```

## What we gained

- A URL can carry a variable part: `<int:index>` is converted to an `int` for you.
- Looking something up and not finding it is a normal case: the use case raises `PostNotFoundError` and the route answers 404.
- The same `post.html` shows every post, and the header image comes from the post's own `image_url`.

---

[step-7]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2/raw/branch/main/docs/screenshots/step-7-post.png
