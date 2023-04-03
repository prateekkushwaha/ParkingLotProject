from enum import Enum


class Output(Enum):
    Created_Parking_Lot = "Created a parking lot with %s slots"
    Allocated_Slot_Number = "Allocated slot number: %s"
    Slot_Number_Free = "Slot number %s is free"
    Status_Table_Cols = "Slot No. Registration No Colour"
    Parking_Lot_Full = "Sorry, parking lot is full"
    Car_Slot_Not_Found = "Not found"
