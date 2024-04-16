from IPython.display import Markdown as render_markdown
import os as __os
with open(__os.path.join(__os.path.dirname(__file__), 'PRELOADED_VARS.md'), 'r') as __f:
    PRELOADED_VARS_MARKDOWN = __f.read()
    
def display_preloaded_var_markdown():
    return render_markdown(PRELOADED_VARS_MARKDOWN)