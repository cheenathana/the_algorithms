def parse_ranges(string):
    for dranges in string.split(','):
        # If incase -> character was there
        if '->' in dranges:
            val,_ = dranges.split('->')
            yield int(val)
            continue           
        
        # If incase single digit was there
        if '-' not in dranges:
            yield int(dranges)
            continue

        start, end = dranges.split('-')
        for x in range(int(start), int(end)+1):
            yield x
