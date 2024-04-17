import psutil
import socket
import subprocess
import time
import os,sys
import threading


def is_window_exists_by_title(title):
    import win32gui
    try:
        # 定义回调函数，用于枚举所有窗口
        def enum_windows_proc(hwnd, lParam):
            if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) == title:
                lParam.append(hwnd)
            return True

        # 创建一个空列表，用于存储找到的窗口句柄
        hwnds = []
        # 枚举所有顶级窗口，并对每个窗口执行回调函数
        win32gui.EnumWindows(enum_windows_proc, hwnds)

        # 如果列表不为空，说明找到了具有指定标题的窗口
        return len(hwnds) > 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def is_self_already_running(if_exit=True, debug=False):
    """
    判断程序自身是否已经运行，如果参数if_exit为真，则直接退出。
    """
    current_process = psutil.Process()
    if debug:
        print(current_process.name(), current_process.pid)
    for proc in psutil.process_iter(["pid", "name"]):
        if debug:
            print(proc.info["name"], proc.info["pid"])
        # 检查进程名称和PID是否与当前进程相同
        if proc.info["name"] != "python.exe" and proc.info["name"] == current_process.name() and proc.pid != current_process.pid:
            if if_exit:
                sys.exit()
            return True
    return False


def exit_program(root=None):
    """
    退出程序，关闭 Tkinter 窗口并终止程序运行。

    :param root: Tkinter 的根窗口对象
    """
    if root is not None:
        root.quit()  # 关闭 Tkinter 窗口
    sys.exit()   # 终止程序运行



def open_config_file(file_to_open=None):
    """打开包含任务信息的文件"""
    os.startfile(file_to_open)  # 在默认程序中打开文件序中打开文件

def open_file_in_new_thread(filepath):

    def edit_file(filepath):
        subprocess.run(["notepad.exe", filepath])

    thread = threading.Thread(target=edit_file, args=(filepath,))
    thread.start()


def monitor_and_start_thread(thread, target, args):
    """
    检查线程是否在运行，如果没有运行，则启动它。
    
    :param thread: 要监测的线程对象
    :param target: 线程目标函数
    :param args: 传递给目标函数的参数
    """
    if not thread.is_alive():
        # 线程未在运行，启动线程
        thread = threading.Thread(target=target, args=args, daemon=True)
        thread.start()
        print("线程已启动")
    else:
        print("线程正在运行")

def is_program_running(exe_file_name):
    """检查指定的程序是否正在运行"""
    if ".exe" not in exe_file_name:
        exe_file_name += ".exe"
    for process in psutil.process_iter(["name"]):
        if process.info["name"].lower() == exe_file_name.lower():
            return True
    return False

def start_programe_in_new_process(full_path):
        # Windows平台的创建新进程组标志
    CREATE_NEW_PROCESS_GROUP, DETACHED_PROCESS = 0x00000200, 0x00000008

    subprocess.Popen([full_path], creationflags=DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP)

def restart_program(programe_path, program_name):
    try:
        # 结束进程
        subprocess.run(["taskkill", "/f", "/im", program_name], check=True)
        print(f"Program {program_name} has been terminated.")
    except subprocess.CalledProcessError as e:
        print(f"报错但应该是正常现象。有可能该进程本来就结束了，所以才需要修复。错误信息为：Error terminating program {program_name}: {e}")

    try:
        # 等待一段时间，确保进程已经完全结束
        time.sleep(2)
        # 重新启动进程
        # 假设程序在系统的PATH中，或者提供完整的路径
        # subprocess.run([programe_path + "/" + program_name], check=True)
        program_path = programe_path + "/" + program_name
        start_programe_in_new_process(program_path)
        print(f"Program {program_name} has been restarted.")
    except subprocess.CalledProcessError as e:
        print(f"Error starting program {program_name}: {e}")

def open_directory(dir_name):
    subprocess.Popen(r"explorer " + dir_name)


def open_file_in_new_thread(filepath):

    def edit_file(filepath):
        subprocess.run(["notepad.exe", filepath])

    thread = threading.Thread(target=edit_file, args=(filepath,))
    thread.start()


