seats = {
    'U1': {'Booking_status': True, 'gender': 'M', 'price': 1200, 'name': 'Kalyan', 'age': 21},
    'U2': {'Booking_status': True, 'gender': 'M', 'price': 1200, 'name': 'Ram', 'age': 22},
    'U3': {'Booking_status': True, 'gender': 'M', 'price': 1200, 'name': 'Mustafa', 'age': 22},
    'U4': {'Booking_status': False, 'gender': None, 'price': 1200, 'name': None, 'age': None},
    'U5': {'Booking_status': False, 'gender': None, 'price': 1200, 'name': None, 'age': None},
    'U6': {'Booking_status': False, 'gender': None, 'price': 1200, 'name': None, 'age': None},
    'U7': {'Booking_status': True, 'gender': 'F', 'price': 1200, 'name': 'Ramya', 'age': 28},
    'U8': {'Booking_status': False, 'gender': None, 'price': 1200, 'name': None, 'age': None},
    'U9': {'Booking_status': False, 'gender': None, 'price': 1200, 'name': None, 'age': None},
    'U10': {'Booking_status': True, 'gender': 'F', 'price': 1200, 'name': 'Swathi', 'age': 30},
    'L1': {'Booking_status': False, 'gender': None, 'price': 1200, 'name': None, 'age': None},
    'L5': {'Booking_status': False, 'gender': None, 'price': 1200, 'name': None, 'age': None},
    'L10': {'Booking_status': False, 'gender': None, 'price': 1200, 'name': None, 'age': None}
}

def display_seats(seats):
    print("\nSeat Status:")
    for seat in seats.keys():
        if seats[seat]['Booking_status']:
            gender = seats[seat]['gender']
            print(f"**{seat}**-{gender}")
        else:
            print(f"{seat}-{seats[seat]['price']}")

def payment_process(seats, selected_seat):
    age = seats[selected_seat]['age']
    price = seats[selected_seat]['price']
    if age < 5:
        print("Below five years: No payment required.")
        seats[selected_seat]['Booking_status'] = True
    elif age < 60:
        payment = int(input(f"Enter the payment ₹{price}: "))
        if payment == price:
            print("Payment successful!\nSeat booked.")
            seats[selected_seat]['Booking_status'] = True
        else:
            print("Incorrect payment. Try again.")
    else:
        discount = price * 0.15
        discounted_price = int(price - discount)
        payment = int(input(f"Enter the payment ₹{discounted_price}: "))
        if payment == discounted_price:
            print("Payment successful with senior citizen discount!\nSeat booked.")
            seats[selected_seat]['Booking_status'] = True
        else:
            print("Incorrect payment. Try again.")

def search_seat(seats, selected_seat):
    if selected_seat in seats:
        if seats[selected_seat]['Booking_status']:
            print(f"Seat {selected_seat} is already booked. Try another one.")
        else:
            seats[selected_seat]['name'] = input("Enter your name: ")
            seats[selected_seat]['gender'] = input("Enter your gender (M/F): ").upper()
            seats[selected_seat]['age'] = int(input("Enter your age: "))
            payment_process(seats, selected_seat)
    else:
        print("Invalid seat number. Please try again.")

# Run the seat booking
display_seats(seats)
selected_seat = input("\nEnter the seat number to book: ").upper()
search_seat(seats, selected_seat)
display_seats(seats)
