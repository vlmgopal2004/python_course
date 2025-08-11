import Booking_Bus_Seats as bs
bs.display_seats(bs.seats)
bs.selected_seat = input("\nEnter the seat number to book: ").upper()
bs.search_seat(bs.seats, bs.selected_seat)
bs.display_seats(bs.seats)