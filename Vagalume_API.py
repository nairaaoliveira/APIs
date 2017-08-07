<!DOCTYPE html>
<HTML>
<head>
	<title>Vagalume API Example</title>
	<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
</head>
<style>
	#aprox {color:black;font-weight:bold;padding:10px 0}
</style>
<BODY>
	<h1>Lyrics API example</h1>
	<div style='width:500px'>
		<p>This example is using <a href='http://api.jquery.com/jQuery.getJSON/'>getJSON</a> to fetch <a href='http://api.vagalume.com.br/docs/letras/'>lyrics from Vagalume</a>. It's a very complete example 
		using jQuery, but you can make any change you want to match your needs. It's important to keep Vagalume logo and link on your webpage.</p>
		<p>Artist and Song name are static on this page, which you could generate from your favourite programming language or even change this code
		to fech this data somewhere else.</p>

		<!--- Here you can specify the artist and music to fetch -->
		<span style='color:green'>
			<b>Artist:</b> <i id='artista'>Madonna</i> /
			<b>Song:</b> <i id='music'>Holiday</i>
		</span>

		<!--- Where lyrics should be placed. Don't remove Vagalume logo and link. -->
		<a target=_blank style='float:right;font-size:10px;color:#000;text-decoration:none;font-weight:bold' href="http://www.vagalume.com.br/"><img border=0 src="http://www.vagalume.com.br/images/logo_small2.jpg" alt="Vagalume"><br/>Letras de Músicas</a>
		<div id='letra' style='width:400px;text-align:left'>
			<pre class=text>Fetching lyrics... <img src="http://www.vagalume.com.br/images/processing.gif"></pre>
		</div>
		<a target=_blank id=vagalumeBrandBottom href="http://www.vagalume.com.br/search.php?t=art&q=Madonna">More about Madonna at Vagalume &raquo;</a>
	</div>
	<script>
		/* EXAMPLE CODE USING VAGALUME API (Lyrics)
		You can make any modifications to this code.
		Please read API Terms at api.vagalume.com.br/terms/
		IMPORTANT: VAGALUME LOGO AND LINK MUST BE PRESENT ON THE PAGE
		Copyright Vagalume Midia Ltda. All rights reserved.
		Permission is hereby granted, free of charge, to any person obtaining a copy
		of this software and associated documentation files (the "Software"), to
		deal in the Software without restriction, including without limitation the
		rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
		sell copies of the Software, and to permit persons to whom the Software is
		furnished to do so, subject to the following conditions:
		The above copyright notice and this permission notice shall be included in
		all copies or substantial portions of the Software.
		THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
		IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
		FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
		AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
		LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
		FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
		IN THE SOFTWARE.
		*/
		function showLetra (data,art,mus,arrayid) {
			if (! arrayid) arrayid = 0;
			if (data.type == 'exact' || data.type == 'aprox') {
				// Print lyrics text
				$('#letra .text').text(data.mus[arrayid].text);
				// Show buttons to open original and portuguese translation
				if (data.mus[arrayid].translate) {
					$('#letra .text').prepend('<input type=button value="Portuguese &raquo;" onClick="$(document).trigger(\'translate\')"><br/>');
					$(document).one('translate',function() {
						$('#letra .text').text(data.mus[arrayid].translate[0].text);
						$('#letra .text').prepend('<input type=button value="&laquo; Original" onClick="$(document).trigger(\'original\')"><br/>');
						$(document).one('original',function() {
							showLetra(data,art,mus,arrayid);
						});
					});
				}
				// If not exact match (ex: U2 / Beautiful)
				if (data.type == 'aprox' && !$('#aprox').is('div')) {
					$('#letra').prepend('<div id=aprox>We found something similar<br/><span class=songname>"' + data.mus[arrayid].name + '"</span></div>');
					// If Vagalume found more than one possible matches
					if (data.mus.length > 0) {
						var html = '<select class=songselect>';
						for (var i = 0; i < data.mus.length; i++) {
							html += '<option value="'+i+'"'+(i==arrayid?' selected':'')+'>'+data.mus[i].name+'</option>';
						}
						html += '</select>';
						$('#aprox span.songname').html(html);
						$('#aprox select.songselect').change(function() {
							var aID = $('option:selected',this).val();
							showLetra (data,art,mus,aID);
						});
					}
				}
			} else if (data.type == 'song_notfound') {
				// Song not found, but artist was found
				// You can list all songs from Vagalume here
				$('#letra .text').html(
					'Song "'+mus+'" from "'+art+'" was not found.<br/>'
					+'<a target=_blank href="http://www.vagalume.com.br/add/lyrics.php">'
					+'Add this song to Vagalume &raquo;</a>'
				);
			} else {
				// Artist not found
				$('#letra .text').html(
					'Song "'+mus+'" from "'+art+'" was not found<br/>'
					+'(artist not found)<br/>'
					+'<a target=_blank href="http://www.vagalume.com.br/add/lyrics.php">'
					+'Add this song to Vagalume &raquo;</a>'
				);
			}
		}
		function fetchLetra (art,mus) {
			var data = jQuery.data(document,art + mus); // cache read
			if (data) {
				showLetra(data, art, mus);
				return true;
			}
			var url = "http://api.vagalume.com.br/search.php"
				+"?art="+encodeURIComponent(art)
				+"&mus="+encodeURIComponent(mus);
			// Check if browser supports CORS - http://www.w3.org/TR/cors/
			if (!jQuery.support.cors) {
				url += "&callback=?";
			}
			jQuery.getJSON(url,function(data) {
				// What we do with the data
				jQuery.data(document,art + mus,data); // cache write
				showLetra(data, art, mus);
			});
		}
		// Just an example of how you can call this using elements on the page
		fetchLetra($("#artista").text(),$("#music").text());
	</script>
</BODY>
</HTML>