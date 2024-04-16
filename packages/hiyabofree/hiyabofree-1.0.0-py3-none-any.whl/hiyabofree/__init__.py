from bs4 import BeautifulSoup
import requests
import os
from colorama import Fore , init
import shutil
import ast
import os
import platform
sistema_operativo = platform.system()
import urllib3
from queue import Queue
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import json
import sys
sys.setrecursionlimit(1500)

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0"}

download_queue = Queue()

if sistema_operativo == "Windows":
    cmd = "cls"
elif sistema_operativo == "Linux":
    cmd = "clear"

def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

def progress(filename, index, total):
    downloaded_mb = index / (1024 * 1024)
    total_mb = total / (1024 * 1024)
    downloaded_percent = (index / total) * 100
    progress_bar_length = 15
    completed_length = int(progress_bar_length * downloaded_percent / 100)
    remaining_length = progress_bar_length - completed_length

    print(f"{Fore.GREEN}{filename} [{completed_length * '●'}{remaining_length * '○'}] {downloaded_mb:.2f}MB / {total_mb:.2f}MB ({downloaded_percent:.2f}%)", end='\r')

def printl(text):
    init()
    print(Fore.GREEN + text,end='\r')

def make_session(dl):
    session = requests.Session()
    username = dl['u']
    password = dl['p']
    if dl['m'] == 'm':
      return session
    if dl["m"] == "uoi" or dl["m"] == "evea":
        v = str(dl["id"])
        resp = requests.post("https://api-89xq.onrender.com/session",json={"id":v},headers={'Content-Type':'application/json'})
        data = json.loads(resp.text)
        session.cookies.update(data)
        return session
    if dl['m'] == 'moodle':
        url = dl['c']+'login/index.php'
    else:
      url = dl['c'].split('/$$$call$$$')[0]+ '/login/signIn'
    resp = session.get(url,headers=headers,allow_redirects=True,verify=False)
    soup = BeautifulSoup(resp.text, "html.parser")
    if dl['m'] == 'moodle':
      try:
        token = soup.find("input", attrs={"name": "logintoken"})["value"]
        payload = {"anchor": "",
        "logintoken": token,
        "username": username,
        "password": password,
        "rememberusername": 1}
      except:
        payload = {"anchor": "",
        "username": username,
        "password": password,
        "rememberusername": 1}
    else:
      try:
          csrfToken = soup.find('input',{'name':'csrfToken'})['value']
          payload = {}
          payload['csrfToken'] = csrfToken
          payload['source'] = ''
          payload['username'] = username
          payload['password'] = password
          payload['remember'] = '1'
      except Exception as ex:
          print(ex)
    
    resp = session.post(url,headers=headers,data=payload,verify=False)
    if resp.url!=url:
        return session
    return None

def wait_download(queue, ichunk=0, index=0, file=None, session=None):
    while not queue.empty():
        dl = queue.get()
        try:
            filename = dl['fn']
            total_size = dl['fs']
            if dl["m"] == "uoi":
                dl['u'] = ""
                dl['p'] = ""
                dl["c"] = ""
            session = make_session(dl)
            state = 'ok'
            i = ichunk
            l = 1
            chunk_por = index
            filet = dl['fn']
            if os.path.exists(filename):
                os.unlink(filename)
            if len(filet) > 1:
                filet = filename[:5] + "." + filename[-5:]
            f = open(filename, "wb")
            os.system(cmd)
            total = len(dl['urls'])
            parte = 0
            while total_size > chunk_por:
                chunkur = dl['urls'][i]  # Possible error here
                parte += 1
                if dl['m'] == 'm':
                    draftid = chunkur.split(":")[0]
                    fileid = chunkur.split(":")[1]
                    chunkurl = dl["c"] + "webservice/draftfile.php/" + draftid + "/user/draft/" + fileid + "/" + f"{filename.replace(' ','%2520')}-{i}.zip?token=" + dl['token']
                elif dl["m"] == "uoi":
                    chunkurl = chunkur + "/.file"
                elif dl['m'] == 'moodle' or dl['m'] == 'evea':
                    draftid = chunkur.split(":")[0]
                    fileid = chunkur.split(":")[1]
                    chunkurl = dl["c"] + "draftfile.php/" + draftid + "/user/draft/" + fileid + "/" + f"{filename.replace(' ','%2520')}-{i}.zip"
                else:
                    chunkurl = dl['c'].split('^')[0] + chunkur + dl['c'].split('^')[1]
                resp = session.get(chunkurl, headers=headers, stream=True, verify=False)
                for chunk in resp.iter_content(chunk_size=8192):
                    chunk_por += len(chunk)
                    f.write(chunk)
                    progress(f'{filet} ', chunk_por, total_size)
                l += 1
                i += 1
                if parte == total:
                    total_size = chunk_por
            f.close()
            if os.path.exists('Downloads_C/' + filename):
                os.unlink('Downloads_C/' + filename)
            shutil.move(filename, 'Downloads_C/' + filename)

            os.system(cmd)
            if queue.empty():
                printl('Descarga Finalizada !!! Archivos Guardados en ./Downloads_C. Envie 0 y luego Enter para salir o pulse solo Enter para continuar')
                state = 'finish'
                a = input()
                if a == '0':
                    if state == 'finish':
                        return False, i, chunk_por, file, session
                else:
                    return True, i, chunk_por, file, session
        except Exception as e:
            error_message = f"Error durante la descarga: {str(e)}"
            print(error_message)
            return False

def initi():
    while True:
        ichunk = 0
        index = 0
        file = None
        session = None
        init()
        print(Fore.CYAN + 'Pegue una direct Url o escriba "start" para comenzar la descarga de la cola')
        msg = input()
        if msg.lower() == "start":
            if download_queue.empty():
                print(Fore.RED + "La cola de descarga está vacía. Pegue una URL para agregarla a la cola.")
                continue
            else:
                print(Fore.GREEN + "Comenzando la descarga de la cola...")
                print(Fore.RED + "!!! Iniciando Sesión.")
                result = wait_download(download_queue, ichunk, index, file, session)
                if result:
                    break
        else:
            url = ast.literal_eval(msg)
            if os.path.exists('Downloads_C/'):
                pass
            else:
                os.mkdir('Downloads_C/')
            download_queue.put(url)
    
initi()
