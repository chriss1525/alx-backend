#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import math
from typing import List

""" calculate the start and end indices for a given page and page_size"""


def index_range(page: int, page_size: int) -> tuple:
    """ return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters."""
    staart = (page - 1) * page_size
    end = page * page_size
    return (staart, end)


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
        """takes two integer arguments page with default value 1 and page_size
        with default value 10."""
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        return [] if (start >= len(self.dataset()) or
                      end > len(self.dataset())) else self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """ return a dictionary containing key value pairs of the pagination"""
        return {
            'page_size': len(self.get_page(page, page_size)),
            'page': page,
            'data': self.get_page(page, page_size),
            'next_page': page + 1 if page + 1 < len(self.dataset()) else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': math.ceil(len(self.dataset()) / page_size)
        }
