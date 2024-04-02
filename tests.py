import unittest
from event_manager import EventManager

class TestEventManager(unittest.TestCase):
    def setUp(self):
        self.event_manager = EventManager()

    def test_add_event(self):
        result = self.event_manager.add_event("Test Event", "This is a test event", "2024-01-01", "12:00")
        self.assertEqual(result, "Event added successfully.")

    def test_delete_event(self):
        self.event_manager.add_event("Test Event", "This is a test event", "2024-01-01", "12:00")
        result = self.event_manager.delete_event("Test Event")
        self.assertEqual(result, "Event deleted successfully.")

    def test_search_events(self):
        self.event_manager.add_event("Test Event", "This is a test event", "2024-01-01", "12:00")
        self.event_manager.add_event("Another Event", "Another test event", "2024-01-02", "13:00")
        result = self.event_manager.search_events("Test")
        self.assertIn("Test Event", result)
        self.assertNotIn("Another Event", result)

    def test_edit_event(self):
        self.event_manager.add_event("Test Event", "This is a test event", "2024-01-01", "12:00")
        result = self.event_manager.edit_event("Test Event", "New Title", "New Description", "2024-01-03", "14:00")
        self.assertEqual(result, "Event updated successfully.")

if __name__ == '__main__':
    unittest.main()
