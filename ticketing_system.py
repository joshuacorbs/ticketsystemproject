import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("support_tickets.db")
cursor = conn.cursor()

# Create the tickets table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        department TEXT NOT NULL,
        issue TEXT NOT NULL,
        priority TEXT CHECK(priority IN ('Low', 'Medium', 'High')) NOT NULL,
        status TEXT CHECK(status IN ('Open', 'In Progress', 'Resolved')) DEFAULT 'Open'
    )
''')
conn.commit()

# Function to create a new ticket
def create_ticket():
    name = input("Enter your name: ")
    department = input("Enter your department: ")
    issue = input("Describe your issue: ")
    priority = input("Enter priority (Low, Medium, High): ")
    
    cursor.execute("INSERT INTO tickets (name, department, issue, priority) VALUES (?, ?, ?, ?)",
                   (name, department, issue, priority))
    conn.commit()
    print("\nTicket created successfully!\n")

# Function to view all tickets
def view_tickets():
    cursor.execute("SELECT * FROM tickets")
    tickets = cursor.fetchall()
    if not tickets:
        print("\nNo tickets found.\n")
        return
    for ticket in tickets:
        print(f"ID: {ticket[0]}, Name: {ticket[1]}, Dept: {ticket[2]}, Issue: {ticket[3]}, Priority: {ticket[4]}, Status: {ticket[5]}")

# Function to update ticket status
def update_ticket():
    ticket_id = input("Enter ticket ID to update: ")
    new_status = input("Enter new status (Open, In Progress, Resolved): ")
    cursor.execute("UPDATE tickets SET status = ? WHERE id = ?", (new_status, ticket_id))
    conn.commit()
    print("\nTicket updated successfully!\n")

# Function to delete a ticket
def delete_ticket():
    ticket_id = input("Enter ticket ID to delete: ")
    cursor.execute("DELETE FROM tickets WHERE id = ?", (ticket_id,))
    conn.commit()
    print("\nTicket deleted successfully!\n")

# Main menu
def main():
    while True:
        print("\nIT Support Ticketing System")
        print("1. Create Ticket")
        print("2. View Tickets")
        print("3. Update Ticket Status")
        print("4. Delete Ticket")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            create_ticket()
        elif choice == "2":
            view_tickets()
        elif choice == "3":
            update_ticket()
        elif choice == "4":
            delete_ticket()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

# Close database connection when done
conn.close()
 