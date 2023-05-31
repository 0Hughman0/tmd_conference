---
layout: page
title: Program
permalink: /program/
---

Quicklinks:

<a href="#monday">[Monday]</a> - <a href="#tuesday">[Tuesday]</a> - <a href="#wednesday">[Wednesday]</a> - <a href="#thursday">[Thursday]</a>

[\[Poster Session Program\]]({{ "/posters/" | relative_url }})

{% assign talkCountP = 0 %}
{% assign talkCountA = 0 %}
{% assign talkCountB = 0 %}
{% assign talkCountC = 0 %}
{% assign talkCountD = 0 %}

{% assign days = "Sunday;Monday;Tuesday;Wednesday;Thursday" | split: ";" %}
{% for day in days %}

# {{ day }}

<table>
	{% assign data_file = day | append: "_program" %}
	
	{% for item in site.data[data_file] %}
	<tr class="top-aligned">
	<td class="time-row"><b>{{ item.Time }}</b></td>
	{% case item.Type %}
		{% when "Rooms" %}
			{% include roomRow.html roomA=item.RoomA roomB=item.RoomB roomC=item.RoomC roomD=item.RoomD %}
		{% when "Breakfast", "Coffee", "Lunch", "Dinner", "Meal", "Other" %}
			{% include mealRow.html text=item.Text type=item.Type room=item.RoomA%}
		{% when "Plenary" %}
			{% include pleanaryRow.html day=day num=talkCountP time=item.Time room=item.RoomA text=item.Text speaker=item.SpeakerA title=item.TitleA abstract=item.AbstractA %}
			{% assign talkCountP = talkCountP | plus: 1 %}
		{% when "Invited" %}
			{% include speakerRow.html time=item.Time
									   day=day
									   numA=talkCountA speakerA=item.SpeakerA titleA=item.TitleA abstractA=item.AbstractA affiliationA=item.AffiliationA roomA=item.RoomA
									   numB=talkCountB speakerB=item.SpeakerB titleB=item.TitleB abstractB=item.AbstractB affiliationB=item.AffiliationB roomB=item.RoomA
									   numC=talkCountC speakerC=item.SpeakerC titleC=item.TitleC abstractC=item.AbstractC affiliationC=item.AffiliationC roomC=item.RoomA
									   numD=talkCountD speakerD=item.SpeakerD titleD=item.TitleD abstractD=item.AbstractD affiliationD=item.AffiliationD roomD=item.RoomA %}
			
			{% assign talkCountA = talkCountA | plus: 1 %}
			{% assign talkCountB = talkCountB | plus: 1 %}
			{% assign talkCountC = talkCountC | plus: 1 %}
			{% assign talkCountD = talkCountD | plus: 1 %}

		{% when "Poster Session" %}
			{% include posterRow.html %}
	{% endcase %}
	</tr>
	{% endfor %}
</table>

{% endfor %}

<script>
var main = document.getElementById("main");
main.onclick = mainHandleClick;

var displayed = new Set();

function showTalkInfo(id) {
	hideAll();
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

