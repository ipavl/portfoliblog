{% extends 'base.html' %}
{% load markdown_helper %}

{% block title %}About{% endblock %}

{% block content %}
{% filter markdownify %}
This is your about page. You can change it by editing the `common/templates/common/about.md` file.
{% endfilter %}
{% endblock %}