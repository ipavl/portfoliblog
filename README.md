Portfoliblog
============

Portfoliblog is, as its name implies, both a portfolio and a blog. It is built with [Django](https://www.djangoproject.com).

Portfoliblog is currently intended for individuals, however it may also fit the needs of teams - small manual changes
may be required to add features such as multi-user blog post authoring for the moment in order to satisfy team needs.

Features
--------

* Basic Bootstrap theme to give a clean look yet not be too customized out of the box
* Write major content (blog posts, static pages, project descriptions) in Markdown
* Manage most content through Django admin (`/admin/`)
* Basic blogging features (currently no drafts, comments, or multiple authors)
* Consistent look across project details pages and an automatic project index page
* URL shortener

Getting Started
---------------

1. Change the timezone and locale as desired in `settings.py`
2. Create the database and tables: `manage.py migrate`
3. Create a superuser account: `manage.py createsuperuser`
4. Start the development server: `manage.py runserver`
