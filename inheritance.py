# This is the parent class
class military:
    branchName = ''
    headquarters = ''
    numOfEmployees = 873524
    leaderName = ''
    budget = 1000000

# These are child classes
class airForce(military):
    numOfAircrafts = 406
    numOfHelicopters = 432
    numOfPilots = 302

class army(military):
    numOfTanks = 296
    numOfSubmarines = 328
