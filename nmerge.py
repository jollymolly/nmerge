#!python3
"""Merge arbitrary sorted iterables"""


def data_sources_get(data_sources, idx = -1):

    data_sources_len = len(data_sources)
    boundary = idx+1

    if idx == -1:
        idx = 0
        boundary = data_sources_len
    elif not (0 <= idx < data_sources_len):
        raise IndexError(f"Expected data source index within [0, {data_sources_len}) bounds, got: {idx}.")
    else:
        boundary = idx + 1

    ret_val = []

    while idx < boundary:
        try:
            ret_val.append(next(data_sources[idx]))
        except StopIteration:
            data_sources.pop(idx)
            boundary -= 1
            continue
        idx += 1

    return ret_val

def nmerge(*args):

    data_sources = list(map(iter, filter(bool, args)))
    data_items = data_sources_get(data_sources)

    while data_items:

        min_value = min(data_items)

        yield min_value

        min_idx = data_items.index(min_value)
        next_value = data_sources_get(data_sources, min_idx)

        if next_value:
            data_items[min_idx] = next_value[0]
        else:
            data_items.pop(min_idx)


if __name__ == "__main__":
    print(list(nmerge((7, 8, 9), [5, 5, 5, 5, 5, 6], (), range(0, 5), (v for v in ()))))
