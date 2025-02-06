import csv

def custom_round(value):
    num = float(value)
    if num % 1 < 0.5:  
        return int(num) % 10 + (num // 10) * 10
    else:
        return round(num)

input_file = "sales_24.csv"
output_file = "sales_updated.csv"

with open(input_file, mode="r", newline="") as infile:
    reader = csv.reader(infile)
    header = next(reader)
    
    rows = []
    for row in reader:
        if "Amount" in header:
            index = header.index("Amount")
            if row[index]:
                row[index] = custom_round(row[index])
        rows.append(row)


with open(output_file, mode="w", newline="") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(header)
    writer.writerows(rows)

print(f"Updated file: {output_file}")