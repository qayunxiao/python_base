# -*- coding: utf-8 -*-
# @Time    : 2023/1/7 10:39
# @Author  : alvin
# @File    : news_service.py
# @Software: PyCharm
from news_dao import NewsDao
class NewsService:
    __news_dao = NewsDao()
    def search_unreview_list(self,page):
        res = self.__news_dao.search_unreview_list(page)
        return res

    def search_unreview_count_page(self):
        count_page = self.__news_dao.search_unreview_count_page()
        return count_page
