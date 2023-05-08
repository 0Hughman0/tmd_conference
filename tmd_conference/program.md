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
			{% include pleanaryRow.html text=item.Text speaker=item.SpeakerA title=item.TitleA abstract=item.AbstractA %}
		{% when "Invited" %}
			{% include speakerRow.html speakerA=item.SpeakerA titleA=item.TitleA abstractA=item.AbstractA
									   speakerB=item.SpeakerB titleB=item.TitleB abstractB=item.AbstractB
									   speakerC=item.SpeakerC titleC=item.TitleC abstractC=item.AbstractC
									   speakerD=item.SpeakerD titleD=item.TitleD abstractD=item.AbstractD %}
		{% when "Poster Session" %}
			{% include mealRow.html text=item.Text type=item.Type %}
	{% endcase %}
	</tr>
	{% endfor %}
</table>

<script>
function showTalkInfo(id) {
	var el = document.getElementById(id);
	el.style.display= "block";
}
function hideTalkInfo(id) {
	var el = document.getElementById(id);
	el.style.display= "none";
	
}
</script>

