from . import table20240326, table20240410, table20240414, table20240415, table20240419


def get_table_factory(table_name):
    if table_name == "table20240326":
        return table20240326
    elif table_name == "table20240410":
        return table20240410
    elif table_name == "table20240414":
        return table20240414
    elif table_name == "table20240415":
        return table20240415
    elif table_name == "table20240419":
        return table20240419
    else:
        raise NotImplementedError(f"Not supported <{table_name=}>.")
