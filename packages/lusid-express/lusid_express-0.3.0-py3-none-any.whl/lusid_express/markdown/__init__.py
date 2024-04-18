from IPython.display import Markdown as render_markdown
import os as __os
import json as __json
with open(__os.path.join(__os.path.dirname(__file__), 'PRELOADED_VARS.md'), 'r') as __f:
    PRELOADED_VARS_MARKDOWN = __f.read()
    
def display_preloaded_var_markdown():
    """
    Displays the preloaded variables Markdown file.
    """
    return render_markdown(PRELOADED_VARS_MARKDOWN)


def data_to_markdown(data, col_name_key="Key", col_name_value="Value", title="table"):
    """
    Converts a JSON string or dictionary to a Markdown table.
    
    Parameters:
        data (str or dict): JSON string or dictionary containing the data.
        col_name_key (str): Custom name for the column header of the keys.
        col_name_value (str): Custom name for the column header of the values.
        title (str): Title of the table.
    
    Returns:
        str: A Markdown-formatted string representing the table.
    """
    # Parse the JSON string into a dictionary if data is a string
    if isinstance(data, str):
        try:
            data = __json.loads(data)
        except __json.JSONDecodeError:
            raise ValueError("Invalid JSON string provided.")
    
    # Ensure data is a dictionary
    if not isinstance(data, dict):
        raise TypeError("Data must be a dictionary or a JSON string representing a dictionary.")
    
    # Start building the Markdown table
    markdown_table = f"{col_name_key} | {col_name_value}\n"  # Table headers
    markdown_table += "---|---\n"  # Separator line for Markdown table
    
    # Add each key-value pair as a row in the table
    for key, value in data.items():
        # Ensure the value is converted to a string if necessary
        markdown_table += f"{key} | {str(value)}\n"
    
    return f"## {title}\n{markdown_table}"