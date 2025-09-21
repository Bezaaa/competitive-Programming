

class MovieRentingSystem:

    def __init__(self, n, entries):
        # Map (shop, movie) -> price
        self.price_map = {}
        
        # Unrented movies: movie -> SortedList of (price, shop)
        self.unrented = {}
        
        # Rented movies: global SortedList of (price, shop, movie)
        self.rented = SortedList()
        
        for shop, movie, price in entries:
            self.price_map[(shop, movie)] = price
            
            if movie not in self.unrented:
                self.unrented[movie] = SortedList()
            
            self.unrented[movie].add((price, shop))

    def search(self, movie):
        """Return top 5 cheapest unrented shops for a movie."""
        if movie not in self.unrented:
            return []
        return [shop for price, shop in self.unrented[movie][:5]]

    def rent(self, shop, movie):
        """Rent a movie from a shop."""
        price = self.price_map[(shop, movie)]
        
        # Remove from unrented
        self.unrented[movie].remove((price, shop))
        
        # Add to rented
        self.rented.add((price, shop, movie))

    def drop(self, shop, movie):
        """Return a previously rented movie."""
        price = self.price_map[(shop, movie)]
        
        # Remove from rented
        self.rented.remove((price, shop, movie))
        
        # Add back to unrented
        self.unrented[movie].add((price, shop))

    def report(self):
        """Return top 5 cheapest rented movies."""
        return [[shop, movie] for price, shop, movie in self.rented[:5]]
