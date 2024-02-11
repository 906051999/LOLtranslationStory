from DrissionPage import ChromiumPage, ChromiumOptions
import os
from bs4 import BeautifulSoup
import urllib.request


def replace_content(path, file_name):
    html_path = os.path.join(path, 'origin.html')
    # Read the content of the file
    with open(html_path, 'r') as f:
        html_content = f.read()

    # Parse the HTML content
    html_soup = BeautifulSoup(html_content, 'html.parser')

    # Directory to save images
    img_dir = path + "/images/"
    os.makedirs(img_dir, exist_ok=True)
    print("images 文件夹已创建")

    replace_html_path = os.path.join(date_part, 'replace.html')

    # Find all img tags
    for img_tag in html_soup.find_all('img'):
        # Get the URL of the image
        img_url = img_tag.get('src')

        # If the URL does not end with .jpg, skip this iteration
        if not img_url.endswith('.jpg'):
            img_tag.decompose()
            continue

        print(img_url)

        # Download the image and save it to a local directory
        img_name = os.path.basename(img_url)
        img_path = os.path.join(img_dir, img_name)
        urllib.request.urlretrieve(img_url, img_path)

        img_tag['src'] = f"/source/{file_name}/images/{img_name}"

        # # Replace the src attribute with the local path of the image
        # img_tag['src'] = img_path

    # 使用 prettify 方法格式化 HTML
    pretty_html = html_soup.prettify()
    # 将格式化后的 HTML 写入文件
    with open(replace_html_path, 'w', encoding='utf-8') as f:
        f.write(pretty_html)


if __name__ == '__main__':
    # Read the content of the file
    with open('url.txt', 'r') as f:
        content = f.read()

    # Parse the content with BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')

    url_list = []

    # Find all <a> tags and print their href attribute
    for a_tag in soup.find_all('a'):
        url_list.append(a_tag.get('href'))
        print(a_tag.get('href'))

    for url in url_list:
        page = ChromiumPage(addr_or_opts=ChromiumOptions().auto_port())
        page.get(url)
        page.wait.load_start()
        page.wait.doc_loaded()
        # Get the HTML content of the element
        article_html = page.ele(".article").html
        article_title = page.ele(".art-tit").text
        article_time = page.ele(".art-time").text

        # Extract the date part from article_time
        date_part = "../source/" + article_time.split(' ')[0]
        date = article_time.split(' ')[0]
        # Assuming article_time is in 'YYYY-MM-DD HH:MM:SS' format

        # Create a directory with this date if it doesn't exist
        if not os.path.exists(date_part):
            os.makedirs(date_part)
            print(f"{date_part} 已创建")
        else:
            print(f"{date_part} 已存在")
            continue

        # Change the current working directory to this new directory
        # os.chdir(date_part)

        html_path = os.path.join(date_part, 'origin.html')

        # Open the file in write mode and write the content
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(f'<head>\n <meta charset="UTF-8">\n <title>{article_title}</title>\n</head>\n')
            f.write(f'<h1 class="name">{article_title}</h1>\n')
            f.write(f'<div class="time">{article_time}</div>\n')
            f.write(article_html)
        print(f"{date_part}: origin.html 已创建")

        replace_content(date_part, date)

