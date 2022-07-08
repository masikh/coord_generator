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
            'coords': {x: [] for x in self.alfabet}  # Create a dict from self.alfabet e.g. {'A': [], ...}
        }  # <- data structure used to store the coords created in self.generate()

    def get_key_notes(self):
        # Get the index in alfabet of our key
        index = self.alfabet.index(self.key)

        # Get the notes from the alfabet belonging to our key
        key_notes = list()
        for i in range(len(self.scale)):
            key_notes.append(self.alfabet[index % 12])  # On overflow modulo will keep us on track
            index += self.scale[i]  # Increment the index with the scale-steps
        return key_notes

    def generate(self):
        # Get the notes belonging to our key and scale
        key_notes = self.get_key_notes()

        # Create coords in key
        length = len(key_notes)
        for i in range(length):
            coord_tones = [key_notes[i % length], key_notes[(i + 2) % length], key_notes[(i + 4) % length]]
            self.coords['coords'][key_notes[i]] = coord_tones

        # Cleanup coords not part of the key
        coords = self.coords['coords']
        self.coords['coords'] = {x: coords[x] for x in coords if len(coords[x])}  # 0 == False

    def print_coord(self):
        print(json.dumps(self.coords, indent=2))  # json dumps coverts a dict to a string, indent makes it pretty


def main():
    coords = Coords(key='C', scale=True)  # Create a class instance
    coords.generate()  # Call class methods ...
    coords.print_coord()


if __name__ == '__main__':
    main()  # <- Programs entry point

