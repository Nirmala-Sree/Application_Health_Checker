import requests
import csv

# Function to check the status of a URL
def check_uptime(url):
    try:
        response = requests.get(url)
        # Check if the status code indicates the application is up (2xx codes)
        if 200 <= response.status_code < 300:
            return "UP (Available)"
        else:
            return "DOWN (Not Responding)"
    except requests.exceptions.RequestException as e:
        return "DOWN (Not Responding)"

# Function to read URLs from a CSV file and check their uptime
def check_apps_uptime(csv_file, result_file):
    # Open the result CSV file for writing
    with open(result_file, mode='w', newline='') as result_csv:
        result_writer = csv.writer(result_csv)
        result_writer.writerow(['URL', 'Status'])

        # Open the input CSV file and process each URL
        with open(csv_file, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:  # Ignore empty rows
                    url = row[0]
                    status = check_uptime(url)

                    # Print the status to the console in simple language
                    if "UP" in status:
                        print(f"Site {url} is UP (Available).")
                    else:
                        print(f"Site {url} is DOWN (Not Responding).")

                    # Write the result to the result CSV file
                    result_writer.writerow([url, status])

# Example usage
if __name__ == "__main__":
    # Path to your input CSV file (make sure it contains the URLs)
    csv_file = 'application_health_check.csv'  # Modify this path as necessary
    result_file = 'application_health_result.csv'  # Path to save the results
    check_apps_uptime(csv_file, result_file)
