#!/usr/bin/env PYTHON

import os
from tornado.web import Application
from tornado.ioloop import IOLoop
from src.handlers import handlers
from tornado.options import options

from src.common.utils import init_root_path, load_config
    
def init_server():
    settings = dict(
                    debug = True,
                    static_path=options.static_resource_dir,
                    template_path=options.current_template_dir
    )
    server = Application(handlers, **settings)
    #server.settings = settings # Never use this.    
    server.listen(options.port)

if __name__ == "__main__":
    root_path = os.path.dirname(os.path.abspath(__file__))
    init_root_path(root_path)
    
    config_file_path = root_path + os.sep + "setup.cfg"
    load_config(config_file_path)
    
    init_server()
    IOLoop.current().instance().start()

