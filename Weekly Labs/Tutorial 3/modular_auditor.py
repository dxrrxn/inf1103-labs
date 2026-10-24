
TAX_RATE = 0.10          # 10% tax on each delivery
QUIT_SIGNAL = "quit"
OVERSTOCK_LIMIT = 500 

def get_valid_input():
    """Prompt once, validate, and return an int, the quit signal, or None."""
    user_input = input("Enter stock quantity (or type 'quit' to stop): ").strip()

    if user_input.lower() == QUIT_SIGNAL:
        return QUIT_SIGNAL

    if not user_input.isdigit():
        print(f"Error: '{user_input}' is not a valid number. Please try again.")
        return None

    return int(user_input)


def process_delivery(current_total, new_value):
    """Add the delivery to the running total and return the new total."""
    return current_total + new_value

def calculate_tax(amount):
    """Return the tax (10%) owed on this specific delivery."""
    return amount * TAX_RATE

def generate_report(total_units, failed_attempts, deliveries_processed=0, total_tax=0.0):
    """Print the final audit summary."""
    print("\n----- Inventory Audit Report -----")
    print(f"Total Deliveries Processed: {deliveries_processed}")
    print(f"Total Units Processed: {total_units}")
    print(f"Total Tax Calculated: {total_tax:.2f}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")
    print("----------------------------------")

def main():
    inventory = 0
    total_units_processed = 0
    failed_entries = 0

    while True:
        user_input = input("Enter stock quantity (or type 'quit' to stop): ").strip()

        if user_input.lower() == "quit":
            break

        
        if not user_input.isdigit():
          
            print(f"Error: '{user_input}' is not a valid number. Please try again.")
            failed_entries += 1
            continue
        elif int(user_input) < 0:
            print("Error: Negative stock quantities are not allowed.")
            failed_entries += 1
            continue
        else:
            quantity = int(user_input)

            inventory += quantity
            total_units_processed += quantity


            if inventory > 500:
                print(f"OVERSTOCK ALERT! Inventory has reached {inventory} units, "
                      f"exceeding the 500-unit limit.")
                break
            else:
                print(f"Stock added. Current inventory: {inventory}")

    print("\n----- Inventory Audit Report -----")
    print(f"Total Units Processed: {total_units_processed}")
    print(f"Number of Failed/Rejected Entries: {failed_entries}")
 
 
if __name__ == "__main__":
    main()
 