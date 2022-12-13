from os import listdir


def file_finder(snd_dir, snd_filename):
    """
    snd_dir - daxiline gonderilmiş sistem fayl yolunu alar
    snd_filename - daxiline gönderilmiş fayl tipi (.csv , .txt , .html ve s.)
        ve fayl adları elece de fayl adlarının bir qismini alaraq
        mövcud fayl adlarını tapar ve bir list daxiline yığar
    """
    find_dir = listdir(snd_dir) # listdir verilmiş path daxilindeki faylları list olaraq return eder
    new_dirlist = list()
    for dir_walker in find_dir:
        if snd_filename in dir_walker:
            new_dirlist.append(dir_walker)
    return new_dirlist

def file_merge_list_create(snd_dirmrg, loc_merge_list):
    """
    Faylların tam yolunu yaradaraq bir liste yığar
    """
    new_merge_list = []
    apnd_full_path = ""
    last_symbol = snd_dirmrg[-1]
    esc_symbol = "\\"
    for filenamer in loc_merge_list:
        if last_symbol == esc_symbol:
            full_folder_path = snd_dirmrg
            apnd_full_path = snd_dirmrg + filenamer
        else:
            full_folder_path = snd_dirmrg + esc_symbol
            apnd_full_path = snd_dirmrg + esc_symbol + filenamer
        new_merge_list.append(apnd_full_path)
    return full_folder_path , new_merge_list

def merge_file_creater(folder_path , my_files , user_filename ):
    """
    Yeni faylı yaradar ve daxiline bütün metn
    elemntlerini verilmiş lis ardıcıllığı ile yığar 
    """
    new_text_filename = folder_path + user_filename + "_all.txt"
    new_file = open(new_text_filename, "w", encoding= "cp1252",errors='ignore')
    for file_read in my_files:
        text = open(file_read , "r", encoding= "cp1252", errors='ignore')
        has_read_text = text.read()
        new_file.write(has_read_text+"\n")
        text.close()
    return new_file.close(), new_text_filename

def app_starter():
    """
    Proqramı başladar
    """
    dir_input = input("Input your directory path:\n")
    filename_inp = input("Input your filename:\n")
    filename_list = file_finder(dir_input ,filename_inp)
    merge_list = file_merge_list_create (dir_input , filename_list)
    file_create = merge_file_creater ( merge_list[0] , merge_list[1] , filename_inp)
    return print(f"Operation Sucessufully. Your file path is:\n\n {file_create[1]} ")

app_starter()

