from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem
from ImagesTab.FieldParser import parse_images_data

class ImageTabContent(QWidget):
    def __init__(self, data_list):
        super(ImageTabContent, self).__init__()

        table = QTableWidget(self)
        
        table.setColumnCount(len(data_list[0].keys())-1)
        table.setRowCount(len(data_list))  

        header_labels = []
        for key in data_list[0].keys():
            if(key == "RepoDigests"):
                continue
            header_labels.append(f"{key}")

        table.setHorizontalHeaderLabels(header_labels)
        for item_index, item_data in enumerate(data_list):
            parsed_items = parse_images_data(item_data.items())
            for col, value in enumerate(parsed_items):
                item = QTableWidgetItem(str(value))
                table.setItem(item_index, col, item)

        table.resizeColumnsToContents()
        layout = QVBoxLayout(self)
        layout.addWidget(table)