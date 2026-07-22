class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair position and speed, then sort by position DESCENDING
        cars = sorted(zip(position, speed), reverse=True)
        
        fleets = 0
        current_slowest_time = 0
        
        for p, s in cars:
            # Your quotient logic: (Target - Position) / Speed
            time_to_reach = (target - p) / s
            
            # If this car takes LONGER than the fleet ahead, it starts a new fleet
            if time_to_reach > current_slowest_time:
                fleets += 1
                current_slowest_time = time_to_reach
                
        return fleets