def check_processes_and_notice(task_list, notice_func=None, debug=False):
    # 检查事先定义好的进程是否已经启动，如果没有启动，就执行指定的操作。
    if debug:
        print("enter check_processes")

    # 先取所有进程及子进程名字到一个集合里面。类似('updater.exe', 'hipsdaemon.exe', 'python.exe', 'tdxw.exe', 'dbsvr_abc.exe', 'atiesrxx.exe', 'comppkgsrv.exe', 'qqprotect.exe', 'mysqld.exe'...)
    all_set = get_all_process_with_child()
    result_dict = {}
    if debug:
        print(all_set)
    for to_check_process in task_list:
        if os.path.basename(to_check_process).lower() in all_set:
            result_dict[to_check_process] = True
    # result_dict = lyyprocess.get_result_dict_from_set(all_set, task_dict)

    if debug:
        print("result_dict", result_dict)
    # 把路径去掉。false_keys ['D:/Soft/_lyytools/_jiepan/_jiepan.exe', 'D:/Soft/_lyytools/f1999/f1999.exe']
    false_keys = [os.path.basename(key) for key in task_list if key not in result_dict.keys()]
    if debug:
        print("false_keys", false_keys)
    if false_keys and notice_func:
        notice_func(" 和 ".join(false_keys) + "未运行", "请及时检查")


def if_set_include_list_element(all_set, task_dict):
    """
    判断要检查的程序（在字典中的元素）是否被包含在全体进程集合中，从而不管是否子进程，都能正确找到。

    """
    print("all_set length=", len(all_set))
    result_dict = {}
    for item in all_set:
        found = False  # 标记是否找到匹配的任务
        for task in task_dict.keys():
            if task in item:
                result_dict[task] = True
                found = True
                break  # 只跳出当前的内部循环
        if found:
            continue  # 继续下一个外部循环
    return result_dict


def get_all_process_with_child():
    """
    获取当前运行的所有进程及子进程名字，存入集合中。
    """
    all_set = set()
    for proc in psutil.process_iter(["pid", "name"]):
        try:
            proc_info = proc.as_dict(attrs=["pid", "name"])
            process_name = proc_info["name"].lower()
            all_set.add(process_name)
            print("+", end="", flush=True)
            child_procs = psutil.Process(proc_info["pid"]).children(recursive=True)
            for child_proc in child_procs:
                child_proc_info = child_proc.as_dict(attrs=["pid", "name"])
                child_process_name = child_proc_info["name"].lower()
                all_set.add(child_process_name)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return all_set


def get_all_process_hwnd_dict():
    """
    获取当前运行的所有进程及子进程名字，存入字典中。
    """
    hwnd_dict = {}
    for proc in psutil.process_iter(["pid", "name"]):
        try:
            proc_info = proc.as_dict(attrs=["pid", "name"])
            process_name = proc_info["name"].lower()

            if process_name not in hwnd_dict.keys():
                hwnd_dict[process_name] = proc_info["pid"]

            print("+", end="", flush=True)
            child_procs = psutil.Process(proc_info["pid"]).children(recursive=True)
            for child_proc in child_procs:
                child_proc_info = child_proc.as_dict(attrs=["pid", "name"])
                child_process_name = child_proc_info["name"].lower()
                if child_process_name not in hwnd_dict.keys():
                    hwnd_dict[child_process_name] = proc_info["pid"]
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return hwnd_dict


def check_processes(task_dict):
    """
    检查指定的进程是否在运行，如果没有运行，打印出来，并返回。用来通知哪些没运行。
    """
    print("enter check_processes, try to find name in all process and child process")
    false_list = []
    all_set = get_all_process_with_child()
    result_dict = if_set_include_list_element(all_set, task_dict)
    print("result_dict", result_dict)
    false_keys = [key for key in task_dict.keys() if key not in result_dict.keys()]
    print("false_keys", false_keys)
    if false_keys:
        print(" 和 ".join(false_keys) + "未运行", "请及时检查")
    false_list = [x for x in false_keys if x in task_dict.keys()]
    return false_keys


def check_port_in_use(port):
    # 检查指定端口是否被占用
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind(("localhost", port))
        except OSError:
            print("# 端口被占用，查找占用端口的进程")
            for conn in psutil.net_connections():
                if conn.status == "LISTEN" and conn.laddr.port == port:
                    pid = conn.pid
                    process = psutil.Process(pid)
                    print(f"# 占用端口的进程名：{process.name()}，进程路径：{process.exe()}")
                    return process.name(), process.exe()
    return None, None



