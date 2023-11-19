dict = {"S": [], "A": [], "B": [], "C": [], "D": [], "F": []}


class TierList:
    def __init__(self, tier, item):
        dict[tier].append(item)

    def __str__(self):
        print_str = ""
        for tier in dict:
            print_str += tier + " : "
            for item in dict[tier]:
                print_str += item
                if item != dict[tier][-1]:
                    print_str += ", "
            print_str += "\n"
        return print_str

        # print_str = ""
        # print_str += tier + " : "
        # for item in dict[tier]:
        #     print_str += item
        #     if item != dict[tier][-1]:
        #         print_str += ", "
        # return print_str

    def add(self, *args):
        if len(args) == 2:
            dict[args[0]].append(args[1])
        if len(args) == 3:
            dict[args[0]].insert(args[1] - 1, args[2])

    def search_tier(self, item):
        for tier in dict:
            for goal in dict[tier]:
                if item == goal:
                    return tier

    def remove(self, item):
        tier = self.search_tier(item)
        if tier == "S" or tier == "A" or tier == "B" or tier == "C" or tier == "D" or tier == "F":
            dict[tier].remove(item)

    def move(self, *args):
        if len(args) == 2:

            self.remove(args[1])
        self.add(self.search_tier(args[1]), args[0], args[1])
        if len(args) == 3:
            self.remove(args[3])
            self.add(args[0], args[1], args[3])


