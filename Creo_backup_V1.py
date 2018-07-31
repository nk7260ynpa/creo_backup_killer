import glob
import os

# 搜尋並擷取檔名
all_files = glob.glob("*")
final_list = []
# 分離最後的副檔名
for all_file in all_files:
    part_name = all_file.split(".")
    # 驗證為creo檔案
    try:
        int(part_name[-1]) > 0
        del part_name[-1]
        file_name = ".".join(part_name)
        final_list.append(file_name)
    except:
        continue
final_set = set(final_list)
all_file = []
for kind in final_set:
    all_file.append(kind)

for d in all_file:
    d_str = (d + ".*")
    d_name = glob.glob(d_str)
    d_number = len(d_name)
    for d_part in range(1, len(d_name)):
        del_name = (d + "." + str(d_part))
        print(del_name)
        os.remove(del_name)

all_files = glob.glob("*")
final_list = []
old_name_list = []
# 分離最後的副檔名
for all_file in all_files:
    part_name = all_file.split(".")
    # 驗證為creo檔案
    try:
        int(part_name[-1]) > 0
        old_name = ".".join(part_name)
        # 刪除最後一碼
        del part_name[-1]
        file_name = ".".join(part_name)
        os.rename(old_name, (file_name + ".1"))
    except:
        continue

exit(0)
