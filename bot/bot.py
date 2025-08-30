import re
import os
from typing import List, Set

def is_valid_ethereum_address(address: str) -> bool:
    """Check if a string is a valid Ethereum address"""
    pattern = r'^0x[a-fA-F0-9]{40}$'
    return bool(re.match(pattern, address))

def extract_addresses(file_path: str) -> List[str]:
    """Extract all Ethereum addresses from a text file"""
    addresses = set()  # Using set to automatically handle duplicates
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Remove any whitespace and check if line looks like an address
                line = line.strip()
                if is_valid_ethereum_address(line):
                    addresses.add(line.lower())  # Convert to lowercase for case-insensitive comparison
    except Exception as e:
        print(f"Error reading file: {e}")
        return []
    
    return sorted(list(addresses))

def save_addresses(addresses: List[str], output_file: str, amount: str = "0.00001458") -> bool:
    """Save addresses to a file, one per line with amount"""
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            for addr in addresses:
                file.write(f"{addr} {amount}\n")
        return True
    except Exception as e:
        print(f"Error saving to file: {e}")
        return False

def main():
    input_file = 'addr.txt'
    output_file = 'unique_addresses.txt'
    
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found in the current directory.")
        return
    
    print(f"Processing {input_file}...")
    
    # Extract and deduplicate addresses
    addresses = extract_addresses(input_file)
    
    if not addresses:
        print("No valid Ethereum addresses found in the file.")
        return
    
    print(f"Found {len(addresses)} unique Ethereum addresses.")
    
    # Save to file with amount
    amount = "0.0001458"
    if save_addresses(addresses, output_file, amount):
        print(f"Successfully saved {len(addresses)} addresses with amount {amount} to {output_file}")
    
    # Show some statistics
    print("\nFirst 5 addresses with amounts:")
    for addr in addresses[:5]:
        print(f"- {addr} {amount}")
    
    if len(addresses) > 5:
        print(f"... and {len(addresses) - 5} more")

if __name__ == "__main__":
    main()
