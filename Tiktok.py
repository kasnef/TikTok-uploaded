import os
import time
from colorama import Fore, Style
from multiprocessing import Process
from module.load_proxy_module import load_proxies
from module.check_data_module import check_ssid
from module.load_ssid_module import load_ssid
from module.upload_with_ssid_uc  import upload_videos_uc
from module.upload_with_ssid import upload_videos

os.system("cls")

def get_c_user_from_cookie(ssid):
    user = ssid.split(" ")[0]
    user_name = user[:6]
    return user_name

def run_process(ssid, caption, wait_time, browser_name):
    process_action = upload_videos_uc()
    c_user = get_c_user_from_cookie(ssid)
    browser_name_with_c_user = f"{browser_name}: {c_user} "
    process_action.run_upload_videos(ssid, caption, wait_time, browser_name_with_c_user)
    
if __name__ == "__main__":
    adminNoiti = Fore.CYAN + "Admin: "
    systemNoiti = Fore.GREEN + "System: "
    browserNoiti = Fore.MAGENTA + "Browser "
    warning = Fore.YELLOW + "Warn: "   
    error = Fore.RED + "Error: "
    browser_name = "ID "
    script_path = os.path.abspath(__file__) 
    src_directory = os.path.dirname(script_path)
    ssid_path = os.path.join(src_directory, 'data', 'ssid.txt')
    
    print(adminNoiti + Fore.WHITE + "Caption: ")
    caption = input()
    print(adminNoiti + Fore.WHITE + "Time(min): ")
    wait_time = float(input())
    print(adminNoiti + Fore.WHITE + "Num of process: ")
    len_count = int(input())
    print(Style.RESET_ALL)
    
    ssid_instance = load_ssid()
    ssid_values = ssid_instance.getSSid()
    processes = []
    
    check = check_ssid()    
    check_null = check.check_null_ssid()
    check_len = check.check_len_ssids(len_count)
    
    while True:
        
        if check_null and check_len:
            taken_ssid = ssid_values[:len_count]
            remaining_ssid = ssid_values[len_count:]
            
            ssid_list = taken_ssid

            with open(ssid_path, "w") as ssid_file:
                ssid_file.writelines(remaining_ssid)
                
        elif check_null and not check_len:
            ssid_list = ssid_values
            with open(ssid_path, "w") as ssid_file:
                ssid_file.writelines([])
                
        elif not check_null:
            print(adminNoiti + Fore.WHITE + "The program has stopped working because all ssid have been used up")
            break
        
        for ssid in ssid_list:
            ssid_login = ssid.strip()
            process = Process(target=run_process, args=(ssid_login, caption, wait_time, browser_name))
            processes.append(process)
            process.start()
            
        for process in processes:
            process.join()
            
        time.sleep(10000)
