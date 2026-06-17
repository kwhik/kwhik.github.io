---
layout: page
title: About
permalink: /about/

---

kWhik produces solutions to enable you to harness the energy of the sun inexpensively and quickly.

## Translation and Terminology

This site is written in American English with electrical terminology commonly used in the United States.  The narrative and expository can be translated to other languages with various levels of success through Google Translate (see below) or browser capabilities, but the terminology translation is beyond these tools.   Apologies for any difficulties this cause.

Switch site from
<span class="notranslate">&nbsp;<a onclick="location.href='{{site.url}}{{page.url}}'" class="notranslate">EN</a>&nbsp;</span> 
to:
<span class="notranslate">
&nbsp;{% for item in site.languages -%}
<a onclick="location.href='https://kwhik-com.translate.goog{{page.url}}?_x_tr_sl=auto&_x_tr_tl={{item}}'" class="notranslate">{{item}}</a>
{% if forloop.last -%}
{% else -%}
•
{% endif -%}
{% endfor -%}
</span>
