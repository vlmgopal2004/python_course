from abc import ABC, abstractmethod

# -------------------------
# Base Abstract Class
# -------------------------
class Person(ABC):
    """Abstract base class representing a Metro employee (common attributes)."""

    def __init__(self, name, age, contact_info, gender, employee_id):
        self.name = name
        self.age = age
        self.__contact_info = contact_info  # Private variable (Encapsulation)
        self.gender = gender
        self.employee_id = employee_id

    def update_contact_info(self, new_contact):
        """Setter method to update contact info"""
        self.__contact_info = new_contact

    def get_contact_info(self):
        """Getter method for private contact info"""
        return self.__contact_info

    @abstractmethod
    def display_info(self):
        """Abstract method that must be implemented by subclasses"""
        pass


# -------------------------
# Driver Subclass
# -------------------------
class Driver(Person):
    """Represents a Metro train driver."""

    def __init__(self, name, age, contact_info, gender, employee_id, route_assigned, shift_timing, license_number):
        super().__init__(name, age, contact_info, gender, employee_id)
        self.route_assigned = route_assigned
        self.shift_timing = shift_timing
        self.__license_number = license_number  # Immutable (private)

    @property
    def license_number(self):
        """Read-only property"""
        return self.__license_number

    def update_shift(self, new_shift_timing):
        """Update shift timing for driver"""
        self.shift_timing = new_shift_timing
    
    def display_info(self):
        return (f"[Driver] Name: {self.name}, Age: {self.age}, Contact: {self.get_contact_info()}, "
                f"Gender: {self.gender}, Employee ID: {self.employee_id}, Route: {self.route_assigned}, "
                f"Shift: {self.shift_timing}, License: {self.license_number}")


# -------------------------
# Station Staff Subclass
# -------------------------
class StationStaff(Person):
    """Represents staff working at a Metro station (ticketing, security, cleaning, etc.)"""

    def __init__(self, name, age, contact_info, gender, employee_id, station_name, role):
        super().__init__(name, age, contact_info, gender, employee_id)
        self.station_name = station_name
        self.role = role

    def assign_station(self, new_station_name):
        """Reassign staff to another station"""
        self.station_name = new_station_name

    def display_info(self):
        return (f"[StationStaff] Name: {self.name}, Age: {self.age}, Contact: {self.get_contact_info()}, "
                f"Gender: {self.gender}, Employee ID: {self.employee_id}, Station: {self.station_name}, Role: {self.role}")


# -------------------------
# Maintenance Staff Subclass
# -------------------------
class MaintenanceStaff(Person):
    """Represents maintenance staff with specialization and shift."""

    def __init__(self, name, age, contact_info, gender, employee_id, specialization, shift_timing):
        super().__init__(name, age, contact_info, gender, employee_id)
        self.specialization = specialization
        self.shift_timing = shift_timing

    def update_shift(self, new_shift_timing):
        """Update shift timing for maintenance staff"""
        self.shift_timing = new_shift_timing

    def display_info(self):
        return (f"[MaintenanceStaff] Name: {self.name}, Age: {self.age}, Contact: {self.get_contact_info()}, "
                f"Gender: {self.gender}, Employee ID: {self.employee_id}, Specialization: {self.specialization}, Shift: {self.shift_timing}")


# -------------------------
# Supporting Classes
# -------------------------
class Route:
    """Represents a Metro route with stations and distance."""

    def __init__(self, route_name, station_list, total_distance):
        self.route_name = route_name
        self.station_list = station_list
        self.total_distance = total_distance

    def display_route(self):
        """Show route details"""
        return f"{self.route_name} ({self.total_distance} km): {' ,'.join(self.station_list)}"

    def calculate_estimated_time(self, avg_speed=35):
        """Calculate estimated travel time (minutes)"""
        return round(self.total_distance / avg_speed * 60, 2)


# -------------------------
# Controller / Manager Class
# -------------------------
class MetroManagement:
    """Central class to manage employees, routes, and stations."""

    all_employees = []
    routes = []
    stations = []

    @classmethod
    def register_employee(cls, employee):
        """Register a new employee"""
        cls.all_employees.append(employee)

    def list_all_employees(self):
        """List all registered employees"""
        if not self.all_employees:
            print("No employees registered.")
        else:
            for emp in self.all_employees:
                print(emp.display_info())

    def find_employee_by_id(self, emp_id):
        """Search for an employee by ID"""
        for emp in self.all_employees:
            if emp.employee_id == emp_id:
                return emp.display_info()
        return "Employee not found."

    @staticmethod
    def generate_report():
        """Generate a system report summary"""
        return f"Total Employees: {len(MetroManagement.all_employees)} | Routes: {len(MetroManagement.routes)} | Stations: {len(MetroManagement.stations)}"


