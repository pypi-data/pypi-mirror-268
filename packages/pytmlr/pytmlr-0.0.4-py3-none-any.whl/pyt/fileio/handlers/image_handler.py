import imageio
from mmengine.fileio import register_handler, BaseFileHandler


class ImageHandler(BaseFileHandler):
    str_like = False

    def load_from_fileobj(self, file, **kwargs):
        return imageio.v3.imread(file, **kwargs)

    def dump_to_str(self, obj, **kwargs):
        raise NotImplementedError

    def dump_to_fileobj(self, obj, file, **kwargs):
        return imageio.v3.imwrite(file, obj, **kwargs)


@register_handler("png")
class PngHandler(ImageHandler):
    def dump_to_fileobj(self, obj, file, **kwargs):
        super().dump_to_fileobj(obj, file, extension=".png", **kwargs)


@register_handler("gif")
class GifHandler(ImageHandler):
    def dump_to_fileobj(self, obj, file, **kwargs):
        super().dump_to_fileobj(obj, file, extension=".gif", **kwargs)


@register_handler("jpeg")
class JpegHandler(ImageHandler):
    def dump_to_fileobj(self, obj, file, **kwargs):
        super().dump_to_fileobj(obj, file, extension=".jpeg", **kwargs)


@register_handler("jpg")
class JpgHandler(ImageHandler):
    def dump_to_fileobj(self, obj, file, **kwargs):
        super().dump_to_fileobj(obj, file, extension=".jpeg", **kwargs)
