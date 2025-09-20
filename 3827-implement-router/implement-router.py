
class Router:
    def __init__(self, memory_limit):
        self.packet_queue = deque()
      
        self.memory_limit = memory_limit
        # Set to track unique packets in memory
        self.packet_set = set()
        # Map: destination -> list of timestamps (sorted by insertion order)
        self.destination_map = defaultdict(list)
     
        self.current_size = 0

    def addPacket(self, source, destination, timestamp):
        packet = (source, destination, timestamp)
        
        # Ignore duplicate packets
        if packet in self.packet_set:
            return False

        # Remove oldest packet if memory is full
        if self.current_size >= self.memory_limit:
            oldest = self.packet_queue.popleft()
            self.packet_set.remove(oldest)
            self.destination_map[oldest[1]].pop(0)
            self.current_size -= 1

        # Add new packet
        self.packet_queue.append(packet)
        self.packet_set.add(packet)
        self.destination_map[destination].append(timestamp)
        self.current_size += 1

        return True

    def forwardPacket(self):
        if self.current_size == 0:
            return []

        
        self.current_size -= 1
        packet = self.packet_queue.popleft()
        self.packet_set.remove(packet)
        self.destination_map[packet[1]].pop(0)
        return list(packet)

    def getCount(self, destination, start_time, end_time):
        timestamps = self.destination_map[destination]
       
        left = bisect.bisect_left(timestamps, start_time)
        right = bisect.bisect_right(timestamps, end_time)
        return right - left
