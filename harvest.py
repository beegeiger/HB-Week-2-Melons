############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    
    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.pairings = []

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)
        # Fill in the rest

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code
        # Fill in the rest


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType("musk", 1998, "green", True, True, "muskmelon")
    musk.add_pairing("mint")
    all_melon_types.append(musk)
    
    casaba = MelonType("cas", 2003, "orange", True, False, "casaba")
    casaba.add_pairing("strawberries")
    casaba.add_pairing("mint")
    all_melon_types.append(casaba)
    
    crenshaw = MelonType("cren", 1996, "green", False, False, "crenshaw")
    crenshaw.add_pairing("proscuitto")
    all_melon_types.append(crenshaw)
    
    yellow_watermelon = MelonType("yw", 2013, "yellow", False, True, "yellow_watermelon")
    yellow_watermelon.add_pairing("ice cream")
    all_melon_types.append(yellow_watermelon)

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    for melon in melon_types:
        print "{} pairs with".format(melon.name)
        for pairing in melon.pairings:
            print "- {}".format(pairing)
    # Fill in the rest

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melons = {}
    for melon in melon_types:
        melons[melon.code] = melon
    return melons

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""
    def __init__(self, melon_type, shape_rate, color_rate, field, harvester):
        self.melon_type = melon_type
        self.shape_rate = shape_rate
        self.color_rate = color_rate
        self.field = field
        self.harvester = harvester

    def is_sellable(self):
        return self.shape_rate > 5 and self.color_rate > 5 and self.field != 3
    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""
    melon_list = []

    melon1 = Melon(melon_types['yw'], 8, 7, 2, "Sheila")
    melon2 = Melon(melon_types['yw'], 3, 4, 2, "Sheila")
    melon3 = Melon(melon_types['yw'], 9, 8 , 3, "Sheila")
    melon4 = Melon(melon_types['cas'], 10, 6, 35, "Sheila")
    melon5 = Melon(melon_types['cren'], 8, 9, 35, "Michael")
    melon6 = Melon(melon_types['cren'], 8, 2, 35, "Michael")
    melon7 = Melon(melon_types['cren'], 2, 3, 4, "Michael")
    melon8 = Melon(melon_types['musk'], 6, 7, 4, "Michael")
    melon9 = Melon(melon_types['yw'], 7, 10, 3, "Sheila")

    melon_list.append(melon1)
    melon_list.append(melon2)
    melon_list.append(melon3)
    melon_list.append(melon4)
    melon_list.append(melon5)
    melon_list.append(melon6)
    melon_list.append(melon7)
    melon_list.append(melon8)
    melon_list.append(melon9)

    return melon_list

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 


melons = make_melon_types()
# print melons
# print_pairing_info(melons)
melons = make_melon_type_lookup(melons)
# melon = Melon("yw", 7, 10, 3, "Sheila")
# print melon.is_sellable()
print make_melons(melons)