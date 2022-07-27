---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
title: 2D Transition Metal Dichalcogenides & Related Materials
sub_title: June 26 – 29, 2023 | Churchill College, Cambridge, UK
image: /assets/top_banner.png

introduction: |
    The conference will cover latest developments in synthesis of 2D TMDs and their 
    implementation in electronics, photonics, catalysis, as well as energy conversion 
    and storage. 
---

## Topics

<div class="entries-grid">
	<article class="entry">
		<h1 class="entry-title">
			Wafer scale synthesis of TMDs

		</h1>
		
	</article>
	<article class="entry">
		<h1 class="entry-title">
			2D TMDs for novel logic, memory and interconnects

		</h1>
		
	</article>
	<article class="entry">
		<h1 class="entry-title">
			2D TMDs for excitonic, plasmonic and other photonic devices

		</h1>
		
	</article>
	<article class="entry">
		<h1 class="entry-title">
			Van der Waals heterostructures of TMDs

		</h1>
		
	</article>
	<article class="entry">
		<h1 class="entry-title">
			Engineering quantum states in 2D TMDs and sensing with them

		</h1>
		
	</article>
	<article class="entry">
		<h1 class="entry-title">
			2D TMDs for energy conversion and storage 

		</h1>
		
	</article>
	<article class="entry">
		<h1 class="entry-title">
			Defect engineering and catalysis with 2D TMDs

		</h1>
		
	</article>
	<article class="entry">
		<h1 class="entry-title">
			Imaging and characterization

		</h1>
		
	</article>
	
</div>


## Plenary Speakers
<div class="entries-grid">
{% for pair in site.data.plenaries %}

	<article class="entry">
		<img src="/assets/Plenary Speakers/{{ pair["Name"] }}.jpg" height="200" width="200" style="border-radius:50%">
        <em>{{ pair["Name"] }}</em>
        <em>{{ pair["Institute"] }}</em>
	</article>
{% endfor %}
</div>

