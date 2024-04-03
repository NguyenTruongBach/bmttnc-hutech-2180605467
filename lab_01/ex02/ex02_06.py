# Nhập giá trị cho X và Y, mỗi giá trị được ngăn cách bởi dấu phẩy
input_str = input("Nhập X, Y: ")

# Chuyển giá trị đầu vào thành một danh sách gồm hai giá trị số nguyên
dimensions = [int(x) for x in input_str.split(',')]

# Ghép danh sách này thành hai biến riêng để lưu giá trị X và Y
rowNum, colNum = dimensions

# Tạo một danh sách 2 chiều để lưu các giá trị
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

# Gán giá trị tại mỗi vị trí trong danh sách 2 chiều
for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col] = row * col

# In kết quả
print(multilist)