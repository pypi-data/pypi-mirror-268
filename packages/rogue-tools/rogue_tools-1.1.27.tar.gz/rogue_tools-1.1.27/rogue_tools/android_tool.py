import time
import re
import os
import sys
import subprocess
import traceback
from rogue_tools import android_tool,time_tool,thread_tool,path_tool
from loguru import logger



def add_root_path_for_airtest(src_path):
    '''
    传入启动脚本的位置,一般情况下是 : src_path = os.path.realpath(__file__)
    '''
    try:
        root_path=os.path.join(os.path.split(src_path)[0], "..", "..", "..", "..", "..")
        if not root_path in sys.path:
            sys.path.append(root_path)
    except BaseException:
        traceback.print_exc()

class Android():
    def __init__(self,adb_path,device_name,device_brand) -> None:
        self.device_name = device_name
        self.adb_path = adb_path
        self.device_brand = device_brand

    def adb_execute(self,cmd):
        adb = f'{self.adb_path} -s {self.device_name}  {cmd}'
        logger.debug(adb)
        result = subprocess.run(adb, capture_output=True, text=True, shell=True)
        return result.stdout.split('\n')


class DevicesManager(metaclass=thread_tool.Singleton):
    def __init__(self) -> None:
        self.adb_path = 'adb'
        self.devices:dict[Android] = {}
        self.devices_name = {}
        self.tp = thread_tool.ThreadPool()
        #self.init_device_dic(60)

    def __del__(self):
        self.tp.shutdown()

    def set_adb(self,adb_exe):
        '''设置用于命令行的adb执行器'''
        self.adb_path = adb_exe

    def get_all_connected_devices(self):
        result = subprocess.run(f'{self.adb_path} devices', capture_output=True, text=True, shell=True)
        # 提取设备名称，忽略空行
        devices_name = [
            re.match(r'(\S+)\s+device', line).group(1) 
            for line in result.stdout.split('\n')[1:]
            if re.match(r'(\S+)\s+device', line)
        ]
        return devices_name

    def connect(self, device_dic:dict,try_times=15):
        '''连接设备'''
        
        for device in device_dic:
            try:
                subprocess.run(f'{self.adb_path} connect {device}', capture_output=True, text=True, shell=True)
            except BaseException:
                logger.warning(f'connect {device} failed')

        for _ in range(try_times):
            # 运行 adb devices 命令，获取连接的设备信息
            self.devices_name = self.get_all_connected_devices()
            logger.debug(f'connecting:{self.devices_name}')

            # 创建设备对象字典
            self.devices = {}
            for device in self.devices_name:
                device_brand =  device_dic.get(device,None)
                if device_brand:
                    self.devices[device] = Android(self.adb_path, device,device_brand) 
            print(self.devices)
            # 如果找到设备，停止循环
            if self.devices:
                logger.debug(f'find {self.devices}')
                self.device_name_list = [device for device in self.devices]
                print(self.device_name_list)
                return
            # 等待一秒再尝试
            time.sleep(1)



    def kill_adb_server(self):
        adb = f'{self.adb_path} kill-server'
        return subprocess.run(adb, capture_output=True, text=True, shell=True)

    def get_device_name_list(self):
        return self.device_name_list
    
    def run_in_all(self, adb_cmd, device_name=None,in_thread=True):
        '''用于执行命令,多设备会自动转为多线程模式'''
        loop_dic = {device_name: self.devices.get(device_name)} if device_name else self.devices
        if in_thread:
            rs_dic = {device_name: result for device_name, result in self.tp.map(
                lambda d: (d[0], d[1].adb_execute(adb_cmd)),
                loop_dic.items()
            )}
        else:
            rs_dic = {device_name: loop_dic[device_name].adb_execute(adb_cmd) for device_name in loop_dic}
        print(rs_dic,loop_dic)
        return rs_dic

    def get_apk_info(self, device_name=None):
        '''获得当前处于活动状态的apk的包名和主活动名字,需要先将app置于活动状态'''
        rs_dic = {}
        dumpsys_window_cmd = 'shell dumpsys window'
        window_info_dic = self.run_in_all(dumpsys_window_cmd, device_name)

        # 用于匹配主活动名的正则表达式
        def extract_apk_info(line):
            activity_match = re.search(r'mFocusedWindow=\S+ \S+ (\S+/\S+)}', line)
            if activity_match:
                package_name, activity_name = activity_match.group(1).split('/')
                return package_name, activity_name
            return None, None

        for device_name,window_info_list in window_info_dic.items():
            rs_dic[device_name]=next((extract_apk_info(line) for line in window_info_list if extract_apk_info(line) != (None, None)), (None, None))
        return rs_dic


    def get_installed_apk(self, device_name=None):
        '''获取已安装的apk列表'''
        install_dic = self.run_in_all('shell pm list packages', device_name)
        # 使用列表推导式来提取不带前缀的包名，并将其放入一个新的列表中
        for device_name, package_list in install_dic.items():
            package_list = [line[8:] for line in package_list if line.startswith('package:')]
            install_dic[device_name] = package_list
        return install_dic

    def is_all_install_apk(self, apk_name):
        '''检查已连接的所有设备,是否都安装了某个apk'''
        is_install = True
        for device in self.devices:
            is_install &= self.is_install_apk(device.device_name)

    def is_install_apk(self, apk_name, device_name):
        '''检查是否安装了某个apk'''
        return apk_name in (self.get_installed_apk(device_name).get(device_name,[]))
    
    def install_apk(self,local_path,device_name=None):
        '''安装apk'''
        install_apk_cmd = f'install -g {local_path}'
        return self.run_in_all(install_apk_cmd,device_name,in_thread=False)

    def uninstall_apk(self,package_name,device_name=None):
        '''卸载apk'''
        return self.run_in_all(f'uninstall {package_name}',device_name)

    def start_app(self,package_name,activity_name,device_name=None):
        '''启动app'''
        # startActivity
        return self.run_in_all(f'shell am start -n {package_name}/{activity_name}',device_name)
        
    def stop_app(self,package_name,device_name=None):
        '''停止app'''
        return self.run_in_all(f'shell am force-stop {package_name}',device_name)

    def clear_data(self,package_name,device_name=None):
        '''清理一个apk的数据'''
        return self.run_in_all(f'shell pm clear {package_name}',device_name)

    def delete_file(self,path,device_name=None):
        '''删除文件'''
        if path in ('/','/sdcard','/storage','/system'):
            raise Exception(f'rm error,for path = {path}')
        return self.run_in_all(f'shell rm -rf {path}',device_name)
    
    def tar_folder(self,src_folder,target_full_path:str,device_name=None):
        '''将某个path打包'''
        #adb shell tar -cvf /sdcard/cache.tar /sdcard/cache
        target_full_path = target_full_path if target_full_path.endswith('.tar') else target_full_path + '.tar'
        self.run_in_all(f'shell tar -cvf {target_full_path} {src_folder}',device_name)
        self._wait_file_prepare(target_full_path,device_name)
        return True

    def pull_file(self,file_or_files,local_folder,device_name=None):
        '''
        拉取安卓文件,可能会报权限错误,这个无解
        一般先tar打包,再拉
        '''
        #adb pull /sdcard/Android/data/com.baitian.spacex.sx.bt/files/CustomAstralLog.log E:\\test
        if type(file_or_files)==list:
            for file in file_or_files:
                self.pull_file(file,local_folder)
        else:
            target_local_folder = path_tool.join_path(local_folder,device_name)
            target_local_folder = path_tool.make_folder(target_local_folder)
            self.run_in_all(f'pull {file_or_files} {target_local_folder}',device_name)
            # 要等待，就返回等待的结果
            base_name = path_tool.get_file_base_name(file_or_files)
            path_tool.wait_file_prepare(path_tool.join_path(target_local_folder,base_name))


    def get_file_size(self,file,device_name=None):
        #adb shell stat -c "%s"
        if file.endswith('/'):
            print(f'Warning!Your path [ {file} ] is folder,not file.Then you can see 3488')
        rs_dic = {}
        try:
            temp_dic = self.run_in_all(f'shell stat -c "%s" {file}',device_name)
            for key,values in temp_dic.items():
                for size in values:
                    if len(size)>0:
                        rs_dic[device_name]=int(size)
        except BaseException:
            traceback.print_exc()
        return rs_dic

    def _wait_file_prepare(self,file,device_name=None,time_out = 600):
        last_size = 0
        is_continue = True
        start_time = time.time()
        while is_continue:
            if time.time() - start_time > time_out:
                break
            time.sleep(3)
            is_continue = True
            size_dic = self.get_file_size(file,device_name)
            for device_name,size in size_dic.items():
                is_continue = is_continue and (size == last_size and size>0) # size变化
                print(f'waiting file:{int(time.time() - start_time)}s , {int(size)}b')
                last_size = size
        return False


    