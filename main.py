import heapq  


class ParkingLot:
    def __init__(self, max_slots):
        # Create a list of available slots (1 to max_slots) and convert to a min-heap
        self.available = list(range(1, max_slots + 1))
        heapq.heapify(self.available)  # Make it a min-heap
        self.occupied = {}  # Map slot -> car ID
        self.car_to_slot = {}  # Map car ID -> slot

    def park_car(self, car_id):
        if not self.available:
            print("Full capacity, please wait.")
            return None
        # Get the nearest available slot
        slot = heapq.heappop(self.available)
        # Track both slot -> car ID and car ID -> slot
        self.occupied[slot] = car_id
        self.car_to_slot[car_id] = slot
        print(f"Car {car_id} parked at slot {slot}")
        return slot

    def leave_slot(self, car_id):
        # Check if the car ID exists in the mapping
        if car_id not in self.car_to_slot:
            print(f"Car {car_id} not found in the parking lot.")
            return
        # Find the slot from car ID
        slot = self.car_to_slot.pop(car_id)
        # Remove from occupied slots
        self.occupied.pop(slot)
        # Add the slot back to the available heap
        heapq.heappush(self.available, slot)
        print(f"Car {car_id} left from slot {slot}. Slot {slot} is now available.")

lot = ParkingLot(2)           
lot.park_car("ABC123")       
lot.park_car("XYZ789")      
lot.park_car("XYZ799")      
lot.leave_slot("ABC123")     
lot.park_car("LMN456")       



# Car ABC123 parked at slot 1
# Car XYZ789 parked at slot 2
# Full capacity, please wait.
# Car ABC123 left from slot 1. Slot 1 is now available.
# Car LMN456 parked at slot 1
