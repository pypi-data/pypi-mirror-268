import webview as wv
import threading as th
import os
import hashlib
import random
from .utils import remove_indentation
from .document import Document
from .js import runpython
class Window:
    def __init__(self, name, path):
        wv.DRAG_REGION_SELECTOR = "drag-region"
        self.webview = wv.create_window(name, f"{path}/index.html", )
        def evalpy(script):
            print(f"Running script {hashlib.sha1(script.encode()).hexdigest()[:7]}")
            #print(remove_indentation(script))
            exec(remove_indentation(script), {"window": self, "document": Document(self)})
        self.webview.expose(evalpy)
    def start(self, debug:bool = False):
        """Starts the window."""
        self.wviewprocess = th.Thread(target=wv.start, kwargs = {"private_mode": True, "debug": debug, "http_port": random.randint(55556, 59999)}, name="MainThread")
        self.wviewprocess.start()
        self.webview.evaluate_js(runpython)
        
