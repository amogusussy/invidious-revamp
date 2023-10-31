def readable_number(data, key):
    value = data[key]
    if value < 1000:
        return f"{value}"
    elif value < 10000:
        return f'{value/1000:.1f}K'
    elif value < 1000000:
        return f'{round(value / 1000):.0f}K'
    else:
        return f'{value / 1000000:.1f}M'
