import subprocess
import platform
import json
import os

def __identify_os_architecture():
    system = platform.system()
    architecture = platform.machine()

    if system == 'Darwin':
        os = 'macOS'
    elif system == 'Windows':
        os = 'Windows'
    elif system == 'Linux':
        os = 'Linux'
    else:
        os = 'unknown OS'
    if 'arm' in architecture.lower():
        arch = 'ARM'
    elif 'x86_64' in architecture.lower() or 'amd64' in architecture.lower():
        arch = 'x86_64'
    else:
        arch = 'unknown architecture'
    if os != 'Windows' and os!='Linux':
        raise Exception('Unsupported OS')
    if arch != 'x86_64':
        raise Exception('Unsupported Architecture')
    return os, arch


def html_tree_shaking(inputHtmlStr):
    filename="";
    current_file_path = os.path.dirname(os.path.abspath(__file__))
    os_name, arch = __identify_os_architecture()
    if os_name == 'Windows':
        filename=os.path.normpath(os.path.join(current_file_path, "./.bin/html-tree-shaking-win.exe"))
    else:
        filename=os.path.normpath(os.path.join(current_file_path, "./.bin/html-tree-shaking-linux"))
        if(os.getenv("CHROME_PATH") == None):
            os.environ["CHROME_PATH"]="/usr/bin/google-chrome"
    try:
        process = subprocess.Popen([filename],
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE)
        stdout, _ = process.communicate(input=(inputHtmlStr+"\ninternal_command_$$$=do_shaking").encode())
        output = stdout.decode().strip()
        dict_obj = json.loads(output)
        if(dict_obj.get("success") == True):
            return dict_obj.get("output")
        else:
            print("Error in htmlTreeShaking: "+dict_obj.get("message"))
            raise Exception(dict_obj.get("message"))
    except Exception as e:
        print("Error in htmlTreeShaking: "+str(e))
        raise e
    finally:
        process.kill();

