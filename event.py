class Event:
    def __init__(self, title, description, date, time):
        self.title = title
        self.description = description
        self.date = date
        self.time = time

    def __str__(self):
        return f"Title: {self.title}\nDescription: {self.description}\nDate: {self.date}\nTime: {self.time}"
