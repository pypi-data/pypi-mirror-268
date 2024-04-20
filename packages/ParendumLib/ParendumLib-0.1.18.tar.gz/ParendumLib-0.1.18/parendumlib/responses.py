from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse


class Response:

    def __init__(self, config: dict = None, templates_directory: str = None):
        self.templates = None if not templates_directory else Jinja2Templates(directory=templates_directory)
        self.config = config or dict()

    def message(self, data, msg, extra: dict = None):
        return JSONResponse(self.__response_model__(data, msg, extra))

    def render_template(self, file_name: str, context: dict):
        return self.templates.TemplateResponse(file_name, context)

    def error_message(self, key: str, error_key: str):
        _msg_data = self.config.get('messages', dict()).get(key, dict())
        _title = _msg_data.get('title', '<No title defined>')
        _msg = _msg_data.get('errors', dict()).get(error_key, dict(code=999, message="<No message defined>"))
        return JSONResponse(self.__error_response_model__(_title, _msg.get('code', 500), _msg.get('message')))

    @staticmethod
    def __response_model__(data, msg: str = None, extra: dict = None):
        if not isinstance(data, list):
            data = [data]
        res = dict(data=data, code=200)
        if msg:
            res["message"] = msg
        if extra:
            res.update(extra)
        return res

    @staticmethod
    def __error_response_model__(error, code: int, msg):
        return dict(error=error, code=code, message=msg)
