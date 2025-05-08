import heapq

class ParkingLot:
    def __init__(self, max_slots):
        self.available = list(range(1, max_slots + 1)) 
        heapq.heapify(self.available)                  
        self.occupied = set()

    def park_car(self):
        if not self.available:
            print("Full capacity, please wait.")
            return None
        slot = heapq.heappop(self.available)             
        self.occupied.add(slot)
        print(f"Car parked at slot {slot}")
        return slot

    def leave_slot(self, slot):
        if slot not in self.occupied:
            print(f"Slot {slot} is not occupied.")
            return
        self.occupied.remove(slot)
        heapq.heappush(self.available, slot)            
        print(f"Slot {slot} is now available.")


lot = ParkingLot(2)
lot.park_car()   # Car parks at slot 1
lot.park_car()   # Car parks at slot 2
lot.park_car()   # Car parks at slot 3
lot.leave_slot(1)  # Car leaves from slot 1
lot.park_car()   # Next car parks at slot 1 again

# CONSOLE OUTPUT
# Car parked at slot 1
# Car parked at slot 2
# Full capacity, please wait.
# Slot 1 is now available.
# Car parked at slot 1
