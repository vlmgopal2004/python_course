from abc import ABC, abstractmethod

# ==============================
# Base Class (Abstraction + Encapsulation)
# ==============================
class Person(ABC):
    def __init__(self, name, age, gender, contact_info, employee_id):
        self.name = name
        self.age = age
        self.gender = gender
        self.__contact_info = contact_info  # Encapsulation
        self.employee_id = employee_id

    def update_contact_info(self, new_contact):
        self.__contact_info = new_contact

    def get_contact_info(self):
        return self.__contact_info

    @abstractmethod
    def display_info(self):
        pass  # Abstraction

# ==============================
# Subclasses (Inheritance + Polymorphism)
# ==============================
class Driver(Person):
    def __init__(self, name, age, gender, contact_info, employee_id, route_assigned, shift_timing, license_number):
        super().__init__(name, age, gender, contact_info, employee_id)
        self.route_assigned = route_assigned
        self.shift_timing = shift_timing
        self.__license_number = license_number  # Encapsulation

    def update_shift(self, new_shift):
        self.shift_timing = new_shift

    def display_info(self):  # Polymorphism
        print(f"Driver: {self.name}, Route: {self.route_assigned}, Shift: {self.shift_timing}")

class StationStaff(Person):
    def __init__(self, name, age, gender, contact_info, employee_id, station_name, role):
        super().__init__(name, age, gender, contact_info, employee_id)
        self.station_name = station_name
        self.role = role

    def assign_station(self, station_name):
        self.station_name = station_name

    def display_info(self):  # Polymorphism
        print(f"Station Staff: {self.name}, Station: {self.station_name}, Role: {self.role}")

class MaintenanceStaff(Person):
    def __init__(self, name, age, gender, contact_info, employee_id, specialization, shift_timing):
        super().__init__(name, age, gender, contact_info, employee_id)
        self.specialization = specialization
        self.shift_timing = shift_timing

    def report_issue(self, issue):
        print(f"Maintenance Staff {self.name} reported: {issue}")

    def display_info(self):  # Polymorphism
        print(f"Maintenance Staff: {self.name}, Specialization: {self.specialization}, Shift: {self.shift_timing}")

# ==============================
# Supporting Classes
# ==============================
class Route:
    def __init__(self, route_id, stations_list, total_distance):
        self.route_id = route_id
        self.stations_list = stations_list
        self.total_distance = total_distance

    def display_route(self):
        print(f"Route {self.route_id} covers: {', '.join(self.stations_list)}")

    @staticmethod
    def calculate_estimated_time(distance, avg_speed):
        return distance / avg_speed

class Station:
    def __init__(self, station_name, location, facilities):
        self.station_name = station_name
        self.location = location
        self.facilities = facilities

    def display_facilities(self):
        print(f"Facilities at {self.station_name}: {', '.join(self.facilities)}")

# ==============================
# Controller Class (Class Methods + Static Methods)
# ==============================
class MetroManagement:
    all_employees = []
    routes = []
    stations = []

    @classmethod
    def register_employee(cls, employee):  # Class Method
        cls.all_employees.append(employee)

    def list_all_employees(self):  # Instance Method
        for emp in self.all_employees:
            emp.display_info()

    def find_employee_by_id(self, emp_id):  # Instance Method
        for emp in self.all_employees:
            if emp.employee_id == emp_id:
                return emp
        return None

    @staticmethod
    def generate_report():  # Static Method
        print(f"Total Employees: {len(MetroManagement.all_employees)}")
        print(f"Total Routes: {len(MetroManagement.routes)}")
        print(f"Total Stations: {len(MetroManagement.stations)}")

# ==============================
# Example Usage (CLI could be built here)
# ==============================
if __name__ == "__main__":
    metro = MetroManagement()

    d1 = Driver("Rajesh", 35, "M", "9876543210", "D001", "Route1", "Morning", "LIC123")
    s1 = StationStaff("Priya", 29, "F", "9876500000", "S001", "Ameerpet", "Ticketing")

    MetroManagement.register_employee(d1)
    MetroManagement.register_employee(s1)

    metro.list_all_employees()
    MetroManagement.generate_report()
