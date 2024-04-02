#!/usr/bin/env python3

"""Simple helper function

    - function named index_range that takes two
        integer arguments page and page_size.
    - the function should return a tuple of size
        two containing a startindex and an end
        index corresponding to the range of indexes
        to return in a list for those
        particular pagination parameters.
    - page numbers are 1-indexed, i.e. the first page is page 1.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """simple helper func"""
    start_index = (page - 1) * page_size
    end_index = page_size + start_index
    return (start_index, end_index)
