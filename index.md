---
layout: default
title: Home
---

<h1>{{ site.title }}</h1>
<p>{{ site.description }}</p>

{% assign all_til = site.os | concat: site.network | concat: site.database | concat: site.datastructure | concat: site.algorithm %}
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