# -------------------------
# CLI Interface
# -------------------------
def main():
    metro_system = MetroManagement()

    # ✅ Pre-loaded Hyderabad Metro Routes with all stations
    red_line = Route(
        "Red Line",
        [
            "Miyapur", "JNTU College", "KPHB Colony", "Kukatpally", "Dr. B.R. Ambedkar Balanagar",
            "Moosapet", "Bharatnagar", "Erragadda", "ESI Hospital", "SR Nagar", "Ameerpet",
            "Punjagutta", "Irrum Manzil", "Khairatabad", "Lakdi-ka-pul", "Assembly",
            "Nampally", "Gandhi Bhavan", "Osmania Medical College", "MG Bus Station (MGBS)",
            "Malakpet", "New Market", "Chaderghat", "Dilsukhnagar", "Moosarambagh",
            "LB Nagar"
        ],
        29
    )

    blue_line = Route(
        "Blue Line",
        [
            "Nagole", "Uppal", "Stadium", "NGRI", "Habsiguda", "Tarnaka", "Mettuguda",
            "Secunderabad East", "Parade Ground", "Paradise", "Rasoolpura", "Prakash Nagar",
            "Begumpet", "Ameerpet", "Madhura Nagar", "Yusufguda", "Road No. 5 Jubilee Hills",
            "Jubilee Hills Check Post", "Pedamma Temple", "Madhapur", "Durgam Cheruvu",
            "Hitec City", "Raidurg"
        ],
        27
    )

    green_line = Route(
        "Green Line",
        [
            "JBS Parade Ground", "Parade Ground", "Secunderabad West", "Gandhi Hospital",
            "Musheerabad", "RTC X Roads", "Chikkadpally", "Narayanguda", "Sultan Bazar",
            "MG Bus Station (MGBS)", "Imlibun", "Shalibanda", "Shamsheergunj", "Jungametta",
            "Falaknuma"
        ],
        15
    )
    
    # Store routes inside MetroManagement
    metro_system.routes.extend([red_line, blue_line, green_line])

    # ✅ Add Default Employees (10 total: 3 Drivers, 4 Station Staff, 3 Maintenance Staff)
    default_employees = [
        # Drivers
        Driver("Ravi Kumar", 35, "9876543210", "Male", "D001", "Red Line", "Morning", "LIC12345"),
        Driver("Anita Sharma", 30, "8765432109", "Female", "D002", "Blue Line", "Evening", "LIC54321"),
        Driver("Suresh Reddy", 40, "7654321098", "Male", "D003", "Green Line", "Night", "LIC67890"),

        # Station Staff
        StationStaff("Priya Verma", 28, "9988776655", "Female", "S001", "Ameerpet", "Ticketing"),
        StationStaff("Arjun Singh", 32, "8877665544", "Male", "S002", "LB Nagar", "Security"),
        StationStaff("Meena Iyer", 26, "7766554433", "Female", "S003", "Nagole", "Cleaning"),
        StationStaff("Vikram Das", 29, "6655443322", "Male", "S004", "Raidurg", "Ticketing"),

        # Maintenance Staff
        MaintenanceStaff("Farhan Ali", 38, "5544332211", "Male", "M001", "Electrical", "Morning"),
        MaintenanceStaff("Sunita Devi", 34, "4433221100", "Female", "M002", "Mechanical", "Evening"),
        MaintenanceStaff("Kiran Rao", 36, "3322110099", "Male", "M003", "Signal Systems", "Night"),
    ]

    for emp in default_employees:
        MetroManagement.register_employee(emp)

    # CLI menu loop
    while True:
        print("\n========= Hyderabad Metro Employee Management =========")
        print("1. Register New Employee")
        print("2. List All Employees")
        print("3. Find Employee by ID")
        print("4. Display All Routes")
        print("5. Generate System Report")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\na. Driver\nb. Station Staff\nc. Maintenance Staff")
            sub_choice = input("Enter your choice: ")

            name = input("Enter name: ")
            age = int(input("Enter age: "))
            gender = input("Enter gender: ")
            contact = input("Enter contact info: ")
            emp_id = input("Enter employee ID: ")

            if sub_choice == "a":
                route = input("Enter route assigned: ")
                shift = input("Enter shift timing: ")
                license_no = input("Enter license number: ")
                emp = Driver(name, age, contact, gender, emp_id, route, shift, license_no)

            elif sub_choice == "b":
                station = input("Enter station name: ")
                role = input("Enter role: ")
                emp = StationStaff(name, age, contact, gender, emp_id, station, role)

            elif sub_choice == "c":
                specialization = input("Enter specialization: ")
                shift = input("Enter shift timing: ")
                emp = MaintenanceStaff(name, age, contact, gender, emp_id, specialization, shift)

            else:
                print("Invalid choice.")
                continue

            MetroManagement.register_employee(emp)
            print("Employee registered successfully!")

        elif choice == "2":
            metro_system.list_all_employees()

        elif choice == "3":
            emp_id = input("Enter employee ID to search: ")
            print(metro_system.find_employee_by_id(emp_id))

        elif choice == "4":
            print("\n--- Metro Routes ---")
            for route in metro_system.routes:
                print(route.display_route(), "| Est. Time:", route.calculate_estimated_time(), "min")

        elif choice == "5":
            print(MetroManagement.generate_report())

        elif choice == "6":
            print("Exiting system... Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
