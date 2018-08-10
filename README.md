# Jinja2 White Space Control Examples

## Jinja2 Document

http://jinja.pocoo.org/docs/2.10/templates/

If an application configures Jinja to ```trim_blocks```, the first newline after a template tag is removed automatically (like in PHP). The ```lstrip_blocks``` option can also be set to strip tabs and spaces from the beginning of a line to the start of a block. (Nothing will be stripped if there are other characters before the start of the block.)

You can also strip whitespace in templates by hand. If you add a minus sign (-) to the start or end of a block (e.g. a For tag), a comment, or a variable expression, the whitespaces before or after that block will be removed:

```
{% for item in seq -%}
    {{ item }}
{%- endfor %}
```

This will yield all elements without whitespace between them. If seq was a list of numbers from ```1``` to ```9```, the output would be ```123456789```.

## Control the white spaces

* If start the template from a new line after the raw string start quotes ```"""```, the rendered result will have one extra blank line in the beginning.

```
my_template = """
  First Line with indent 2"""
t = Template(my_template)
t.render()
```

Result is:
```
>>> render.py

  First Line with indent 2
```

* If start the template right after the raw string quotes ```"""```, there will be no extra new line in the beginning.

```
my_template = """  First Line with indent 2"""
t = Template(my_template)
t.render()
```

Result is:
```
>>> render.py
  First Line with indent 2
```

* When trim_blocks is set to False (by default), template tags such as "if", "for" will generate a blank line. To the "for" loop, the blank line is added to every statement into the for loop.

if statement:
```
my_template = """  First Line with indent 2
Second Line
==== Block 1 ====
{% if arg.third_line == True %}
Third Line
Third Line 222
{% endif %}
    **end line 1 with indent 4
==== End Block 1 ====
"""
my_template = """  First Line with indent 2"""
t = Template(my_template)
my_arg = {}
t.render(arg = my_arg)
```

Result is:
```
  First Line with indent 2
Second Line
==== Block 1 ====

    **end line 1 with indent 4
==== End Block 1 ====
```

for statement:
```
my_template = """  First Line with indent 2
Second Line
==== Block 1 ====
{% for item in arg.block2 %}
{{ item }}
{% endfor %}
    **end line 1 with indent 4
==== End Block 1 ====
"""
t = Template(my_template)
my_arg = {}
my_arg["block1"] = ["aa", "bbb", "cccc"]
t.render(arg = my_arg)
```

Result:
```
  First Line with indent 2
Second Line
==== Block 1 ====

aa

bbb

cccc

==== End Block 1 ====
```

* When ```trim_blocks``` is set to True, no extra blank lines will be added in the ```if``` or ```for``` blocks.

for statement:
```
my_template = """  First Line with indent 2
Second Line
==== Block 1 ====
{% for item in arg.block2 %}
{{ item }}
{% endfor %}
    **end line 1 with indent 4
==== End Block 1 ====
"""
t = Template(my_template)
my_arg = {}
my_arg["block1"] = ["aa", "bbb", "cccc"]
t.render(arg = my_arg)
```

Result:
```
  First Line with indent 2
Second Line
==== Block 1 ====
aa
bbb
cccc
==== End Block 1 ====
```

* The minus sign "-" can be used to fine tune the white spaces.

```
my_template = """  First Line with indent 2
Second Line
==== Block 1 ====
{% for item in arg.block2 -%}
{{ item }}
{%- endfor %}
    **end line 1 with indent 4
==== End Block 1 ====
"""
t = Template(my_template)
my_arg = {}
my_arg["block1"] = ["aa", "bbb", "cccc"]
t.render(arg = my_arg)
```

Result:
```
  First Line with indent 2
Second Line
==== Block 1 ====
aabbbcccc
==== End Block 1 ====
```

