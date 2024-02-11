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

source_dir = '../pages'
links = []

for root, dirs, files in os.walk(source_dir):
    for dir in dirs:
        replace_html_path = os.path.join(root, dir, 'replace.html')
        if os.path.exists(replace_html_path):
            with open(replace_html_path, 'r') as f:
                soup = BeautifulSoup(f, 'html.parser')

            style_tag = soup.new_tag("style")
            style_tag.string = styles
            soup.head.append(style_tag)
            pretty_html = soup.prettify()

            with open(replace_html_path, 'w') as f:
                f.write(pretty_html)

            title = soup.title.string if soup.title else 'No Title'
            article = soup.find('div', {'class': 'article'})
            summary = article if article else 'No Summary'
            link = f'<a href="{replace_html_path}" target="_blank">{title}</a>'
            links.append((dir, link, summary))

links.sort(reverse=True)

path = os.path.join(source_dir, 'index.html')

with open(path, 'w') as f:
    f.write('<html lang="zh-CN">\n')
    f.write(f'<head>\n <meta charset="UTF-8">\n <title>联盟译事合集</title>\n')
    f.write(f'<style>\n')

    f.write(
        '.time { font-size: 16px; color: #333; margin: 0px 0; height: auto; overflow: auto; text-align: left; display: flex; align-items: flex-start; }\n')
    f.write('@media (max-width: 600px) { .time { flex-direction: column; width: 100%; height: auto; } }\n')
    #
    f.write(
        'a { color: #FFFFFF; font-size: 16px; background-color:  #3F51B5; border: 1px solid #3F51B5; padding: 10px; text-decoration: none; transition: background-color 0.3s ease; text-align: left; display: flex; align-items: flex-start; }\n')
    f.write('a:hover { background-color: #FFFFFF; color: #3F51B5; }\n')

    # f.write(
    #     '.link { color: #FFFFFF; font-size: 16px; background-color:  #3F51B5; border: 1px solid #3F51B5; padding: 10px; text-decoration: none; transition: background-color 0.3s ease; text-align: left; display: flex; align-items: flex-start; }\n')
    # f.write('.link:hover { background-color: #FFFFFF; color: #3F51B5; }\n')

    f.write(
        '.link-container { display: compact; font-size: 12px; flex-direction: column; justify-content: center; align-items: center; border: 1px solid #E0E0E0; box-shadow: 0 2px 1px -1px rgba(0,0,0,0.2), 0 1px 1px 0 rgba(0,0,0,0.14), 0 1px 3px 0 rgba(0,0,0,0.12); margin: 0px; padding: 10px; background-color: #FFFFFF; width: auto; height: 70%; overflow: auto; }\n')
    f.write('@media (max-width: 600px) { .link-container { flex-direction: column; width: 90%; height: 50%; } }\n')

    f.write(f'</style>\n')
    f.write(f'</head>\n')
    f.write(f'<body>\n')
    f.write(f'<h1 class="name">联盟译事合集</h1>\n')
    for dir, link, summary in links:
        f.write(f'<div class="time"><h3>{dir}</h3></div>\n')
        f.write(f'<div class="link">{link}</div>\n')
        f.write(f'<div class="link-container"><p>{summary}</p></div>\n')
    f.write('</body>\n</html>')
