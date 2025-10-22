# Akamai Technologies Shares Outstanding

## Summary
This application fetches the number of shares outstanding for Akamai Technologies from the SEC API and displays the maximum and minimum values along with their fiscal years.

## Setup
1. Clone the repository.
2. Ensure you have Python installed.
3. Run `main.py` to fetch data and create `data.json`.

## Usage
Open `index.html` in a web browser. You can also pass a CIK as a query parameter (e.g., `index.html?CIK=0001018724`) to fetch data for a different company.

## Code Explanation
- `main.py`: Fetches data from the SEC API, processes it, and saves it to `data.json`.
- `index.html`: Displays the data and updates dynamically based on the CIK query parameter.

## License
MIT License

## Description
This app provides a simple interface to view the shares outstanding for Akamai Technologies and allows for dynamic fetching of data for other companies using their CIK.
