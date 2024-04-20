import pickle, bz2, gzip
from mmengine.fileio import register_handler, BaseFileHandler


@register_handler("pgz")
class PgzHandler(BaseFileHandler):
    str_like = False

    def load_from_fileobj(self, file, **kwargs):
        with gzip.GzipFile(fileobj=file, mode="rb") as f:
            return pickle.load(f, **kwargs)

    def dump_to_str(self, obj, **kwargs):
        return gzip.compress(obj, **kwargs)

    def dump_to_fileobj(self, obj, file, **kwargs):
        with gzip.GzipFile(fileobj=file, mode="wb") as f:
            pickle.dump(obj, f, **kwargs)


@register_handler("pbz2")
class Pbz2Handler(BaseFileHandler):
    str_like = False

    def load_from_fileobj(self, file, **kwargs):
        with bz2.BZ2File(file, mode="rb") as f:
            return pickle.load(f, **kwargs)

    def dump_to_str(self, obj, **kwargs):
        return bz2.compress(obj, **kwargs)

    def dump_to_fileobj(self, obj, file, **kwargs):
        with bz2.BZ2File(file, mode="wb") as f:
            pickle.dump(obj, f, **kwargs)
