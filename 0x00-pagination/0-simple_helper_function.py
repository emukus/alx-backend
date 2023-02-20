#!/usr/bin/env python3
"""Takes two int aguments and returns a tuple of size two
containing a start and end index corresponding to the range of indexes"""


def index_range(page: int, page_size: int) -> tuple:
    """Params: page: page to be indexed
    page_size: no. of indexes a page should have
    """
    start = (page - 1) * page_size
    end = page * page_size
    return start, end
