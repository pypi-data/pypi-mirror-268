from mmengine.fileio import register_handler, BaseFileHandler


@register_handler("pt")
class PTHandler(BaseFileHandler):
    str_like = False

    def load_from_fileobj(self, file, **kwargs):
        import torch

        return torch.load(file, **kwargs)

    def dump_to_str(self, obj, **kwargs):
        raise NotImplementedError("PTHandler does not support dump_to_str.")

    def dump_to_fileobj(self, obj, file, **kwargs):
        import torch

        torch.save(obj, file, **kwargs)


@register_handler("safetensors")
class SafeTensorsHandler(BaseFileHandler):
    str_like = False

    def load_from_fileobj(self, file, **kwargs):
        from safetensors.torch import load
        return load(file.read())

    def dump_to_str(self, obj, **kwargs):
        raise NotImplementedError("PTHandler does not support dump_to_str.")

    def dump_to_fileobj(self, obj, file, **kwargs):
        from safetensors.torch import save_file
        save_file(obj, file)
