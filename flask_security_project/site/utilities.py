import copy
from flask_sqlalchemy import Pagination


def get_page_numbers(pagination: Pagination, active_page: int):
    pages_list = list()
    prev_list = list()
    next_list = list()

    prev_pag = copy.copy(pagination)
    next_pag = copy.copy(pagination)

    for x in range(1, 4):
        if prev_pag.has_prev:
            prev_list.append(prev_pag.prev_num)
        else:
            break
        prev_pag = prev_pag.prev()

    for y in range(1, 4):
        if next_pag.has_next:
            next_list.append(next_pag.next_num)
        else:
            break
        next_pag = next_pag.next()

    pages_list.extend(reversed(prev_list))
    pages_list.append(active_page)
    pages_list.extend(next_list)
    return pages_list
