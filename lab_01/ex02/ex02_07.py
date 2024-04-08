# Print a prompt asking the user to enter text
print("Nhập các dòng văn bản (Nhập 'done' để kết thúc):")

# Create an empty list to store the input lines
lines = []

# Keep accepting input lines until the user enters 'done'
while True:
    line = input()
    if line.lower() == 'done':
        break
    else:
        # Convert the input line to lowercase and append it to the list
        lines.append(line.lower())

# Convert all the lines to uppercase and print them
print("\nCác dòng đã nhập sau khi chuyển thành chữ in hoa:")
for line in lines:
    print(line.upper())