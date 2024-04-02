from event_manager import EventManager

class UserInterface:
    def __init__(self):
        self.event_manager = EventManager()

    def display_menu(self):
        print("Event Manager")
        print("1. Create Event")
        print("2. List Events")
        print("3. Delete Event")
        print("4. Search Events")
        print("5. Edit Event")
        print("6. Quit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                title = input("Enter event title: ")
                description = input("Enter event description: ")
                date = input("Enter event date (YYYY-MM-DD): ")
                time = input("Enter event time (HH:MM): ")
                print(self.event_manager.add_event(title, description, date, time))
            elif choice == '2':
                print(self.event_manager.list_events())
            elif choice == '3':
                title = input("Enter event title to delete: ")
                print(self.event_manager.delete_event(title))
            elif choice == '4':
                query = input("Enter keyword or date to search: ")
                print(self.event_manager.search_events(query))
            elif choice == '5':
                title = input("Enter event title to edit: ")
                new_title = input("Enter new title (leave blank to keep current): ")
                new_description = input("Enter new description (leave blank to keep current): ")
                new_date = input("Enter new date (YYYY-MM-DD) (leave blank to keep current): ")
                new_time = input("Enter new time (HH:MM) (leave blank to keep current): ")
                print(self.event_manager.edit_event(title, new_title, new_description, new_date, new_time))
            elif choice == '6':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    ui = UserInterface()
    ui.run()
