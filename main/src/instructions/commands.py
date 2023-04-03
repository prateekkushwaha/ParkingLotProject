from enum import Enum


class Commands(Enum):
    Create_Parking_Lot = "create_parking_lot"
    Park_Car = "park"
    Leave_Car = "leave"
    Status_Of_Parking_Lot = "status"
    Regis_Nums_For_Cars = "registration_numbers_for_cars_with_colour"
    Slot_Nums_For_Cars_With_Colours = "slot_numbers_for_cars_with_colour"
    Slot_Num_For_Regis = "slot_number_for_registration_number"
