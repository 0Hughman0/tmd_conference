---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
title: 2D Transition Metal Dichalcogenides 2023
sub_title: June 26 - 29, 2023 | Churchill College, Cambridge, UK
image: /assets/top_banner.jpg
introduction: |
    The conference will cover latest developments in synthesis of 2D TMDs and their 
    implementation in electronics, photonics, catalysis, as well as energy conversion 
    and storage. <b>Abstracts from students and postdoctoral researchers are very welcome.</b>
---
## Topics

<div class="topics-grid">
	<div>
	  <ul>
		{% for topic in site.data.topics limit:5 %}
		<li>
			{{ topic['name'] }}
		</li>
		{% endfor %}
  	  </ul>
	</div>
	<div>
	<ul>
		{% for topic in site.data.topics offset:5 %}
		<li>
			{{ topic['name'] }}
		</li>
		{% endfor %}
	</ul>
	</div>
</div>


## Confirmed Plenary Speakers

<div class="speaker-box">
{% for pair in site.data.plenaries %}

	<article class="portrait">
		<img src="{{ '/assets/Plenary Speakers/' | relative_url }}{{ pair['Name'] }}.jpg" height="200" width="200" style="border-radius: 50%">
        <b>{{ pair["Name"] }}</b>
        <em>{{ pair["Institute"] }}</em>
	</article>
{% endfor %}
</div>


## Organizers
<div class="speaker-box">
{% for pair in site.data.organizers %}

	<article class="portrait">
		<img src="{{ '/assets/organizers/' | relative_url }}{{ pair['Name'] }}.jpg" height="200" width="200" style="border-radius:50%">
        <b>{{ pair["Name"] }}</b>
        <em>{{ pair["Institute"] }}</em>
	</article>
{% endfor %}
</div>
