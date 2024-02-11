from urllib.parse import quote
from bs4 import BeautifulSoup
import re
from DrissionPage import ChromiumPage, ChromiumOptions

base_url = "https://lol.qq.com/search/index.shtml?order=sIdxTime&page="
count = 1
after_url = "&type=ALL&keyword="
keyword = "联盟译事"
encoded_keyword = quote(keyword)
full_url = f"{base_url}{count}{after_url}{encoded_keyword}"

# 创建 ChromiumPage 对象
page = ChromiumPage()

# 使用get方法访问URL
page.get(full_url)
page.wait.ele_loaded('css=div.result-total[style="display: block"]')
html = page.ele(".m-navigation")

# 使用BeautifulSoup解析HTML
soup = BeautifulSoup(html.html, 'html.parser')

# 找到class为"m-navigation"的div标签
div = soup.find('div', {'class': 'm-navigation'})

# 使用正则表达式找到所有的数字
numbers = re.findall(r'\d+', div.text)

# 将数字列表转换为整数列表
numbers = list(map(int, numbers))

# 找到最大的数字
page_num = max(numbers)

print(page_num)

res = page.eles(".item-name")

_list = []

for item in res:
    # 获取当前<h3>元素下的<a>元素
    lnk = item('tag:a')
    _list.append(lnk)
    # 打印<a>元素文本和href属性
    print(lnk.text, lnk.link)

for count in range(2, page_num + 1):
    page_temp = ChromiumPage(addr_or_opts=ChromiumOptions().auto_port())
    page_temp.get(f"{base_url}{count}{after_url}{encoded_keyword}")
    page_temp.wait.load_start()
    page_temp.wait.ele_loaded('css=div.result-total[style="display: block"]')
    page_temp.wait.doc_loaded()
    info = page_temp.eles(".item-name")
    for item in info:
        # 获取当前<h3>元素下的<a>元素
        lnk = item('tag:a')
        _list.append(lnk)
        # 打印<a>元素文本和href属性
        print(lnk.text, lnk.link)


with open('url.txt', 'w') as f:
    for item in _list:
        f.write(item.html + '\n')
