---
layout: page
title: Invited Speakers
permalink: /speakers/
---

<div class="entries-grid">
{% for pair in site.data.2D_Conference %}

	<article class="entry">
		<img src="/assets/Invited speakers/Accepted/{{ pair["Name"] }}.jpg" height="200" width="200" style="border-radius:50%">
        <em>{{ pair["Name"] }}</em>
        <em>{{ pair["Institute"] }}</em>
	</article>

{% endfor %}
</div>


