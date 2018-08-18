name = "magic_markdown"

from magic_markdown.MagicMarkdown import MagicMarkdown

def load_ipython_extension(ipython):
    ipython.register_magics(MagicMarkdown)
