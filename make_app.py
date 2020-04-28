import os

script_file = 'JobManager.py'
app_name = 'AppName'
command_list = ['pyinstaller', '--clean', '--onefile', '--windowed','--name', app_name, script_file]
cmand = " ".join(command_list)
os.system(cmand)