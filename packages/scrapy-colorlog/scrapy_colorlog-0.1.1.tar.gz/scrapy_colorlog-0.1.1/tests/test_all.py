from scrapy_colorlog.formatter import ColoredFormatter
from scrapy_colorlog.utils import configure_logging, get_scrapy_root_handler


def test_logging():
    configure_logging()
    handler = get_scrapy_root_handler()
    assert handler is not None
    assert isinstance(handler.formatter, ColoredFormatter)
    assert False
