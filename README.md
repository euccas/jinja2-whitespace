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



