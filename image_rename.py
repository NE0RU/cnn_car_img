import os


file_n = input("Input file name: ")

# 주어진 디렉토리에 있는 항목들의 이름을 담고 있는 리스트를 반환합니다.
# 리스트는 임의의 순서대로 나열됩니다.
file_path = 'images/' + file_n
file_names = os.listdir(file_path)
print(file_names)

# i = 1
# for name in file_names:
#     src = os.path.join(file_path, name)
#     dst = str(i) + '.jpg'
#     dst = os.path.join(file_path, dst)
#     os.rename(src, dst)
#     i += 1

i = 1
for name in file_names:
    src = os.path.join(file_path, name)
    dst = file_n + '_' + str(i) + '.jpg'
    dst = os.path.join(file_path, dst)
    os.rename(src, dst)
    i += 1