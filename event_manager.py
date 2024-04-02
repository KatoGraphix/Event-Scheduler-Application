from event import Event
from datetime import datetime

class EventManager:
    def __init__(self):
        self.events = []

    def add_event(self, title, description, date, time):
        try:
            datetime.strptime(date, '%Y-%m-%d')
            datetime.strptime(time, '%H:%M')
        except ValueError:
            return "Invalid date or time format. Please use YYYY-MM-DD for date and HH:MM for time."

        event = Event(title, description, date, time)
        self.events.append(event)
        return "Event added successfully."

    def list_events(self):
        if not self.events:
            return "No events found."
        
        sorted_events = sorted(self.events, key=lambda x: (x.date, x.time))
        return '\n\n'.join(str(event) for event in sorted_events)

    def delete_event(self, title):
        for event in self.events:
            if event.title == title:
                self.events.remove(event)
                return "Event deleted successfully."
        return "Event not found."

    def search_events(self, query):
        results = []
        for event in self.events:
            if query.lower() in event.title.lower() or query.lower() in event.description.lower() or query == event.date:
                results.append(event)
        if results:
            return '\n\n'.join(str(event) for event in results)
        else:
            return "No matching events found."

    def edit_event(self, title, new_title, new_description, new_date, new_time):
        for event in self.events:
            if event.title == title:
                event.title = new_title
                event.description = new_description
                event.date = new_date
                event.time = new_time
                return "Event updated successfully."
        return "Event not found."
