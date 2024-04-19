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
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import json
import sys
sys.setrecursionlimit(1500)

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0"}

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
        resp = requests.post("https://render-api-lm8c.onrender.com/session",json={"id":v},headers={'Content-Type':'application/json'})
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

def wait_download(url,ichunk=0,index=0,file=None,session=None):
    init()
    printl(Fore.RED + 'Iniciando sesion!!!')
    dl = url
    filename = dl['fn']
    total_size = dl['fs']

    if dl["m"] == "uoi":
        dl['u'] = ""
        dl['p'] = ""
        dl["c"] = ""
    if not session:
        session = make_session(dl)    
    if session:
        init()
        os.system(cmd)
        printl(Fore.BLUE + 'Sesion Iniciada ... !!!')
    else:
        init()
        os.system(cmd)
        printl(Fore.RED + 'Error al iniciar sesion ... !!!')
    state = 'ok'
    i = ichunk
    l = 1
    chunk_por = index
    filet =  dl['fn']
    filename = dl['fn']
    if os.path.exists(filename):
        os.unlink(filename)
    if len(filet) > 1:
        filet = ""
    f = open(filename,"wb") 
    os.system(cmd)
    total = len(dl['urls'])
    parte = 0
    while total_size > chunk_por: 
        chunkur = dl['urls'][i]
        parte+=1
        if dl['m'] == 'm':
          draftid = chunkur.split(":")[0]
          fileid = chunkur.split(":")[1]
          chunkurl = dl["c"]+"webservice/draftfile.php/"+draftid+"/user/draft/"+fileid+"/"+f"{filename.replace(' ','%2520')}-{i}.zip?token="+dl['token']
        elif dl["m"] == "uoi":
            chunkurl = chunkur+"/.file"
        elif dl['m'] == 'moodle'or dl['m'] == 'evea':
          draftid = chunkur.split(":")[0]
          fileid = chunkur.split(":")[1]
          chunkurl = dl["c"]+"draftfile.php/"+draftid+"/user/draft/"+fileid+"/"+f"{filename.replace(' ','%2520')}-{i}.zip"
        else:
          chunkurl = dl['c'].split('^')[0] + chunkur + dl['c'].split('^')[1]
        resp = session.get(chunkurl,headers=headers,stream=True,verify=False)  
        for chunk in resp.iter_content(chunk_size=8192):
            chunk_por += len(chunk)
            f.write(chunk)
            progress(f'{filet} ',chunk_por,total_size)
        l+=1
        i+=1
        if parte==total:
            total_size = chunk_por
    f.close()
    if os.path.exists('Downloads_C/' + filename):
        os.unlink('Downloads_C/' + filename)
    shutil.move(filename,'Downloads_C/'+filename)
        
    os.system(cmd)
    printl('Descarga Finalizada !!! Archivos Guardados en ./Downloads_C. Envie 0 y luego Enter para salir o pulse solo Enter para continuar')
    state = 'finish'
    a = input()
    if a == '0':
        if state == 'finish':
            return False,i,chunk_por,file,session
    else:
        return True,i,chunk_por,file,session

def initi():
    while (True):
        ichunk = 0
        index = 0
        file = None
        session = None
        init()
        print(Fore.CYAN + 'Pegue una direct Url')
        msg = input()
        url = ast.literal_eval(msg)
        if os.path.exists('Downloads_C/'):
            pass
        else:
            os.mkdir('Downloads_C/')
        wait,ichunk,index,file,session = wait_download(url,ichunk,index,file,session)
        if not wait:
            break
    
initi()
