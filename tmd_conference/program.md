---
layout: page
title: Program
permalink: /program/
---

# Monday

<table>
	{% for item in site.data.program_monday %}
	<tr>
	<td><b>{{ item.Time }}</b></td>
	{% case item.Type %}
		{% when "Breakfast", "Coffee", "Lunch", "Dinner", "Meal" %}
			{% include mealRow.html text=item.Text type=item.Type %}
		{% when "Plenary" %}
			{% include pleanaryRow.html text=item.Text speaker=item.SpeakerA title=item.TitleA %}
		{% when "Invited" %}
			{% include speakerRow.html speakerA=item.SpeakerA titleA=item.TitleA speakerB=item.SpeakerB titleB=item.TitleB speakerC=item.SpeakerC titleC=item.TitleC %}
	{% endcase %}
	</tr>
	{% endfor %}
</table>
