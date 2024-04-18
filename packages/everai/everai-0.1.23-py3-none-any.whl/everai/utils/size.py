units = [
    "B",
    "KiB",
    "MiB",
    "GiB",
    "TiB",
    "PiB",
    "EiB"
]


def readable_size(size: int) -> str:
    if size < 1024:
        return "{} B".format(size)

    show_size: float = float(size)
    unit_index = 0
    while show_size > 1024:
        show_size /= 1024
        unit_index += 1
        if unit_index >= len(units) - 1:
            break

    if show_size == int(show_size):
        return f'{int(show_size)} {units[unit_index]}'

    return f'{show_size:.2f} {units[unit_index]}'
