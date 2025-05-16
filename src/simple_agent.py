import os

class SimpleAgent:
    def __init__(self, name="BasicAgent", openai_api_key=None):
        self.name = name
        self.openai_api_key = openai_api_key  # Store the API key
        self.available_actions = {
            "greet": self.greet,
            "say_hello": self.greet,
            "wave": self.wave,
            "thank_you": self.acknowledge_thanks,
            "goodbye": self.say_goodbye,
            "use_openai": self.use_openai_example  # Example action using OpenAI
        }

    def greet(self):
        print(f"{self.name} says: Hello!")

    def wave(self):
        print(f"{self.name} performs a friendly wave.")

    def acknowledge_thanks(self):
        print(f"{self.name} says: You're welcome!")

    def say_goodbye(self):
        print(f"{self.name} says: Goodbye!")

    def use_openai_example(self):
        if self.openai_api_key:
            print(f"{self.name} would use OpenAI with key: {self.openai_api_key[:8]}... (not actually using it yet)")
            # Here you would integrate with the OpenAI API
        else:
            print(f"{self.name} cannot use OpenAI because the API key is not provided.")

    def process_instruction(self, instruction):
        instruction = instruction.lower()
        for action_trigger, action_function in self.available_actions.items():
            if action_trigger in instruction:
                action_function()
                return True
        print(f"{self.name} doesn't understand the instruction: '{instruction}'")
        return False