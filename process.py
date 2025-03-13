import os
import json
from pathlib import Path

titles = []
contentDict = {}
def procMd(dirname: str):
    with os.scandir(dirname) as entries:
        for entry in entries:
            if entry.is_file():
                pathStr = os.path.join(dirname,entry.name)
                print(pathStr)
                content = getText(pathStr)
                name = entry.name[:-3].split('.', 1)[1].replace('Python', '').replace('常用数据结构之', '')
                titles.append(name)
                contentDict[name] = content
def getText(pathStr: str)->str:
    # 创建 Path 对象
    file_path = Path(pathStr)
    content = file_path.read_text(encoding='utf-8')
    content = content.replace('src="res/', 'class="lazy" data-src="/res/').replace('(res/', '(/res/')
    return content

# 使用 os.scandir() 遍历目录
with os.scandir('.') as entries:
    for entry in entries:
        if entry.is_dir() and entry.name.startswith('Day'):
            procMd(entry.name)

if len(contentDict.items()) > 0:
    json_str = json.dumps(contentDict, ensure_ascii=False)
    json_str = json_str.replace('骆昊', '小明')
    with open('content.json', 'w', encoding='utf-8') as file:
        file.write(json_str)
    json_str = json.dumps(titles, ensure_ascii=False)
    with open('titles.json', 'w', encoding='utf-8') as file:
        file.write(json_str)