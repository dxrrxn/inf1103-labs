def main():
    inventory = 0
    total_units_processed = 0
    failed_entries = 0


while True:
        user_input = input("Enter stock quantity (or type 'quit' to stop): ").strip()
 
        # Exit condition
        if user_input.lower() == "quit":
            break

        if not user_input.isdigit():
            # Step 4: Reject non-numeric input (e.g. "ten")
            print(f"Error: '{user_input}' is not a valid number. Please try again.")
            failed_entries += 1
            continue
        