---
layout: page
title: Invited Speakers
permalink: /speakers/
---

<div class="entries-grid">
{% for pair in site.data.2D_Conference %}

	<article class="entry">
		<img src="{{ '/assets/Invited Speakers/Accepted/' | relative_url }}{{ pair['Name'] }}.jpg" height="200" width="200" style="border-radius:50%">
        <em>{{ pair["Name"] }}</em>
        <em>{{ pair["Institute"] }}</em>
	</article>

{% endfor %}
</div>


<style>
    tab1 { padding-left: 4em; }
</style>
## Contact us
<div class="entries-grid">
	<article class="entry">
		<p>
			<a href="www.2dtmds2023.com">www.2dtmds2023.com</a>

		</p>
		
		
	</article>
	<article class="entry">
		<p>
			Email: 2dtmds2023@msm.cam.ac.uk

		</p>
		
	</article>
	<article class="entry">
		<p>
			Address: Churchill College<br>
			<tab1>University of Cambridge</tab1><br>
			<tab1>Storey's Way</tab1><br>
			<tab1>Cambridge</tab1><br>
			<tab1>UK Postcode: CB3 0DS</tab1><br>

		</p>
		
		
	</article>
	
</div>