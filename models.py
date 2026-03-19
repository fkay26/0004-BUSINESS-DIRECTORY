#Business class for storing business data
from datetime import datetime
#using class as stated in the requirements
class Business:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.date_added = datetime.now()

    def display(self):
        return f"{self.name} ({self.category}) - {self.date_added.strftime('%Y-%m-%d %H:%M')}"