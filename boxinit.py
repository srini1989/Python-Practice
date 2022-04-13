class Box:
    """
    This is an example of Box methods.
    Below are the methods that are available
    1. reset
    2. resize
    3. volume
    4. surface_area
    """

    def __init__(self, height, width, depth):
        self.height = height
        self.depth = depth
        self.width = width

    def reset(self):
        print("I am being reset")
        self.height = 2
        self.depth = 2
        self.width = 2
        print("Reset Complete !")

    def resize(self, height, width, depth):
        print("I am resizing")
        self.height = height
        self.width = width
        self.depth = depth
        print("Resizing Complete !")

    def volume(self):
        return self.height * self.width * self.depth

    def surface_area(self):
        return 2 * (self.height + self.width *
                    self.width + self.depth *
                    self.width + self.depth)

    def describe(self):
        print("Hey, I am box! with volume {}mm, and surface are {}mm.".format(self.volume(), self.surface_area()))

    def compare(self, other_box):
        """
        Compares two boxes in the following way
        somebox.compare(otherbox)
        """
        volume1 = self.volume()
        volume2 = other_box.volume()
        difference_volume = volume1 - volume2
        if difference_volume > 0:
            print("{} bigger than {}".format((self, other_box)))
        else:
            print("{} bigger than {}".format(other_box, self))
