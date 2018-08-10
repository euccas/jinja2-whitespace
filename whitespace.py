from jinja2 import Template

my_template = """  First Line with indent 2
Second Line
==== Block 1 ====
==== End Block 1 ====
< blank >
==== Block 2 ====
==== End Block 2 ====
"""

t = Template(my_template)
my_arg = {}
result = t.render(arg=my_arg)

print(result)