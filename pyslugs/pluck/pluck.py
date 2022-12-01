from functools import reduce

def pluck(dofd, *paths, sep='.', default='UNIQUE_DEFAULT'):
    values = []
    
    for path in (p.split(sep) for p in paths):
        try:
            values.append(reduce(lambda acc, keys: acc[keys], path, dofd))
        except KeyError:
            if default == 'UNIQUE_DEFAULT':
                raise 
            values.append(default)
            
    return values[0] if len(values) == 1 else tuple(values)
