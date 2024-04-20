import csv, io
from mmengine.fileio import register_handler, BaseFileHandler


@register_handler("csv")
class CSVHandler(BaseFileHandler):
    str_like = True

    def load_from_fileobj(self, file, use_eval=False, **kwargs):
        ret = list(csv.reader(file, **kwargs))
        if use_eval:
            ret = [[eval(__) for __ in _] for _ in ret]
        return ret

    def dump_to_fileobj(self, obj, file, **kwargs):
        csv_writer = csv.writer(file, **kwargs)
        csv_writer.writerows(obj)

    def dump_to_str(self, obj, **kwargs):
        output = io.StringIO()
        self.dump_to_fileobj(output, obj)
        return output.getvalue()
