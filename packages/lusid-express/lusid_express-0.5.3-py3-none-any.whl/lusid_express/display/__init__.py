from IPython.display import Markdown as render_markdown, HTML as render_html
import os as __os
import json as __json

with open(__os.path.join(__os.path.dirname(__file__), "PRELOADED_VARS.md"), "r") as __f:
    PRELOADED_VARS_MARKDOWN = __f.read()


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
    data = __convert_data(data)

    # Start building the Markdown table
    markdown_table = f"{col_name_key} | {col_name_value}\n"  # Table headers
    markdown_table += "---|---\n"  # Separator line for Markdown table

    # Add each key-value pair as a row in the table
    for key, value in data.items():
        # Ensure the value is converted to a string if necessary
        markdown_table += f"{key} | {str(value)}\n"

    return f"## {title}\n{markdown_table}"


STYLES = {
    "table": """
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&display=swap');

:root {
    --main-color: #00B6DA; /* Light theme color */
    --table-color: #065F82; /* Light theme table color */
    --accent-color: #FF5500; /* Light theme accent color */
    --foreground-color: #777777; /* Light theme background */
}

@media (prefers-color-scheme: dark) {
    :root {
        --main-color: #0094AC; /* Dark theme color */
        --table-color: #043A4A; /* Dark theme table color */
        --accent-color: #E76F00; /* Dark theme accent color */
        --foreground-color: #777777; /* Dark theme background */
    }
}

body, h1, h2, h3, p {
    font-family: 'Montserrat';
}
table {

    margin-left: 2px;
    margin-right: 2px;
    border-collapse: collapse;
    text-align: center;
    color: #065F82;
    border: 2px solid #ccc; /* Add border */
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); /* Add drop shadow */
    font-weight: semi-bold;
}
h1 {
    font-size: 15px;
    line-height: 30px;
    font-weight: bold;

    color: #00B6DA;
}
h2 {
    font-size: 12px;
    line-height: 16px;
    font-weight: bold;
    
  color: var(--foreground-color);

}
h3 {
    font-size: 12px;
    line-height: 12px;
    font-weight: 600;
    text-align: start
color: var(--foreground-color);

}
p {
    font-size: 12px;
    line-height: 12px;
    font-weight: 500;
color: var(--foreground-color);

}
th, td {
    height: 15px; /* Fixed height for all rows */


}
th h2, td h3, td p {
    margin: 0;     /* Remove margin from cell contents */
    padding: 5px;  /* Reduce padding */
    text-align: left; 
    white-space: nowrap; /* Prevent text wrapping */
}

tr:nth-child(even) td {
    border-color: #FF5500;
    color: #FF5500
}
    tr:nth-child(odd) td {
    border-color: #415464;
    color: #FF5500;
}

</style>
"""
}

def __convert_data(data):
    """
    Converts a JSON string to a dictionary if necessary.

    Parameters:
        data (str or dict): JSON string or dictionary containing the data.

    Returns:
        dict: The data as a dictionary.
    """
    # Parse the JSON string into a dictionary if data is a string
    if isinstance(data, str):
        try:
            data = __json.loads(data)
        except __json.JSONDecodeError:
            raise ValueError("Invalid JSON string provided.")

    # Ensure data is a dictionary
    if not isinstance(data, dict):
        raise TypeError(
            "Data must be a dictionary or a JSON string representing a dictionary."
        )

    return data


def data_to_html(data, col_name_key="Key", col_name_value="Value", title="table"):
    """
    Returns table HTML representation.

    Parameters:
        data (str or dict): JSON string or dictionary containing the data.
        col_name_key (str): Custom name for the column header of the keys.
        col_name_value (str): Custom name for the column header of the values.
        title (str): Title of the table.
    """
    data = __convert_data(data)

    table = ""

    # return f"## {title}\n{markdown_table}"
    def get_row(key, value):
        return f"<tr><td><h3>{key}</h3></td><td><p>{value}</p></td></tr>"

    # Add each key-value pair as a row in the table
    for key, value in data.items():
        # Ensure the value is converted to a string if necessary
        table += get_row(key, value)
    return f"""<h1>{title}</h1> <table style="padding-bottom: 20px;" id='data_table'><tr><th><h2>{col_name_key}</h2></th><th><h2>{col_name_value}</h2></th></tr>{table}</table  >  <button onclick='copyTable()'>Copy to Clipboard</button>
 <script>
        function copyTable() {{
            var rows = document.querySelectorAll('#data_table tr');
            var csvContent = '';
            rows.forEach(function(row, index) {{
                var cols = row.querySelectorAll('th, td');
                var rowData = [];
                cols.forEach(function(col) {{
                    var text = col.innerText.replace(/(\\r\\n|\\n|\\r)/gm, '');
                    rowData.push(text);
                }});
                csvContent += rowData.join('\\t') + '\\n';
            }});
            var el = document.createElement('textarea');
            el.value = csvContent;
            document.body.appendChild(el);
            el.select();
            document.execCommand('copy');
            document.body.removeChild(el);
            alert('Copied to clipboard');
        }}
        </script>
        """


def render_table(data, col_name_key="Key", col_name_value="Value", title="table"):
    """
    Renders table from data.

    Parameters:
        data (str or dict): JSON string or dictionary containing the data.
        col_name_key (str): Custom name for the column header of the keys.
        col_name_value (str): Custom name for the column header of the values.
        title (str): Title of the table.
    """
    html_string = data_to_html(data, col_name_key, col_name_value, title)
    styled = (
        "<html><head>"
        + STYLES["table"]
        + "</head><body>"
        + html_string
        + "</body></html>"
    )
    return render_html(styled)

def display_preloaded_vars():
    """
    Displays the preloaded variables in the current environment.
    """
    return render_markdown(PRELOADED_VARS_MARKDOWN)
