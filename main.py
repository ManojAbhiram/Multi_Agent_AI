from agents.classifier_agent import ClassifierAgent
from memory.shared_memory import SharedMemory

def main():
    memory = SharedMemory()
    classifier = ClassifierAgent(memory)

    files = [
        "inputs/sample_email.txt",
        "inputs/sample_data.json",
        "inputs/sample_invoice.pdf"
    ]

    for f in files:
        print(f"\nProcessing: {f}")
        result = classifier.process(f)
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
