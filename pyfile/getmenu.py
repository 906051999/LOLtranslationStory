import os
from bs4 import BeautifulSoup

styles = """
body {
    font-family: Arial, sans-serif;
}
h1 {
    color: #333;
    font-size: 2em;
}
p {
    font-size: 1em;
    line-height: 1.6;
    color: #666;
}
"""

# Define the path to the source directory
source_dir = '../source'

# Initialize an empty list to store the links
links = []

# Traverse the source directory
for root, dirs, files in os.walk(source_dir):
    # For each subdirectory
    for dir in dirs:
        # Define the path to the replace.html file
        replace_html_path = os.path.join(root, dir, 'replace.html')
        # Check if replace.html exists
        if os.path.exists(replace_html_path):
            # Open and parse replace.html
            with open(replace_html_path, 'r') as f:
                soup = BeautifulSoup(f, 'html.parser')

            # Add CSS styles to the HTML content
            style_tag = soup.new_tag("style")
            style_tag.string = styles
            soup.head.append(style_tag)
            # Beautify the HTML content
            pretty_html = soup.prettify()
            # Write the beautified HTML content back to replace.html
            with open(replace_html_path, 'w') as f:
                f.write(pretty_html)

            # Extract the title
            title = soup.title.string if soup.title else 'No Title'
            # Create a link to replace.html, using the title as the link text
            link = f'<a href="{replace_html_path}" target="_blank">{title}</a>'
            # Add the directory name and link to the list
            links.append((dir, link))

# Sort the links in reverse order by directory name
links.sort(reverse=True)

# Generate an HTML file with the list of links
path = os.path.join(source_dir, 'index.html')

with open(path, 'w') as f:
    f.write('<html lang="zh-CN">\n')
    f.write(f'<head>\n <meta charset="UTF-8">\n <title>联盟译事合集</title>\n')
    f.write(f'<style>\n')
    f.write(
        'body { font-family: Roboto, sans-serif; background-color: #ECEFF1; display: flex; flex-direction: column; align-items: center; justify-content: center; }\n')
    f.write(
        '.link-container { display: flex; flex-direction: column; justify-content: center; align-items: center; border: 1px solid #E0E0E0; box-shadow: 0 2px 1px -1px rgba(0,0,0,0.2), 0 1px 1px 0 rgba(0,0,0,0.14), 0 1px 3px 0 rgba(0,0,0,0.12); margin: 10px; padding: 10px; background-color: #FFFFFF; }\n')
    f.write(
        'a { color: #3F51B5; font-size: 18px; background-color: #ECEFF1; border: 1px solid #3F51B5; padding: 10px; text-decoration: none; transition: background-color 0.3s ease; }\n')
    f.write('a:hover { background-color: #3F51B5; color: #FFFFFF; }\n')
    f.write('@media (max-width: 600px) { .link-container { flex-direction: column; } }\n')
    f.write(f'</style>\n')
    f.write(f'</head>\n')
    f.write(f'<body>\n')
    f.write(f'<h1 class="name">联盟译事合集</h1>\n')
    for dir, link in links:
        f.write(f'<div class="link-container"><h3>{dir}</h3>{link}</div>\n')
    f.write('</body>\n</html>')
