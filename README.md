# biquge
用来爬取小说

## 问题总结：
1. 如果默认直接抓取会导致所有的章节发生混乱，所以在item中维护了section_url及section_number字段，使用url-starturl中的number来记录每一章节的顺序。
2. 最后重写close方法，在close方法中获取download下来的章节，然后按照章节number顺序后合并到最终的txt中，最后将下载的原始章节txt删除。
