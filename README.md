IPython cell magic with the '%%mmd' command allows to include python expressions (and other things) in a markdown text.
The cells can be edited as markdown, python expression are indicated by the double mustaches. 
```
This is markdown with some python stuff. simply put a python expression into a double mustache: {{5+10}}.
```

The cell is interpreted as Markdown, so html will naturally work.<br>
<b>some bold  text!</b>

```
	The cell is interpreted as Markdown and html will naturally work.<br>
	<b>some bold  text!</b>
```

Additionally some of the other types that are defined in IPython.display can be used (after import). Namely:
 - HTML
 - JSON 
 - Image
 - SVG
 - Latex
 - Markdown

```    
	That means whenever your python expression return an element of these types they are inlcuded in their typical IPython fashion.
	{{
	    JSON({"a":10, "b":[1,4,5]})
	}}

	<br><br>

	For LaTeX all \ have to be escaped:
	    
	{{Latex("\\begin{align}F(x) &= \\int^a_b\\frac{x^2}{5} \\end{align}")}}
```