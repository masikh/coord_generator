class Coords:
    def __init__(self, key='C', coord_type=bool()):
        """

        :param key: Coord key
        :param coord_type: True/False ==  Major/Minor
        """
        self.key = key
        self.coord_type = 'major' if coord_type is True else 'minor'
        self.alfabet = ['A', 'Ais/Bes', 'B', 'C', 'Cis/Des', 'D', 'Dis/Es', 'E', 'F', 'Fis/Ges', 'G', 'Gis/As']
        self.major_scale = [2, 2, 1, 2, 2, 2, 1]
        self.minor_scale = []

    def generate(self, jazz=False):
        # Nu doe ik dit
        pass

    def print_coord(self):
        print('Key:', self.key)
        print('Type:', self.coord_type)


def main():
    coords = Coords(key='D', coord_type=False)
    coords.generate(jazz=True)
    coords.print_coord()


if __name__ == '__main__':
    main()

