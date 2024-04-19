Control who can view your djangocms blog posts

----

## Install

* Install the package
    ```bash
    python3 -m pip install djangocms-blog-view-restrictions
    ```

* Add it in your `INSTALLED_APPS`:
    ```python

        "djangocms_blog_view_restrictions",
    ```

* Run the migration:
    ```sh
    python3 manage.py migrate djangocms_blog_view_restrictions
    ```

## Usage

When creating/editing a blog post, a new "View restriction" section allows you to define multiple users/groups that are allowed to view the post.
The user is allowed to view the post if any of the restrictions are met.

You are then responsible to hide partially or totally the post's content in your `djangocms_blog/post_detail.html` template:
```html
{% extends "djangocms_blog/post_detail.html" %}
{% load blog_view_restrictions_tags %}


{% block content_blog %}
  <article>
    {{ post.abstract }}

    {% if request.user|can_view_post:post %}
      {% if post.app_config.use_placeholder %}
        <div class="blog-content">{% render_placeholder post.content %}</div>
      {% else %}
        <div class="blog-content">{% render_model post "post_text" "post_text" "" "safe" %}</div>
      {% endif %}
    {% else %}
      This post is for subscribers only.
    {% endif %}

    ...

  </article>
{% endblock content_blog %}
```
