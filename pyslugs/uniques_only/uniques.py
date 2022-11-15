def ishashable(element):
    try:
        hash(element)
    except TypeError:
        return False

    return True


def uniques_only(data):
    unique = set()
    unique_unhash = []

    for item in data:
        if not ishashable(item):   
            if item not in unique_unhash:
                unique_unhash.append(item)
                yield item
            continue
    
        if item not in unique:
            unique.add(item)
            yield item
