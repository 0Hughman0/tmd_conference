---
layout: page
permalink: /posters/
title: Poster Program
---


<table>
	<tr>
		<th>Poster</th>
		<th>Info</th>
		<th style="width:10%">Keywords</th>
	</tr>	
	{% for item in site.data.Posters_program %}
	<tr class="top-aligned">
		<td class="time-row"><b>{{ forloop.index }}</b></td>
		<td>
			{% include talkInfo.html time="19:30 - 21:00" room="TBC" speaker=item.Name title=item.Title abstract=item.Abstract %}
		</td>
		<td>"{{ item.Keywords | split: ";" | join: '", "' }}"</td>
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

