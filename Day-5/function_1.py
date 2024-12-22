# Write a function parse_logs(file_path: str) that reads a log file and returns the count of:

# Number of ERROR logs
# Number of WARNING logs
def parse_logs(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        print(lines)
    count = 0
    for x in lines:
        count += x.count("ERROR")
    print("ERROR appears", count)
    count = 0
    for y in lines:
        count += y.count("WARNING")
    print("WARNING appears", count)    


parse_logs("C:/Users/Dhanush/Documents/python_scripting/Day-5/text.txt")