IPython cell magic with the `%%mmd` command allows to include python expressions (and other things) in a markdown text.
The cells can be edited as markdown, python expression are indicated by the double mustaches. 

[See the notebook example](https://github.com/transfluxus/magic_markdown/blob/master/example/magic_markdown_test.ipynb)

## Install

`pip install magic-markown`

in your notebook:

`%load_ext magic_markdown`

then you can create magic markdown cells by beginning a cell like this:
`%%mmd`

Write markdown and insert python code whereever you need: {{"hello".upper()}}. You can also access variables and functions you defined or imported before. [Checkout the full example.](https://github.com/transfluxus/magic_markdown/blob/master/example/magic_markdown_test.ipynb)
