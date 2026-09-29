
TAX_RATE = 0.10          # 10% tax on each delivery
QUIT_SIGNAL = "quit"
OVERSTOCK_LIMIT = 500 
INVENTORY_FILE = "inventory.txt"  # File to persist inventory data


def load_inventory():
    """Read the saved total and history from INVENTORY_FILE.

    Returns (0, []) if the file is missing, empty or unreadable, so a
    first run works without error.
    """
    try:
        with open(INVENTORY_FILE, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"No {INVENTORY_FILE} found - starting with an empty inventory.")
        return 0, []

    total = 0
    history = []

    if len(lines) >= 1 and lines[0].strip().isdigit():
        total = int(lines[0].strip())

    if len(lines) >= 2 and lines[1].strip():
        for item in lines[1].strip().split(","):
            item = item.strip()
            if item.isdigit():
                history.append(int(item))

    print(f"Loaded {INVENTORY_FILE}: {total} units, {len(history)} past transactions.")
    return total, history

def save_inventory(total, history):
    """Write the final total and the transaction history to INVENTORY_FILE."""
    with open(INVENTORY_FILE, "w") as f:
        f.write(f"{total}\n")
        f.write(",".join(str(amount) for amount in history) + "\n")
    print(f"Saved {total} units and {len(history)} transactions to {INVENTORY_FILE}.")

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

def generate_report(total_units, failed_attempts, deliveries_processed=0,
                    total_tax=0.0, history=None):
    """Print the final audit summary."""
    if history is None:
        history = []

    print("\n----- Inventory Audit Report -----")
    print(f"Total Deliveries Processed: {deliveries_processed}")
    print(f"Total Units in Inventory: {total_units}")
    print(f"Total Tax Calculated: {total_tax:.2f}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")
    print(f"Transaction History: {history}")
    print("----------------------------------")
    
def main():
    # 1. Persistence: load whatever was saved last time
    inventory, history = load_inventory()

    # Counters for this session only
    deliveries_processed = 0
    failed_entries = 0
    total_tax = 0.0

    # 2. Keep asking until the user quits
    while True:
        entry = get_valid_input()

        if entry == QUIT_SIGNAL:
            break

        if entry is None:
            failed_entries += 1
            continue

        # 3. Valid value: update total, tax, history and counters
        inventory = process_delivery(inventory, entry)
        total_tax += calculate_tax(entry)
        history.append(entry)
        deliveries_processed += 1

        if inventory > OVERSTOCK_LIMIT:
            print(f"OVERSTOCK ALERT! Inventory has reached {inventory} units, "
                  f"exceeding the {OVERSTOCK_LIMIT}-unit limit.")
            break

        print(f"Stock added. Current inventory: {inventory}")

    # 4. Write-back, then report
    save_inventory(inventory, history)
    generate_report(inventory, failed_entries, deliveries_processed, total_tax, history)

if __name__ == "__main__":
    main()
 