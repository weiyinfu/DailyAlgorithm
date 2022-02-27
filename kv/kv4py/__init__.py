import logging
good_format = logging.Formatter(
    '%(asctime)s pid=%(process)d %(filename)s:%(lineno)s %(funcName)s [%(name)s]-%(levelname)s: %(message)s')
logging.root.setLevel(logging.INFO)
import sys
handler=logging.StreamHandler(sys.stdout)
logging.root.addHandler(handler)
handler.setFormatter(good_format)
logging.info("good morning")