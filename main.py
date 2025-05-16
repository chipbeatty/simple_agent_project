from dotenv import load_dotenv
import os
from src.simple_agent import SimpleAgent  # Assuming you might rename or have a more complex agent later

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    print("Error: OPENAI_API_KEY not found in .env file. Please ensure it's set.")
    exit()

if __name__ == "__main__":
    agent = SimpleAgent("MyFirstAgent", openai_api_key=openai_api_key) # Pass the key during initialization
    print(f"Starting {agent.name}. Type an instruction (e.g., 'greet', 'wave', 'thank you', 'goodbye'):")
    while True:
        instruction = input("> ")
        if instruction.lower() == "exit":
            break
        agent.process_instruction(instruction)
    print("Exiting.")