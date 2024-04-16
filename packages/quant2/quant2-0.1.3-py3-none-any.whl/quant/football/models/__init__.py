from .stnet import STNetV1, STNetV2, STNetV3, STNetV4


def get_model(model_type, *args, **kwargs):
    if model_type == "STNetV1":
        return STNetV1(*args, **kwargs)
    elif model_type == "STNetV2":
        return STNetV2(*args, **kwargs)
    elif model_type == "STNetV3":
        return STNetV3(*args, **kwargs)
    elif model_type == "STNetV4":
        return STNetV4(*args, **kwargs)
    else:
        raise NotImplementedError(f"Not supported <{model_type=}>.")
