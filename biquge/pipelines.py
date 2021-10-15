# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os , time
from biquge.settings import DOWNLOAD_PATH

class BiqugePipeline:
    def __init__(self):
        self.folder_path = DOWNLOAD_PATH
        self.topic_path = ''

    def process_item(self, item, spider):
        self.topic_path = self.folder_path + os.path.sep + str(item['novel_name'])
        if not os.path.exists(self.topic_path):
            os.makedirs(self.topic_path)
        section_filename = self.topic_path + os.path.sep + str(item['section_number']) + '--' + str(item['section_name'] + '.txt')
        with open(section_filename, 'w', encoding='utf-8') as f:
            f.write(item['section_name'])
            f.writelines(item['section_content'])
        return item

    def close_spider(self, spider):
        # 设定新文件的名称
        new_file = self.topic_path + os.path.sep + self.topic_path.split("/")[-1] + ".txt"
        # 如果新文件存在，删掉
        if os.path.exists(new_file):
            os.remove(new_file)
            time.sleep(3)
        # 获取目录下所有文件
        files = os.listdir(self.topic_path)
        # 过滤非txt文件
        for i_file in files:
            if not i_file.endswith('.txt'):
                files.remove(i_file)

        # 按照章节顺序调整章节排序
        files = sorted(files, key=lambda filename: int(filename.split('--')[0]))

        # 依次打开旧文件，合并到新文件
        with open(new_file, 'w', encoding='utf-8') as f:
            for old_file in files:
                old_file = open(self.topic_path + os.path.sep + old_file, 'r')
                old_file_content = old_file.read()
                f.write(old_file_content)
                old_file.close()
                os.remove(str(old_file.name))
            f.close()

