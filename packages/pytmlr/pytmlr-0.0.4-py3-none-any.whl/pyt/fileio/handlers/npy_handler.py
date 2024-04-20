import numpy as np
from mmengine.fileio import register_handler, BaseFileHandler


@register_handler("npy")
class NpyHandler(BaseFileHandler):
    str_like = False

    def load_from_fileobj(self, file, **kwargs):
        return np.load(file, **kwargs)

    def dump_to_str(self, obj, **kwargs):
        raise NotImplementedError("NpyHandler does not support dump_to_str.")

    def dump_to_fileobj(self, obj, file, **kwargs):
        np.save(file, obj, **kwargs)
