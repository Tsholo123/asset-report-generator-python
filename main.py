import csv

def generate_report(file_path):
    total_assets = 0
    assigned = 0
    available = 0
    maintenance = 0

    print("=== Asset Report ===\n")

    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                total_assets += 1
                status = row['status']

                if status == "Assigned":
                    assigned += 1
                elif status == "Available":
                    available += 1
                elif status == "Maintenance":
                    maintenance += 1

                print(f"{row['asset_id']} - {row['asset_name']} ({row['asset_type']}) → {status}")

        print("\n=== Summary ===")
        print(f"Total Assets: {total_assets}")
        print(f"Assigned: {assigned}")
        print(f"Available: {available}")
        print(f"Maintenance: {maintenance}")

    except FileNotFoundError:
        print("Error: assets.csv file not found.")

if __name__ == "__main__":
    generate_report("assets.csv")
