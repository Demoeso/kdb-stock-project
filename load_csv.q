system "p 5000"
/ load_csv.q - Minimal working script to load AAPL_daily.csv into a table

/ Step 1: Set the path to the CSV file (relative or full)
csvPath: `:AAPL_daily.csv

/ Step 2: Read file, skip header
lines: 1 _ read0 csvPath

/ Step 3: Define column types (Date, Float x4, Long)
types: ("DFFFFJ"; ",")

/ Step 4: Parse CSV data
data: types 0: lines

/ Step 5: Define column names
colnames: `timestamp`open`high`low`close`volume

/ Step 6: Flip into a table
stockTable: flip colnames!data

/ Step 7: Show the table
stockTable

