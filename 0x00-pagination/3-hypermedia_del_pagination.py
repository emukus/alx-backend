#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
                self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                    i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Takes 2 args and returns a dictionary with the following key-value pairs:
        index: idx of the first item in the current page
        next_index: the next idx to query with.
        The idx of the first item after the last item on the current page.
        page_size: the current page size
        data: actual page of the dataset
        """
        idx_dataset = self.indexed_dataset()
        data_length = len(idx_dataset)

        assert type(index) is int and 0 <= index < data_length

        i, mv, data = 0, index, []
        while (i < page_size and index < data_length):
            element = idx_dataset.get(mv, None)
            if element:
                data.append(element)
                i += 1
            mv += 1

        next_index = None
        while (mv < data_length):
            element = idx_dataset.get(mv, None)
            if element:
                next_index = mv
                break
            mv += 1

        dict_h = {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data
        }

        return dict_h
