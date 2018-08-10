from jinja2 import Template

my_template = """  First Line with indent 2
Second Line
==== Block 1 ====
{% for item in arg.block2 %}
{{ item }}
{% endfor %}
==== End Block 1 ====
"""

t = Template(my_template)
my_arg = {}
my_arg["block2"] = ["aa", "bbb", "cccc"]
result = t.render(arg=my_arg)

print(result)