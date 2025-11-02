class Person:
    '''
    A class representing a person in a social network.
    Attributes:
        name (str): The name of the person.
        friends (list): A list of friends (Person objects).
    Methods:
        add_friend(friend): Adds a friend to the person's friend list.
    '''
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)


class SocialNetwork:
    '''
    A class representing a social network.
    Attributes:
        people (dict): A dictionary mapping names to Person objects.
    Methods:
        add_person(name): Adds a new person to the network.
        add_friendship(person1_name, person2_name): Creates a friendship between two people.
        print_network(): Prints the names of all people and their friends.
    '''
    def __init__(self):
        self.people = {}

    def add_person(self, name):
        if name not in self.people:
            self.people[name] = Person(name)
        else:
            print(f"{name} already exists in the network.")

    def add_friendship(self, person1_name, person2_name):
        if person1_name not in self.people or person2_name not in self.people:
            print(f"Friendship not created. One or both people do not exist!")
            return

        person1 = self.people[person1_name]
        person2 = self.people[person2_name]

        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        for name, person in self.people.items():
            friends_names = [friend.name for friend in person.friends]
            print(f"{name} is friends with: {', '.join(friends_names)}")


# Example Usage
if __name__ == "__main__":
    network = SocialNetwork()

    # Add people
    network.add_person("Alex")
    network.add_person("Jordan")
    network.add_person("Morgan")
    network.add_person("Taylor")
    network.add_person("Casey")
    network.add_person("Riley")

    # Add friendships
    network.add_friendship("Alex", "Jordan")
    network.add_friendship("Alex", "Morgan")
    network.add_friendship("Jordan", "Taylor")
    network.add_friendship("Morgan", "Casey")
    network.add_friendship("Taylor", "Riley")
    network.add_friendship("Casey", "Riley")
    network.add_friendship("Morgan", "Riley")
    network.add_friendship("Alex", "Taylor")

    # Test adding a friendship where someone doesn't exist
    network.add_friendship("Jordan", "Johnny")

    # Print network
    network.print_network()
"""
Design Memo – Social Network Graph

I chose to use a graph data structure to model this social network because it naturally represents relationships between individuals. Each person is a node, and each friendship is a bidirectional edge, which allows us to easily capture the mutual connections that occur in real-life social networks. Unlike a list or tree, a graph allows any user to connect with any other user dynamically without enforcing a strict hierarchy or order, making it ideal for representing complex and evolving social relationships.

In this implementation, the Person class stores individual users and their list of friends, while the SocialNetwork class manages the overall network using a dictionary. The dictionary allows fast access to any person by name, which is important for efficiently adding friendships and searching the network. Friendships are implemented bidirectionally by adding each person to the other’s friends list, ensuring the network accurately reflects mutual connections.

Collision handling for duplicate friendships is managed by checking whether a friend already exists in the list before adding, which prevents redundant entries. Attempting to add a friendship with a non-existent user is gracefully handled with an informative message, which ensures the integrity of the network data.

Performance-wise, adding a new person is very fast because it simply inserts into the dictionary. Adding a friendship is efficient as it involves updating two small lists, though printing the entire network takes longer as it iterates over all people and their friends. Overall, the graph structure provides the flexibility and speed needed to represent a real-world social network while allowing for easy expansion as new users and connections are added.

Using a graph rather than a list or tree provides the best combination of flexibility, efficiency, and accuracy for modeling dynamic, bidirectional social relationships.
"""
