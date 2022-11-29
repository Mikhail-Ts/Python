# Поиск контакта

from export_data import export_data
from print_data import print_data

def search_data(text, data):
    if len(data) > 0:
        for i in data:
            if text in i:
                return i
    else:
        return None