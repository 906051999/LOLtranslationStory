import re

# Open the file and read its content
with open('url.txt', 'r') as file:
    content = file.read()

# Find all <a> tags
links = re.findall(r'<a href="(.*?)".*?>(.*?)</a>', content)

# Open a new Markdown file and write the links
with open('url.md', 'w') as file:
    for link in links:
        # Format the link into Markdown syntax
        md_link = f'> [{link[1]}]({link[0]})\n> \n'
        # Write the link to the file
        file.write(md_link)