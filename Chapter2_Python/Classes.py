class Animal:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def jump(self):
        print("jump")


def main():
    dog = Animal(10, 0.8)
    print(dog.height, dog.weight)
    cat = Animal(3, 0.3)
    print(cat.height, cat.weight)
    dog.jump()


if __name__ == "__main__":
    main()
