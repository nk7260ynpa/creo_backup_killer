import glob
import os


#此段程式在找出creo的所有檔案
def catch_creo():
    all_files = glob.glob("*")
    creo_files = []
    for all_file in all_files:
        part_all_file = all_file.split(".")
        try:
            int(part_all_file[-1]) > 0
            creo_files.append(all_file)
        except:
            continue
    return (creo_files)

#找出多餘的檔案
def find_unnecessary(all_creo_files):
    all_creo_part_list=[]
    for all_creo_file in all_creo_files:
        explode_name=all_creo_file.split(".")
        explode_name.pop()
        explode_name=".".join(explode_name)
        all_creo_part_list.append(explode_name)
        all_creo_part_list=list(set(all_creo_part_list))
    del_file_list=[]
    for del_part_name in all_creo_part_list:
        del_number=len(glob.glob(del_part_name+".*"))
        for d_file in range(1,del_number):
            del_file_name=(del_part_name+"."+str(d_file))
            del_file_list.append(del_file_name)
    return(del_file_list)

#刪除多餘的檔案
def del_unnecessary(unnecessary):
    for del_file in unnecessary:
        try:
            os.remove(del_file)
        except:
            continue

#將所有檔案重新命名
def file_rename():
    rename_file_list=catch_creo()

    for rename_file in rename_file_list:
        rename_file_part=rename_file.split(".")
        rename_file_part[-1]=str(1)
        newname_file=".".join(rename_file_part)
        os.rename(rename_file,newname_file)

#主程式
creo_file=catch_creo()
unnecessary_file=find_unnecessary(creo_file)
del_unnecessary(unnecessary_file)
file_rename()
exit(0)
