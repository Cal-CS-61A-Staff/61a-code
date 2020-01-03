def json_repr(elem):
    if isinstance(elem, list):
        elem_reprs = [json_repr(x) for x in elem]
        return "[" + ", ".join(elem_reprs) + "]"
    elif isinstance(elem, str):
        return '"' + repr(elem)[1:-1] + '"'
    elif isinstance(elem, dict):
        key_val_reprs = [
            json_repr(key) + ": " + json_repr(val) for key, val in elem.items()
        ]
        return "{" + ", ".join(key_val_reprs) + "}"
    elif isinstance(elem, bool):
        if elem:
            return "true"
        else:
            return "false"
    elif isinstance(elem, (int, float)):
        return repr(elem)
    elif hasattr(elem, "__json_repr__"):
        return elem.__json_repr__()
    else:
        raise Exception("Unable to serialize object of type " + str(type(elem)))
