class Garage:

    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self, cars)

    def __getitem__(self, i):
        return self.cars[i]

    def __repr__(self):
        return f"<Garage {self.cars}"




ford = Garage()
ford.cars.append('Fiesta')
ford.cars.append('Focus')

for car in ford:
    print(car)


class LockableList:
    def __init__(self, *values, locked=False):
        self.values = list(values)
        self._locked = locked
'''
The __str__ should be used to return a string that is more suitable for users to read
( e.g it can be more descriptive but not have  every little detail of the object)
'''
    def __str__(self):
        return f"{self.values}"

    def __len__(self):
        return len(self.values)

    def __getitem__(self, i):
        if isinstance(i, int):
            # Perform conversion to positive index if necessary
            if i < 0:
                i = len(self.values) + i

			# Check index lies within the valid range and return value if possible
            if i < 0 or i >= len(self.values):
                raise IndexError("LockableList index out of range")
            else:
                return self.values[i]

friends = LockableList("John", "Rolf", "Mary")

for friend in friends:
	print(friend)


# We have a class called Club, and it is initialized like this (no need to change):
class Club:
    def __init__(self, name):
        self.name = name
        self.players = []

    # optional
    def __len__(self):
        return len(self.players)

    # define a method that allows us to access the i-th player in the club directly via indexing.
    # for example, if some_club is an object of Club class,
    # we can access the i-th player in some_club like this (you may assume i is always valid):
    # some_club[i]
    def __getitem__(self, i):
        return self.players[i]

    # define a method that returns a string representation of this object,
    # which can be used to recreate this object.
    # The return value should be in such format (beware of the spacing):
    # Club {club_name}: {list_of_players}
    # the club_name and list_of_players should be replaced by the according value of current object
    '''
    The __repr should be used to return a string representing the object 
    such that with that string you can re-create the object fully
    '''
    def __repr__(self):
        return f"Club {self.name}: {self.players}"

    # define a method that returns a readable string representation of this object for the user.
    # The return value should be in such format (beware of the spacing):
    # Club {club_name} with {count_of_players} players
    # the club_name and count_of_players should be replaced by the according value of current object
    def __str__(self):
        return f"Club {self.name} with {len(self)} players"

# You only need to finish the method, we will take care of the object creation and call those methods for you!
