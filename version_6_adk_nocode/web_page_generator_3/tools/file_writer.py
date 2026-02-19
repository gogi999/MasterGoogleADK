import os

def save_html_to_file(html_content: str, filename: str = "output.html") -> str:
    """Saves the given HTML content to a file.

    Args:
        html_content: The HTML content as a string.
        filename: The name of the file to save the content to.
                  Defaults to 'output.html'.

    Returns:
        A confirmation message with the absolute path of the saved file.
    """
    try:
        # Ensure the filename has an .html extension for safety
        if not filename.lower().endswith(('.html', '.htm')):
            filename += '.html'

        with open(filename, "w", encoding="utf-8") as f:
            f.write(html_content)
        return f"Successfully saved HTML to {os.path.abspath(filename)}"
    except IOError as e:
        return f"Error: Could not save file. Reason: {e}"
