{% extends 'base.html' %}
{% load markdown_helper %}

{% block title %}Welcome{% endblock %}

{% block content %}
{% filter markdownify %}
This is your homepage. You can edit its content by changing the *content* block of `common/templates/common/index.md`.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque sit amet posuere elit. Suspendisse nisl enim,
semper sit amet ex eget, ultrices egestas ex. Ut ac orci ac lorem volutpat vestibulum. Donec non mattis nibh. Donec
turpis leo, mollis at magna eget, iaculis ultrices enim. Cras commodo, orci vel rutrum vehicula, ex nulla
tinciduntrisus, vel elementum justo nisl id augue. Fusce non enim faucibus, blandit massa nec, bibendum erat. Maecenas
pharetra et metus ac cursus. Pellentesque tempor accumsan enim, feugiat suscipit arcu vulputate ac. Praesent vehicula,
ligula quis ultricies convallis, nulla felis aliquam arcu, eget vulputate urna nisl in lacus. Sed ipsum dui, condimentum
at ultricies et, vulputate sed metus. Nullam vel ipsum convallis, eleifend ante et, eleifend enim.

Duis eu dui ac arcu consectetur viverra. Etiam rutrum dictum nulla ut mollis. Cras tempus, purus nec vehicula
consectetur, nibh diam ullamcorper ipsum, at consectetur quam dui ac nibh. Nam eget ipsum purus. Aliquam id leo
pharetra, aliquam risus nec, tempus odio. Nam ultricies congue neque vel semper. Proin vulputate diam eget quam
condimentum, ac mattis turpis malesuada.
{% endfilter %}
{% endblock %}