def kill_process_by_path(executable_path):
    for proc in psutil.process_iter(["pid", "exe"]):
        if proc.info["exe"] == executable_path:
            try:
                proc.kill()
                print(f"已结束进程 PID: {proc.pid}")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
                print(f"无法结束进程 PID: {proc.pid}, 错误: {e}")




def kill_process_by_name(path):
    for proc in psutil.process_iter(["name"]):
        if proc.info["name"] == name:
            proc.kill()

def kill_process_by_name(name):
    for proc in psutil.process_iter(["name"]):
        if proc.info["name"] == name:
            proc.kill()

def kill_process_by_title_and_exe(window_title, exe_name):

    try:
        # 使用 wmic 命令查询具有特定窗口标题的进程的进程ID
        result = subprocess.run(["wmic", "process", "where", f"name='{exe_name}' and windowtitle='{window_title}'", "get", "/value"], capture_output=True, text=True, check=True)
        pid = result.stdout.strip()  # 获取进程ID

        # 使用 taskkill 命令结束特定的进程
        subprocess.run(["taskkill", "/f", "/pid", pid], check=True)
        print(f"进程 {pid} 已被结束。")
    except subprocess.CalledProcessError as e:
        print(f"无法结束进程: {e}")

def terminate_process_using_port(port):
    try:
        command = f"netstat -ano | findstr :{port}"
        output = subprocess.check_output(command, shell=True, text=True)
        lines = output.strip().split("\n")
        for line in lines:
            parts = line.split()
            pid = int(parts[-1])
            subprocess.run(["taskkill", "/F", "/PID", str(pid)])
        print("已结束占用该端口的程序")
        return pid
    except (subprocess.CalledProcessError, ValueError) as e:
        print(f"结束占用该端口的程序时出现错误：{e}")
        return None


def run_with_error_handling(func, *args, **kwargs):
    try:
        func(*args, **kwargs)
    except Exception as e:
        # 处理异常，可以打印日志或执行其他操作
        print(f"模块 {func.__name__} 出现异常: {e}")


def get_child_process_number(parent_name="JY-Main.exe", debug=False):
    parent_pid = None
    # 查找主进程
    for process in psutil.process_iter(["pid", "name", "cmdline"]):
        process_info = process.info
        if parent_name.lower() in process_info["name"].lower():
            parent_pid = process_info["pid"]
            break
        elif debug:
            print(process_info["name"])

    if parent_pid is None:
        print(f"没有找到名为 {parent_name} 的进程")
        return 0
    # print(f"找到名为 {parent_name} 的进程，其PID为 {parent_pid}")
    parent = psutil.Process(parent_pid)
    # 列举子进程
    children = parent.children()
    if children:
        for child in children:
            print(f"  PID: {child.pid}, 名称: {child.name()}")
    # 列举子线程

    # if main_thread:
    #     for thread_id, thread_obj in threading._active.items():
    #         if thread_obj.ident != main_thread.ident:
    #             #print(f"  Thread ID: {thread_obj.ident}")
    print("子线程数量为：", len(children))
    return len(children)


def get_hwnd(process_name):
    for proc in psutil.process_iter(["pid", "name"]):
        try:
            proc_info = proc.as_dict(attrs=["pid", "name"])
            if process_name.lower() in proc_info["name"].lower():
                return proc_info["pid"]
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass


def set_window_on_top(process):
    if process is not None:
        process.nice(psutil.HIGH_PRIORITY_CLASS)
        print(f"已将进程 {process.pid} 置顶")
    else:
        print("未找到名为 'kingtrade' 的进程")




if __name__ == "__main__":
    print(check_port_in_use(3306))
    kill_process_by_name("notepad.exe")

    exit()
    task_dict = {"jiepan": "D:/Soft/_lyytools/_jiepan/_jiepan.exe", "gui-only": "D:/Soft/_lyytools/gui-only/gui-only.exe", "kingtrader": "D:/Soft/_Stock/KTPro/A.点我登录.exe"}
    stopped = check_processes(task_dict)
    print("stopped=", stopped)
