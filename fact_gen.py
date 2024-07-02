# Simple Python code to print something interesting after user input
import random

def get_fun_fact(name):
    # List of fun facts
    fun_facts = [
        "Space Smell: Astronauts returning from space have described the smell of space as a mixture of hot metal and grilled steak."
    ]
    # Randomly select a fun fact
    fact = random.choice(fun_facts)
    return f"Hello {name}, {fact}"

# Get user input
name = input("Please enter your name: ")

# Print personalized message with a fun fact
print(get_fun_fact(name))

