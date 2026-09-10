def main():
    inventory = 0
    total_units_processed = 0
    failed_entries = 0


while True:
        user_input = input("Enter stock quantity (or type 'quit' to stop): ").strip()
 
        # Exit condition
        if user_input.lower() == "quit":
            break