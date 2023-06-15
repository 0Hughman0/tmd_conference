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
    and storage.
---

<div style="display:flex;flex-wrap:wrap">
	<div style="flex-grow:1">
	
	<h2>Topics</h2>

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


	<h2>Confirmed Plenary Speakers</h2>

	<div class="speaker-box">
	{% for pair in site.data.plenaries %}

		<article class="portrait">
			<img src="{{ '/assets/Plenary Speakers/' | relative_url }}{{ pair['Name'] }}.jpg" class="portrait">
			<b>{{ pair["Name"] }}</b>
			<em>{{ pair["Institute"] }}</em>
		</article>
	{% endfor %}
	</div>


	<h2>Organizers</h2>
	<div class="speaker-box">
	{% for pair in site.data.organizers %}

		<article class="portrait">
			<img src="{{ '/assets/organizers/' | relative_url }}{{ pair['Name'] }}.jpg" class="portrait">
			<b>{{ pair["Name"] }}</b>
			<em>{{ pair["Institute"] }}</em>
		</article>
	{% endfor %}
	</div>

	<h2>Sponsors</h2>

	{% assign sponsors = "Aixtron.svg;attocube.jpg;HeidelbergInstruments.png;HenryRoyceInstitute.png;OxfordInstruments.png;Royal Society of Chemistry.png" | split: ";"  %}

	<div class="tmd-sponsors">
		{% for logoName in sponsors %}
		<article class="tmd-sponsors">
			<img src="{{ '/assets/sponsors/' | relative_url }}{{logoName}}" class="logo">
		</article>
		{% endfor %}
	</div>

</div>
<div style="flex-align:flex-right;max-width:30%">
	<h2>Latest Updates:</h2>

	<a class="twitter-timeline" href="https://twitter.com/2D_TMDs_2023?ref_src=twsrc%5Etfw">Tweets by 2D_TMDs_2023</a> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 

</div>
