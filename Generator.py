import json


class Coords:
    def __init__(self, key='C', scale=bool()):
        """ Simple class for generating coords given a key and scale (bool: major/minor)

            :param key: Coord key
            :param scale: True/False ==  Major/Minor
        """
        self.key = key
        self.major_scale = [2, 2, 1, 2, 2, 2, 1]
        self.minor_scale = [2, 1, 2, 2, 1, 2, 2]
        self.scale = self.major_scale if scale is True else self.minor_scale
        self.alfabet = ['A', 'Ais/Bes', 'B', 'C', 'Cis/Des', 'D', 'Dis/Es', 'E', 'F', 'Fis/Ges', 'G', 'Gis/As']

        self.coords = {
            'key': self.key,
            'scale': 'Major' if scale is True else 'Minor',
            'coords': {
                'a': [],  # e.g. ['a', b', 'Cis/Des']
                'b': [],
                'c': [],
                'd': [],
                'e': [],
                'f': [],
                'g': [],
            },
            'jazz': {'a': [], 'b': [], 'c': [], 'd': [], 'e': [], 'f': [], 'g': []}
        }  # <- used to store the coords created in self.generate(*args, **kwargs)

    def generate(self, jazz=False):
        # TODO: Create coords and store them in a dictionary (self.coords) for easy lookup
        pass

        # TODO: Extra is to create jazzy-coords ;)
        if jazz is True:
            pass

    def print_coord(self):
        print(json.dumps(self.coords, indent=2))


def main():
    coords = Coords(key='D', scale=False)
    coords.generate(jazz=True)
    coords.print_coord()


if __name__ == '__main__':
    main()

