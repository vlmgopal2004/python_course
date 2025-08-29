import emaillogic

subject = input("Enter email subject: ")
body = input("Enter email body:")

choice = input("Do you want to send \n(1) Single Email \nor\n(2) Bulk Emails? Enter the choice: ")

if choice == '1':
    recipient = input("Enter recipient email: ")
    emaillogic.send_email(recipient, subject, body)
elif choice == '2':
    csv_file = input("Enter path to CSV file with email addresses: ")
    emaillogic.send_bulk_emails(csv_file, subject, body)
else:
    print("Invalid choice! Please enter 1 or 2.")