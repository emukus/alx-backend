#!/usr/bin/env python3
"""
Hypermedia pagination
"""
import csv
import math
from typing import List, Dict

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Takes 2 args and returns the requested page no."""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        data = self.dataset()

        if data is None:
            return []

        idx = index_range(page, page_size)
        return data[idx[0]: idx[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Takes the same args and defaults as get_page & returns
        a dict with the following key-value pairs:
        page_size: the length of the returned dataset page
        page: current page no.
        data: dataset page (equivalent to return from previous task
        next_page: no. of next page, None if no next page
        prev_page: no. of prev page, None if no prev page
        total_pages: total no. pages in the dataset as an int
        """
        data = self.get_page(page, page_size)
        total_pages = (len(self.dataset()) // page_size) + 1
        page_size = len(data) if data else 0
        prev_page = page - 1 if page > 1 else None
        next_page = page + 1 if page < total_pages else None

        hyperMedia = {
                'page_size': page_size,
                'page': page,
                'data': data,
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': total_pages
        }

        return hyperMedia
