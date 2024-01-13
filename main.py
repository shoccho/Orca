import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel, QTextEdit
from Api.DataFetcher import NetworkThread
from ImagesTab.ImagesTab import ImageTabContent

class Orca(QMainWindow):
    def __init__(self):
        super(Orca, self).__init__()

        self.setWindowTitle('Orca GUI')
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.tabs = QTabWidget(self.central_widget)

        self.images = QWidget()
        self.containers = QWidget()
        self.logs = QWidget()

        self.tabs.addTab(self.images, 'Images')
        self.tabs.addTab(self.containers, 'Containers')
        self.tabs.addTab(self.logs, 'Logs')

        self.network_thread = NetworkThread()

        self.network_thread.images_loaded.connect(self.populate_images)
        self.network_thread.fetch_images()
        
        self.network_thread.containers_loaded.connect(self.populate_containers)
        self.network_thread.fetch_containers()

        self.layout = QVBoxLayout(self.central_widget)
        self.layout.addWidget(self.tabs)

    def populate_images(self, data):
        layout = QVBoxLayout(self.images)
        label = QLabel("All docker images")
        layout.addWidget(label)
        layout.addWidget(ImageTabContent(data))

    def populate_containers(self, data):
        layout = QVBoxLayout(self.containers)
        label = QLabel("All docker containers")
        layout.addWidget(label)
        layout.addWidget(QTextEdit(str(data)))


def main():
    app = QApplication(sys.argv)
    window = Orca()
    app.setStyle("Fusion")

    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
