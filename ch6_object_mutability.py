l1 = [3, [66,55,44], (7,8,9)]
# Create a shallow copy. Also l2 = l1[:]
l2 = list(l1)
# has no effect on l2
l1.append(100)
# this affect l2
l1[1].remove(55)
print("l2", l2)
print("l1", l1)
# This affect l1
l2[1] += [33, 22]
# += operator create a new tuple, so it won't affect l1
l2[2] += (10, 11)
print("l1", l1)
print("l2", l2)


# ########################################################################
# A bad idea to use mutable parameter as default argument:
# ########################################################################
class HauntedBus:
    # list as default parameter here
    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

# Create bus1
bus1 = HauntedBus(["Jack", "Alice"])
bus1.pick("Mike")
bus1.drop("Jack")
# Everything is right
bus1.passengers

# Create bus2 with default empty
bus2 = HauntedBus()
bus2.pick("Jack")
# everything looks ok so far
bus2.passengers

# Now create bus3 with default empty
bus3 = HauntedBus()
# It should be empty, but now it has values.  The reason is that the self.passenger becomes a reference of the default
# list which was empty initially. Now self.default is a attribute of bus2 and it points to the same object(list) as the
# default passenger parameter does. Since bus2 picked a name, the default list will be changed, too.
# Now if we create a new instance with default parameter, it will use the same object(list) which is already be filled.
bus3.passengers


# ########################################################################
# Defensive programming with mutable parameter as default argument: better to make a copy of it
# ########################################################################
class TwilightBus:
    # The passergers parameter will be a mutable(list), so set None as default. This is right!
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        # since we know passengers will be a list, here we should create a copy of it
        # otherwise, self.passengers become an alias of the passed variable
        # if we modify self.passengers, the original passed variable(same object) will be modified too
        else:
            self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

basketball_team = ["Sue", "Tina", "Maya", "Dianna", "Pat"]
bus = TwilightBus(basketball_team)
bus.drop("Sue")
bus.drop("Tina")
# looks OK for the instance's attribute
bus.passengers
# But the original list is also changed
basketball_team

# del delete references but not object
a = [1,2]
b = a
# This only delete the referenc a(label), not the object [1,2]
del a
b
# Now rebinding b to a different object, object [1,2] has no reference(label, variable name) pointing to it,
# therefore, the garbage collector will discard it
b = [3]