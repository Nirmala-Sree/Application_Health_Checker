# Application Health Checker

The **Application Health Checker** is a Python-based script designed to monitor the status of websites or applications in real-time. This tool checks whether the websites or applications are up and responding by sending HTTP requests and verifying their status codes. It generates a CSV file containing the status of each URL and provides instant feedback in the console.

### Key Features

- **Real-Time Website Monitoring**: Continuously checks the availability of specified URLs and reports their status.
  - **Site Status Check**: Determines if the site is UP (Available) or DOWN (Not Responding).
  - **HTTP Status Code Monitoring**: Verifies the HTTP status codes to determine the availability and responsiveness of the site.
  
- **CSV Report**: Generates a `application_health_result.csv ` file with the URL and its corresponding status (UP or DOWN).

- **Console Alerts**: Prints the status of each site to the console in real-time, giving you immediate feedback on whether a site is available or not.

- **Error Handling**: Handles network errors, invalid URLs, and unreachable sites gracefully, providing informative error messages.

### Usage

To run the **Application Health Checker** script, follow these steps:

#### **Install Required Dependencies**  
Make sure you have Python installed on your system. You will also need to install the `requests` library, which is used to send HTTP requests to the URLs.

You can install the required dependency using pip:
```bash
pip install requests
```
### Running the Script

After installing the required dependencies, you can run the script directly from the command line:

```bash
python application_health_checker.py
```
### Monitoring the Websites

The script will read the list of URLs from the provided CSV file (`applications.csv`) and check their status one by one.

- If a site is **UP (Available)**, it will print to the console:  
  `Site [URL] is UP (Available).`
  
- If a site is **DOWN (Not Responding)**, it will print:  
  `Site [URL] is DOWN (Not Responding).`
  
 ### Stopping the Script

You can stop the script at any time by pressing `Ctrl+C`. The script will exit gracefully, showing the following message:

Monitoring stopped by user. Exiting the program...
### View Logs

The status of each URL check is recorded in the `application_health_result.csv ` file. You can open this file to review the status of all checked URLs.

