<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Hasarfréttir</title>
	<link rel="stylesheet" type="text/css" href="static/styles.css">
</head>
<body>
	%include ('haus.tpl')

	<div class="row">
		<section>{{frettir[0][0]}}</section>
		<section><h3>Nýjustu fréttir</h3></section>
		<section>
			<img src="/static/mynd0.jpg"> </img>
		</section>
		<section> 
		<ul>
			% cmt = 0;
			% for i in frettir:
				<li>
					<h4><a href="/frett/{{cmt}}">{{i[0]}}</a></h4>
				</li>
				% cmt +=1
			% end
		</ul> </section>
	</div>

	%include ('foot.tpl')
</body>
</html>