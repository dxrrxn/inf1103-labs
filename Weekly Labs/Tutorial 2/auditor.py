
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
 