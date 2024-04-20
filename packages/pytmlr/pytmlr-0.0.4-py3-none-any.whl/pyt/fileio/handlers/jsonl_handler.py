import json
from mmengine.fileio import register_handler, BaseFileHandler


@register_handler("jsonl")
class JsonlHandler(BaseFileHandler):
    str_like = False

    def load_from_fileobj(self, file, **kwargs):
        result = [json.loads(jline) for jline in file.readlines()]
        return result

    def dump_to_fileobj(self, obj, file, **kwargs):
        obj.write(self.dump_to_str(obj, **kwargs))

    def dump_to_str(self, obj, **kwargs):
        assert isinstance(obj, (tuple, list)), "obj must be a tuple or list"
        return "\n".join(json.dumps(line) for line in obj)
