import sys
import os
import time
import shutil
import re
import subprocess

win_install_dict = {
'PyQt5':None,
'loguru':None,
#'airtest':None,
'poco':None,
'pocoui':None,
'requests':None,
'openpyxl':None,
#'jinja2':'3.0.1',
'rogue-tools':None,
}
linux_install_dict = {
'loguru':None,
'poco':None,
'pocoui':None,
'requests':None,
'openpyxl':None,
'rogue-tools':None,
}




class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class InstallModule(metaclass=Singleton):
	def __init__(self,python_exe,pip_exe) -> None:
		self.python_exe = python_exe
		self.pip_exe = pip_exe
		self.mods_version_dic={}
		self.last_update_result={}

	def load_mods_version(self):
		'''获得当前所有第三方库的版本'''
		result = subprocess.run(f'{self.pip_exe} list', shell=True, capture_output=True, text=True)
		output_lines = result.stdout.strip().split('\n')[2:]  # 跳过前两行标题
		for line in output_lines:
			package_name,package_version = line.split()
			self.mods_version_dic[package_name] = package_version


	def update_mod(self,mod_name,mod_version=None):
		'''安装单mod个'''
		uninstall_cmd = f'{self.pip_exe} uninstall -y {mod_name}'
		subprocess.run(uninstall_cmd, shell=True)

		if mod_version:
			install_cmd = f'{self.pip_exe} install --no-cache-dir {mod_name}=={mod_version}'
		else:
			install_cmd = f'{self.pip_exe} install --no-cache-dir {mod_name}'
		subprocess.run(install_cmd, shell=True)

		return True

	def update_mods(self,mods:dict):
		self.last_update_result=mods.copy()
		self.load_mods_version()
		for mod_name,version in mods.items():
			now_version=self.mods_version_dic.get(mod_name,0)
			if now_version!=version:
				try:
					self.update_mod(mod_name,version)
					self.last_update_result[mod_name]='已经更新'
				except BaseException:
					self.last_update_result[mod_name]='更新失败'
			else:
				self.last_update_result[mod_name]='无需更新'
		return self.last_update_result

	def show_result(self):
		for key,value in self.last_update_result.items():
			print(key,value)

	def cover_mod(self):
		site_packages_path = get_site_packages_path()

	def get_default_python(self):
		'''获得python安装目录'''
		f=os.popen(f'{self.python_exe} -0p')
		cmd_rs=f.read().splitlines()
		for line_str in cmd_rs:
			info_list=[]
			if len(line_str)>0:
				for info in line_str.split(' '):
					if len(info)>0:
						info_list.append(info)
			if info_list:
				python_version = info_list[0]
				python_path    = info_list[1]            
				return python_version,python_path

def get_site_packages_path():
	'''获取第三方库的路径'''
	for path in sys.path:
		if path.lower().endswith('\\lib\\site-packages'):
			return path






