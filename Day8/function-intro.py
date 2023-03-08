def greet(name,location):
    print(f"Hello {name} from {location}")
    print(f"how is the weather in {location}?")
    print(f"good bye {name}")


name = input("What is your name? ")
location = input("Where are you from? ")
greet(name=name,location=location)