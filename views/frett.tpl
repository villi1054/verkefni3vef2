<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Hasarfréttir</title>
	<link rel="stylesheet" type="text/css" href="static/styles.css">
</head>
<body>
	% include ('haus.tpl')

	<div class="row">
		<section><h3>{{frett[0]}}</h3></section>
		<section>
			<img src="/static/mynd{{nr}}.jpg"> </img>
		</section>
		<section> 
		<p>{{frett[1]}}</p>
		<p>Höfundur: {{frett[3]}}</p>
		</section>
	</div>

	% include ('foot.tpl')
</body>
</html>
