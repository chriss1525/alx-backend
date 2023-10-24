#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" calculate the start and end indices for a given page and page_size"""


def index_range(page: int, page_size: int) -> tuple:
    """ return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters."""
    staart = (page - 1) * page_size
    end = page * page_size
    return (staart, end)
