

class Animal():
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f'{self.name} makes "{self.sound}"')

print("Out of if statement")

if __name__ == "__main__":

    print("\n--- Program started ---\n")

    a = Animal('Cat', "miauuu")
    a.make_sound()

    print("\n--- Program ended ---\n")
