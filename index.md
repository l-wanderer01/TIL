---
layout: default
title: Home
---

<h1>{{ site.title }}</h1>
<p>{{ site.description }}</p>

{% assign all_til = "" | split: "" %}
{% for c in site.collections %}
  {% unless c[0] == "posts" %}
    {% assign all_til = all_til | concat: c[1].docs %}
  {% endunless %}
{% endfor %}
{% assign sorted_til = all_til | sort: "date" | reverse %}

<ul>
{% for item in sorted_til %}
  <li>
    <strong>[{{ item.category }}]</strong>
    <a href="{{ item.url | relative_url }}">{{ item.title }}</a>
    <span>({{ item.date | date: "%Y-%m-%d" }})</span>
  </li>
{% endfor %}
</ul>
