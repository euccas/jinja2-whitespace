from jinja2 import Template

my_template = """  First Line with indent 2
< blank >
Second Line
< blank >
==== Block 1 ====
{% if arg.third_line == True %}
Third Line
Third Line 222
{% endif %}
    **end line 1 with indent 4
==== End Block 1 ====
< blank >
==== Block 2 ====
{% for item in arg.block2 %}
{{ item }}
{% endfor %}
    **end line 2 with indent 4
==== End Block 2 ====
"""

t = Template(my_template, trim_blocks=True, lstrip_blocks=False)
my_arg = {}
my_arg["third_line"] = False
my_arg["block2"] = ["aa", "bbb", "cccc"]
result = t.render(arg=my_arg)

print(result)