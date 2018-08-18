import logging

from IPython.display import display, HTML, JSON, Image, SVG, Latex, Markdown
from IPython.core.magic import Magics, magics_class, cell_magic

import pystache


@magics_class
class MagicMarkdown(Magics):
    """
    Markdown cell_magic with python statements in mustache syntax.
    The result is cast to string. If it is Markdown or HTML (from IPython.display) 
    E.g ### The 
    somehow this should magically use Markdown, HTML, Image, Latex, or from set of Display classes.
    """
    def __init__(self, shell=None,  **kwargs):
        super().__init__(shell=shell, **kwargs)
        self._store = []
        self.logger = logging.getLogger(__name__)
        if not self.logger.hasHandlers():
            self.logger.addHandler(logging.StreamHandler())        
        self.logger.setLevel(logging.WARNING)
        self.shell = shell


    def eval_or_error(self, statement):
        res = eval(statement, self.shell.user_ns)
        try:
            res = eval(statement, self.shell.user_ns)
        except:
            self.logger.warning('eval_or_error: %s' %(statement))
            res = ''
        finally:
            self.logger.debug('eval_or_error: %s' %(res))
            return res
           
            
    def string_o_eval(self, statement, no_string= False):
        is_str = True
        if isinstance(statement, str) and not no_string:
            return statement, is_str
        # here add a try/except block. and display some red block around the code block
        self.logger.debug('evaling block: %s' % (statement))
        self.logger.handlers[0].flush()
        res = self.eval_or_error(statement.key)
        
        if type(res) in [HTML, JSON, Image, SVG, Latex, Markdown]:
            s_res = res
            is_str = False
        elif isinstance(res, str):
            s_res = res
        else:
            try:
                s_res = str(res)
            except:
                self.logger.warning("can't convert expression to string")
                self.logger.flush()
                if res.key:
                    s_res = res.key 
        return s_res, is_str


    @cell_magic
    def mmd(self, line, cell):
        self._store.append(cell)
        parsed = pystache.parse(cell)
        act_chunk = []
        token_chunks = [act_chunk]
        for stmt in parsed._parse_tree:
            token, is_str = self.string_o_eval(stmt)
            if is_str:
                act_chunk.append(token)
            else:
                token_chunks.append(token)
                act_chunk = []
                token_chunks.append(act_chunk)
        for chunk in token_chunks:
            if isinstance(chunk, list):
                if len(chunk) > 0:
                    display(Markdown(''.join(chunk)))
            else:
                display(chunk)
        return None 
