# network_thread.py
from PyQt5.QtCore import QThread, pyqtSignal
from Api.Api import DockerApi

class NetworkThread(QThread):
    images_loaded = pyqtSignal(list)
    containers_loaded= pyqtSignal(list)

    def __init__(self):
        super(NetworkThread, self).__init__()

    def fetch_images(self):
        data = DockerApi.get_images()
        self.images_loaded.emit(data)
    
    def fetch_containers(self):
        data = DockerApi.get_containers()
        self.containers_loaded.emit(data)
