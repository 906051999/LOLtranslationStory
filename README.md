# LOLtranslationStory
> 内容来自英雄联盟官方的"联盟译事", 只作为学习使用, 请尊重英雄联盟官方网站的使用条款。
> 
> [联盟译事：虚空族类顶级意志卑尔维斯，本土化呈现女皇的无上威势](https://lol.qq.com/news/detail.shtml?docid=15168906162493285141)
> 
> [联盟译事：底城的热情花火泽丽诠释祖安崭新时代](https://lol.qq.com/news/detail.shtml?docid=86893411690277599)
> 
> [联盟译事：以愁作为核心的约德尔人，解读薇古丝身上的独特气质](https://lol.qq.com/news/detail.shtml?docid=10343030346006725307)
> 
> [联盟译事：阿克尚不羁本色深度揭秘影哨设定](https://lol.qq.com/news/detail.shtml?docid=10867916789870485779)
> 
> [联盟译事：格温之名源于亚瑟王将裁缝术语融入翻译](https://lol.qq.com/news/detail.shtml?docid=5902085337455895442)
> 
> [联盟译事：佛耶戈为爱从不停息将诗词之美融入翻译创作](https://lol.qq.com/news/detail.shtml?docid=7239192221425934299)
> 
> [联盟译事：新英雄曾被叫成锐尔国服如何敲定称号及技能名称](https://lol.qq.com/news/detail.shtml?docid=14351372353286859495)
> 
> [联盟译事：揭秘国服星籁歌姬的诞生所有技能皆为音乐主题](https://lol.qq.com/news/detail.shtml?docid=9207848174778189539)
> 
> [联盟译事：为何是沙漠玫瑰而非蔷薇国服译者揭秘莎弥拉翻译故事](https://lol.qq.com/news/detail.shtml?docid=5812536460776118380)
> 
> [联盟译事：揭秘国服“封魔剑魂”称号由来两兄弟与风的不解之缘](https://lol.qq.com/news/detail.shtml?docid=8749787250067449933)
> 
> [联盟译事：充满美感的三字技能组揭秘莉莉娅国服翻译细节](https://lol.qq.com/news/detail.shtml?docid=18021965173029968637)
> 
> [联盟译事：揭秘国服翻译细节沃利贝尔并非它的真名](https://lol.qq.com/news/detail.shtml?docid=8799017217918521682)
> 
> [联盟译事：为均衡忍者注入日式风味何为阿卡丽的“我流”奥义](https://lol.qq.com/news/detail.shtml?docid=6935573049773931075)
> 
> [《联盟译事》：从古诗里汲取灵感揭秘厄斐琉斯武器的命名翻译](https://lol.qq.com/news/detail.shtml?docid=4930147506630970022)
> 
> [联盟译事：凯隐之名竟源于圣经恶人?国服翻译揭秘](https://lol.qq.com/news/detail.shtml?docid=13924685260802963814)
> 
> [联盟译事：禁奥义!瞬狱影杀阵揭秘国服劫翻译细节](https://lol.qq.com/news/detail.shtml?docid=12453037154785678107)
> 
> [联盟译事：从审判天使到正义天使凯尔汉化翻译揭秘](https://lol.qq.com/news/detail.shtml?docid=9022327950992967729)
> 
> [联盟译事：千字轻盈如羊形二玉合一便为珏千珏名称揭秘](https://lol.qq.com/news/detail.shtml?docid=2770045523847026784)
> 
> [联盟译事：以其人之道还治其人之身揭秘塞拉斯称号由来](https://lol.qq.com/news/detail.shtml?docid=10337118720846787728)
> 
> [联盟译事：意境才是本体亚索的“随缘”翻译揭秘](https://lol.qq.com/news/detail.shtml?docid=5192471297395355053)
> 
> [联盟译事：“戏命师烬”中文翻译揭秘Jhin的四种写法](https://lol.qq.com/news/detail.shtml?docid=8759053297907135765)
> 
> [联盟译事：揭秘“万花通灵妮蔻”中文翻译称号背后的故事](https://lol.qq.com/news/detail.shtml?docid=2892403497252779862)

---

**以下为 copilot 生成的内容,仅供参考**

---

这个项目是一个基于Python的网络爬虫，用于从"英雄联盟"官方网站获取并处理文章。该项目主要分为三个部分：

1. **获取URL (`geturl.py`)**：此脚本从"英雄联盟"官方网站的搜索结果中获取文章的URL。它使用`DrissionPage`库与网站交互，并使用`BeautifulSoup`解析HTML内容。

2. **获取和处理内容 (`getcontent.py`)**：此脚本获取每篇文章的HTML内容，处理它，并将其保存为本地HTML文件。它还下载文章中的任何图片，并将HTML内容中的图片URL替换为下载的图片的本地路径。

3. **生成菜单 (`getmenu.py`)**：此脚本生成一个HTML文件，作为所有处理过的文章的菜单。它遍历保存处理过的文章的目录，提取每篇文章的标题，并创建一个链接到文章的HTML文件。

## 需求

- Python 3.6或更高版本
- 库：`DrissionPage`，`BeautifulSoup`，`os`，`urllib`

## 使用方法

1. 运行`geturl.py`获取文章的URL。
2. 运行`getcontent.py`获取并处理每篇文章的内容。
3. 运行`getmenu.py`生成菜单。

请注意，应按照上述指定的顺序运行脚本。

## 免责声明 

此项目仅用于教育目的。请尊重"英雄联盟"官方网站的使用条款。

---

This project is a Python-based web scraper that fetches and processes articles from the "League of Legends" official website. The project is divided into three main parts:

1. **URL Fetching (`geturl.py`)**: This script fetches the URLs of the articles from the search results of the "League of Legends" official website. It uses the `DrissionPage` library to interact with the website and `BeautifulSoup` to parse the HTML content.

2. **Content Fetching and Processing (`getcontent.py`)**: This script fetches the HTML content of each article, processes it, and saves it as a local HTML file. It also downloads any images in the article and replaces the image URLs in the HTML content with the local paths of the downloaded images.

3. **Menu Generation (`getmenu.py`)**: This script generates an HTML file that serves as a menu for all the processed articles. It traverses the directory where the processed articles are saved, extracts the title of each article, and creates a link to the article's HTML file.

## Requirements

- Python 3.6 or higher
- Libraries: `DrissionPage`, `BeautifulSoup`, `os`, `urllib`

## Usage

1. Run `geturl.py` to fetch the URLs of the articles.
2. Run `getcontent.py` to fetch and process the content of each article.
3. Run `getmenu.py` to generate the menu.

Please note that the scripts should be run in the order specified above.

## Disclaimer

This project is for educational purposes only. Please respect the terms of use of the "League of Legends" official website.