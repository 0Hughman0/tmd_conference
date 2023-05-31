---
layout: page
title: Program
permalink: /program/
---

Quicklinks:

<a href="#monday">[Monday]</a> - <a href="#tuesday">[Tuesday]</a> - <a href="#wednesday">[Wednesday]</a> - <a href="#thursday">[Thursday]</a>

[\[Poster Session Program\]]({{ "/posters/" | relative_url }})

# Monday

<table>
	{% for item in site.data.Monday_program %}
	<tr class="top-aligned">
	<td class="time-row"><b>{{ item.Time }}</b></td>
	{% case item.Type %}
		{% when "Rooms" %}
			{% include roomRow.html roomA=item.RoomA roomB=item.RoomB roomC=item.RoomC roomD=item.RoomD %}
		{% when "Breakfast", "Coffee", "Lunch", "Dinner", "Meal" %}
			{% include mealRow.html text=item.Text type=item.Type %}
		{% when "Plenary" %}
			{% include pleanaryRow.html time=item.Time room=item.RoomA text=item.Text speaker=item.SpeakerA title=item.TitleA abstract=item.AbstractA %}
		{% when "Invited" %}
			{% include speakerRow.html time=item.Time
									   speakerA=item.SpeakerA titleA=item.TitleA abstractA=item.AbstractA affiliationA=item.AffiliationA roomA=item.RoomA
									   speakerB=item.SpeakerB titleB=item.TitleB abstractB=item.AbstractB affiliationB=item.AffiliationB roomB=item.RoomA
									   speakerC=item.SpeakerC titleC=item.TitleC abstractC=item.AbstractC affiliationC=item.AffiliationC roomC=item.RoomA
									   speakerD=item.SpeakerD titleD=item.TitleD abstractD=item.AbstractD affiliationD=item.AffiliationD roomD=item.RoomA %}
		{% when "Poster Session" %}
			{% include posterRow.html %}
	{% endcase %}
	</tr>
	{% endfor %}
</table>

# Tuesday

<table>
	{% for item in site.data.Tuesday_program %}
	<tr class="top-aligned">
	<td class="time-row"><b>{{ item.Time }}</b></td>
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

# Wednesday

<table>
	{% for item in site.data.Wednesday_program %}
	<tr class="top-aligned">
	<td class="time-row"><b>{{ item.Time }}</b></td>
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

# Thursday

<table>
	{% for item in site.data.Thursday_program %}
	<tr class="top-aligned">
	<td class="time-row"><b>{{ item.Time }}</b></td>
	{% case item.Type %}
		{% when "Breakfast", "Coffee", "Lunch", "Dinner", "Meal" %}
			{% include mealRow.html type=item.Type text=item.Text room=item.RoomA %}
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
var main = document.getElementById("main");
main.onclick = mainHandleClick;

var displayed = new Set();

function showTalkInfo(id) {
	var el = document.getElementById(id);
	el.style.display= "block";
	displayed.add(el);
}
function hideTalkInfo(id) {
	var el = document.getElementById(id);
	el.style.display = "none";
	displayed.delete(el);
}
function hideAll() {
	for (const el of displayed) {
		el.style.display = "none";
	}
	displayed.clear();
}
function mainHandleClick(event) {
	hideAll();
}

document.addEventListener('keydown', (event) => {switch (event.keyCode) {case 27: hideAll()}})

</script>

