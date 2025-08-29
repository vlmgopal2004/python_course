import emaillogic2

subject = input("Enter email subject: ")
body = input("Enter email body:")

choice = input('''Do you want to send 
               (1) Single Email or
               (2) Bulk Emails? 
               Enter the choice(1 or 2): ''')
attach_choice = input("Do you want to add attachments? (y/n): ").lower()
attachments = []
if attach_choice == "y":
    files = input("Enter file paths separated by commas: ")
    attachments = [f.strip() for f in files.split(",")]

if choice == '1':
    recipient = input("Enter recipient email: ")
    emaillogic2.send_email(recipient, subject, body, attachments)
elif choice == '2':
    csv_file = input("Enter path to CSV file with email addresses: ")
    emaillogic2.send_bulk_emails(csv_file, subject, body, attachments)
else:
    print("Invalid choice! Please enter 1 or 2.")