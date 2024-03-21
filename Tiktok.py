import os
from colorama import Fore, Style
from multiprocessing import Process
from module.load_proxy_module import load_proxies
from module.check_data_module import check_ssid
from module.load_ssid_module import load_ssid
from module.upload_with_ssid import upload_videos
from module.upload_with_ssid_gologin import upload_videos as upload_videos_gologin

os.system("cls")
print("---------------------------------------------------------------------------- \n")
print("---------------------------------------------------------------------------- \n")
print("---------------------------------------------------------------------------- \n")

def get_c_user_from_cookie(ssid):
    start_index = ssid.find("csrf_session_id=")
    if start_index != -1:
        end_index = ssid.find(";", start_index)
        if end_index == -1:
            end_index = None
        c_user_value = ssid[start_index + len("csrf_session_id="):end_index]
        print(c_user_value)
        return c_user_value
    else:
        return None

def run_process(ssid, caption, wait_time, browser_name):
    process_action = upload_videos()
    c_user = get_c_user_from_cookie(ssid)
    browser_name_with_c_user = f"{browser_name}: {c_user} "
    process_action.run_upload_videos(ssid, caption, wait_time, browser_name_with_c_user)
    
def run_with_gologin(ssid, caption, wait_time, browser_name):
    process_action = upload_videos_gologin()
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
    
    print(adminNoiti + Fore.WHITE + "Choose 1 to using gologin and 2 to using webdriver: ")
    browser_choose = input()
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
        
        # proxy = "hanoi106.proxy.mkvn.net:10168:gj28X:89198"
        
        for ssid in ssid_list:
            ssid_login = ssid.strip()
            
            if browser_choose == "1":
                process = Process(target=run_with_gologin, args=(ssid_login, caption, wait_time, browser_name))
                processes.append(process)
                process.start()
            elif browser_choose == "2":
                process = Process(target=run_process, args=(ssid_login, caption, wait_time, browser_name))
                processes.append(process)
                process.start()
            else:
                print(error + Fore.WHITE + "Please choose 1 or 2")
                print(Style.RESET_ALL)
                break
            
        for process in processes:
            process.join()