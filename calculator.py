class BasicComputer:
    def __init__(self):
        self.memory = {}  # A simple memory dictionary to store values

    def display_memory(self):
        """Displays the current memory contents."""
        if not self.memory:
            print("Memory is empty.")
        else:
            print("Memory Contents:")
            for address, value in self.memory.items():
                print(f"Address {address}: {value}")

    def store(self, address, value):
        """Stores a value in a specific memory address."""
        self.memory[address] = value
        print(f"Stored {value} at address {address}.")

    def add(self, address1, address2, result_address):
        """Adds values from two memory addresses and stores the result."""
        if address1 in self.memory and address2 in self.memory:
            self.memory[result_address] = self.memory[address1] + self.memory[address2]
            print(f"Added values from address {address1} and {address2} -> Result stored at address {result_address}.")
        else:
            print("Error: One or both addresses do not exist.")

    def subtract(self, address1, address2, result_address):
        """Subtracts values from two memory addresses and stores the result."""
        if address1 in self.memory and address2 in self.memory:
            self.memory[result_address] = self.memory[address1] - self.memory[address2]
            print(f"Subtracted values from address {address1} and {address2} -> Result stored at address {result_address}.")
        else:
            print("Error: One or both addresses do not exist.")

    def multiply(self, address1, address2, result_address):
        """Multiplies values from two memory addresses and stores the result."""
        if address1 in self.memory and address2 in self.memory:
            self.memory[result_address] = self.memory[address1] * self.memory[address2]
            print(f"Multiplied values from address {address1} and {address2} -> Result stored at address {result_address}.")
        else:
            print("Error: One or both addresses do not exist.")

    def run(self):
        """Runs the basic computer interface."""
        print("Welcome to the Basic Computer!")
        print("Available commands: STORE, ADD, SUBTRACT, MULTIPLY, DISPLAY, EXIT")

        while True:
            command = input("\nEnter command: ").strip().upper()
            if command == "STORE":
                try:
                    address = input("Enter memory address: ")
                    value = int(input("Enter value to store: "))
                    self.store(address, value)
                except ValueError:
                    print("Error: Value must be an integer.")
            elif command == "ADD":
                address1 = input("Enter first memory address: ")
                address2 = input("Enter second memory address: ")
                result_address = input("Enter result memory address: ")
                self.add(address1, address2, result_address)
            elif command == "SUBTRACT":
                address1 = input("Enter first memory address: ")
                address2 = input("Enter second memory address: ")
                result_address = input("Enter result memory address: ")
                self.subtract(address1, address2, result_address)
            elif command == "MULTIPLY":
                address1 = input("Enter first memory address: ")
                address2 = input("Enter second memory address: ")
                result_address = input("Enter result memory address: ")
                self.multiply(address1, address2, result_address)
            elif command == "DISPLAY":
                self.display_memory()
            elif command == "EXIT":
                print("Exiting Basic Computer. Goodbye!")
                break
            else:
                print("Error: Invalid command. Please try again.")

# Run the Basic Computer
computer = BasicComputer()
computer.run()
