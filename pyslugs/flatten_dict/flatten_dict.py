def flatten_dict(dod, *, sep='_', key_maker=''):
    if key_maker:
        return {key_maker( (*k.split(sep),) ) if len(k.split(sep)) > 1 else k: v 
                for k, v in _go_deep(dod, sep).items()}

    return _go_deep(dod, sep)


def _go_deep(nd, sep, placeholder=''):
    if not isinstance(nd, dict):
        return {placeholder: nd}

    return {placeholder + sep + str(kk) if placeholder else str(kk): vv
            for k, v in nd.items()
            for kk, vv in _go_deep(v, sep, k).items()}
