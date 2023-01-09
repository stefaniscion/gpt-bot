import json

def load_memory(file):
    with open(file, 'r') as f:
        memory = json.load(f)
        return memory

def save_memory(file, memory):
    with open(file, 'w') as f:
        json.dump(memory, f)