import os

print(os.path.join('rbd/123','TEMPLATES'))

{{ title }} | {{ site_title|default:_('Cual sera la diferencia (?)') }}


	<h1 id="site-name"><a href="{% url 'admin:index' %}">
	{{ site_header|default:_('Polls administration') }}</a>
	</h1>