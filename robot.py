class Robot:
    """
    Represents a robot, with a name.
    """
    # A class variable, counting the number of robots
    population = 0

    def __init__(self, name):
        """ Initializes the data."""
        self.name = name
        print("(Initializing {})".format(self.name))

        Robot.population += 1

    def status(self):
        pass

    def die(self):
        """ I am dying. """
        print("{} is being destroyed!".format(self.name))
        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(Robot.population))

    def say_hello(self):
        print("Greetings, my master call me {}".format(self.name))

    @classmethod
    def how_many(cls):
        print("We have {:d} robots".format(cls.population))
