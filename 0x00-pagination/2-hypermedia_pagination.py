#!/usr/bin/env python3

"""Hypermedia pagination
"""

import csv
from typing import List, Dict
import math
from typing import Tuple


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

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """simple helper func"""
        start_index = (page - 1) * page_size
        end_index = page_size + start_index
        return (start_index, end_index)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """return the appropriate page of the dataset """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        page_index = self.index_range(page, page_size)
        return self.dataset()[page_index[0]: page_index[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """get hypermedia data"""
        return {
            "page_size": page_size,
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": page + 1 if page < len(self.dataset()) else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": len(self.dataset())
        }
