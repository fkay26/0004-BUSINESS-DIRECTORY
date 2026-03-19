from datetime import datetime

class Business:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.date_added = datetime.now()

    def display(self):
        return f"{self.name} ({self.category}) - {self.date_added.strftime('%Y-%m-%d %H:%M')}"