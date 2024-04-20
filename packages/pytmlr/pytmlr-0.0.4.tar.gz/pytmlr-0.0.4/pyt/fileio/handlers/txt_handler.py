from mmengine.fileio import register_handler, BaseFileHandler


@register_handler("py")
@register_handler("txt")
class TxtHandler(BaseFileHandler):
    str_like = True

    def load_from_fileobj(self, file, **kwargs):
        return file.read()

    def dump_to_fileobj(self, obj, file, **kwargs):
        file.write(str(obj))

    def dump_to_str(self, obj, **kwargs):
        return str(obj)
