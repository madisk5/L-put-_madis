import csv


class Model:
    def __init__(self):
        self.data = []

    def load_file(self, filename, delimiter=';', encoding='utf-8'):
        with open(filename, 'r', encoding=encoding) as file:
            csv_reader = csv.reader(file, delimiter=delimiter)
            next(csv_reader)
            self.data = list(csv_reader)

        self.data = [[cell.lower() for cell in row] for row in self.data]

    def search_text(self, query):
        query_lower = query.lower()
        search_results = []


        for row in self.data:
            for cell in row:
                if query_lower in cell.lower():
                    search_results.append(row)
                    break

        return search_results
