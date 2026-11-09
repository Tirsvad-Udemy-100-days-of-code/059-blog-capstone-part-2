[English](Step-6-Posts-from-API) · **Dansk** · [Bahasa Malaysia](Step-6-Posts-from-API-ms)

# Trin 6: indlæg fra et API

Indlæggene er ikke længere skrevet direkte i HTML'en. De er JSON leveret af et API og vises med en Jinja `for`-løkke.

![Forsiden med listen af indlæg][step-6]

```html
{% for post in posts %}
  <a href="{{ url_for('show_post', index=post.id) }}">
    <h2 class="post-title">{{ post.title }}</h2>
    <h3 class="post-subtitle">{{ post.subtitle }}</h3>
  </a>
  <p class="post-meta">Posted by {{ post.author }} on {{ post.date }}</p>
{% endfor %}
```

Data læses med standardbiblioteket (`urllib`), så projektet ikke behøver `requests`. Kan API'et ikke nås, bruges den kopi af eksempelindlæggene, der følger med pakken, så sitet og testene virker offline. Indlæggene fortolkes ét sted til en `Post`, og use casen `get_posts` giver dem videre til routen.

## Hvad vi har lært

- Punktum-notation i Jinja (`post.title`) er naturlig at læse; den samme løkke virker for et vilkårligt antal indlæg.
- At læse fra et API er en separat opgave: routen ved ikke, hvor indlæggene kommer fra, så testene injicerer et falsk repository.
- En fallback og en timeout (`REQUEST_TIMEOUT_SECONDS` i `constants.py`) holder siden i gang, når netværket ikke er det.

---

[step-6]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2/raw/branch/main/docs/screenshots/step-6-home-posts.png
