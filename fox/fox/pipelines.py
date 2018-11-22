# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import os
html_template = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
        </head>
        <body>
        {content}
        </body>
        </html>
        """


class ReadPipeline(object):
    def process_item(self, item, spider):
        print('#########################获取Content#########################')
        url = item['url']
        content = item['content']
        html = html_template.format(content=content)
        file_name = url.split('/')[5][1:] + url.split('/')[6][1:3] + '.html'
        #拼接要保存的HTML文件名
        file_name = os.path.join(os.path.abspath('.'), 'htmls', file_name)
        print(file_name)
        #将拼接好的html写入文件
        with open(file_name, 'a+', encoding='utf-8') as f:
            f.write(html)
