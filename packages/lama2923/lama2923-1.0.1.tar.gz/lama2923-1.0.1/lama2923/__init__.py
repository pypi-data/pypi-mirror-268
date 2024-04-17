# python version = 3.11
import os
import time
import socket
from colorama import Fore, Style, init
import requests
import msvcrt
import requests
import os
import requests


def ekran_temizle():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')
    else:
        raise NotImplementedError("Tost Makinesi Algılandı!!")
def geçen_süreyi_hesapla(start_time, end_time):
    if not (isinstance(start_time, (int, float)) and isinstance(end_time, (int, float))):
        raise TypeError("SADECE time.time() veya lama2923.tzaman() KABUL EDİLİYOR!")

   
    end_time = end_time
    start_time = start_time
    time_difference = end_time - start_time
    seconds = int(time_difference)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    salise = int((time_difference - int(time_difference)) * 100)
    if days == 0:
        days = False
    if hours == 0 and days == 0:
        hours = False
    if minutes == 0 and hours == 0 and days == 0:
        minutes = False
    if seconds == 0 and minutes == 0 and hours == 0 and days == 0:
        seconds = False
    if salise == 0 and seconds == 0 and minutes == 0 and hours == 0 and days == 0:
        salise = False
        
    return {"Salise": salise, "Seconds": seconds, "Minutes": minutes, "Hours": hours, "Days": days}

def tzaman():
    return time.time()
    
def Gokkusagı(YAZI, DÖNGÜ, Hız, bölüm):
    def hız_kontrol():
        if Hız != None:
            if Hız == 'Yavaş' or Hız == 'Slow' or Hız == 'Hızlı':
                pass
            else:               
                raise ValueError("Hız değerinizi doğru girmeniz gerekir. Hız değeri 'Yavaş' = 'Slow', None (None orta demek) veya 'Hızlı' olmalıdır.")

    def bölüm_kontrol():
        if bölüm != None:
            if bölüm == 'Tam' or bölüm == 'Yarı' or bölüm == 'Çeyrek':
                pass
            else:
                raise ValueError("Bölüm değerinizi doğru girmeniz gerekir. bölüm değeri 'Tam', 'Yarı', None (None Tam demek) veya 'Çeyrek' olmalıdır.")

                
    hız_kontrol()
    bölüm_kontrol()      
    
    init(autoreset=True)
    if not isinstance(DÖNGÜ, int):
        print("DÖNGÜ değerine Tam sayı girmek zorundasın!")
        time.sleep(3)
        ekran_temizle()
        exit(1)

    renkler = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]

    sayı = 0

    YAZI = YAZI
    YAZI_uzunluğu = len(YAZI)
    
    if bölüm == 'Tam' or bölüm == None:
        bölüm_sayısı1 = 238
        bölüm_sayısı2 = bölüm_sayısı1 - 2
    elif bölüm == 'Yarı':
        bölüm_sayısı1 = 119
        bölüm_sayısı2 = bölüm_sayısı1 - 2
    elif bölüm == 'Çeyrek':
        bölüm_sayısı1 = 59
        bölüm_sayısı2 = bölüm_sayısı1 - 2 
               
    while True:
        sayı += 1
        if sayı > DÖNGÜ:
            break
        
        for i in range(1, bölüm_sayısı1 - YAZI_uzunluğu):
            for renk in renkler:
                if Hız == 'Yavaş' or Hız == 'Slow':
                    time.sleep(0.001)  
                elif Hız == 'Hızlı':
                    pass
                elif Hız == None:
                    time.sleep(0.0001)    
                print(" " * i + renk + YAZI)

        for i in range(bölüm_sayısı2 - YAZI_uzunluğu, 0, -1):
            for renk in renkler:
                if Hız == 'Yavaş' or Hız == 'Slow':
                    time.sleep(0.001)  
                elif Hız == 'Hızlı':
                    pass
                elif Hız == None:
                    time.sleep(0.0001)   
                print(" " * i + renk + YAZI)

def port_kontrol(ip_address, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  
    result = sock.connect_ex((ip_address, port))
    sock.close()

    if result == 0:
        return True
    else:
        return False

def internet_kontrol():
    try:
        response = requests.get("http://www.google.com", timeout=2.5)
        return True
    except requests.ConnectionError:
        return False

def lprint(*yazı, end="\n", sep=" ", delay=0.10):
    yazı = map(str, yazı)
    birleşik_kelime = sep.join(yazı)
    kelime_len = len(birleşik_kelime)

    for x in range(1, (kelime_len + 1)):
        if delay <= 0:
            delay = 0.02
            break
        delay -= 0.0005
        

    if delay <= 0:
        delay = 0.02
        

    for char in birleşik_kelime:
        print(char, end="", flush=True)
        time.sleep(delay)

    if not end:
        print(end="")
    else:
        print(end=end)

def otodüzeltmeyi_temizle():
    while msvcrt.kbhit():
        msvcrt.getch()

def linput(*yazı, end="", wend="",sep=" ", delay=0.10, otodt=False):
    sonuncu_harf = ""  
    if yazı:
        sonuncu_argüman = list(yazı[-1])
        if sonuncu_argüman:
            sonuncu_harf = sonuncu_argüman[-1]
            sonuncu_argüman.pop()
            yazı = list(yazı)
            yazı[-1] = ''.join(sonuncu_argüman)

    end = sonuncu_harf + end
    lprint(*yazı, end=end, sep=sep, delay=delay)
    if otodt:
        otodüzeltmeyi_temizle()
    girdi = input()
    
    return girdi

def çoğul_eki(yazı = None):
    if isinstance(yazı, str):
        pass
    elif isinstance(yazı, int):
        ek = sıralama_eki(yazı, Çoğul_eki=True)[-3:-1] + sıralama_eki(yazı, Çoğul_eki=True)[-1]
        return ek
    else:
        raise TypeError(f"Sadece Integer ve String Kullanabilir. {type(yazı)}" + " Değil!")
        
    unsuz_harfler = ['b', 'c', 'ç', 'd', 'f', 'g', 'ğ', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 'ş', 't', 'v', 'y', 'z']
    unlu_harfler = ['a', 'e', 'ı', 'i', 'o', 'ö', 'u', 'ü']
    lar_eki_alanlar = ["o", "u", "a", "ı"]
    ler_eki_alanlar = ["e", "ö", "ü", "i"]
    Char = None
    
    for  char in str(yazı)[::-1]:
        if char not in unsuz_harfler:
            Char = char
            break
        
    if Char in ler_eki_alanlar:
        return "ler"
    
    elif Char in lar_eki_alanlar:
        return "lar"

def sıralama_eki(number, ek_derecesi = 1, Çoğul_eki = False):
    if not isinstance(number, int):
        raise TypeError("verinin Integer verisinde olması zorunludur!")
    def main(number):
        if len(str((int(number)))) < 1 or str((int(number)))[-1] != '0': # Birler Katmanı
            c = {
                "0": "ıncı",
                "1": "inci",
                "2": "nci",
                "3": "üncü",
                "4": "üncü",
                "5": "inci",
                "6": "ıncı",
                "7": "nci",
                "8": "inci",
                "9": "uncu"
            }
            return c[str((int(number)))[-1]]
            

        elif len(str(int(number))) > 1:
            if "0" in str(int(number))[-1]:
                Number, Index = None, None
                for index, number in enumerate(str(int(number))[::-1]):
                    if number != '0':
                        Number, Index = number, index
                        break
                    
                if index == 1:
                    ekler = {
                        "1": "uncu",
                        "2": "nci",
                        "3": "uncu",
                        "4": "ıncı",
                        "5": "nci",
                        "6": "ıncı",
                        "7": "inci",
                        "8": "inci",
                        "9": "ıncı"
                    }
                    return ekler[str(int(Number))]
                    

                elif index == 2: # Yüzler Katmanı
                    return "üncü" 
                elif index == 3 or index == 4 or index == 5: # Binler Katmanı
                    return "inci"
                elif index == 6 or index == 7 or index == 8 : # Milyonlar Katmanı
                    return "uncu"
                elif index == 9 or index == 10 or index == 11 : # Milyarlar Katmanı
                    return "ıncı"
                else: # Trilyonlar Katmanı, Kintilyonlar Katmanı, Kuadrilyonlar Katmanı...
                    return "uncu"

    ek = main(number)
    
    if not Çoğul_eki:
        if ek_derecesi == 1:
            return ek
        elif ek_derecesi == 2:
            ekler = {
                "inci": "sin",
                "nci": "sin",
                "uncu": "sun",
                "üncü": "sün",
                "ıncı": "sın",
            }
            return ek + ekler[ek]
        
        elif ek_derecesi == 3:
            ekler = {
                "inci": "siniz",
                "nci": "sinız",
                "uncu": "sunuz",
                "üncü": "sünüz",
                "ıncı": "sınız",
            }
            return ek + ekler[ek]
        
        elif ek_derecesi == 4:
            ekler = {
                "inci": "yiz",
                "nci": "yiz",
                "uncu": "yuz",
                "üncü": "yüz",
                "ıncı": "yız",
            }
            return ek + ekler[ek]
        
        elif ek_derecesi == 5:
            ekler = {
                "inci": "yim",
                "nci": "yim",
                "uncu": "yum",
                "üncü": "yüm",
                "ıncı": "yım",
            }
            return ek + ekler[ek]
        
    else:
        ler_lar_eki = çoğul_eki(ek)
        return ek + ler_lar_eki

def kurallı_sayı(Numbers=0):
    if not isinstance(Numbers, float):
        try:
            x = float(Numbers)
            pass
        except (ValueError, TypeError):
            
            if not isinstance(Numbers, int):
                try:
                    x = float(Numbers)
                    pass
                except (ValueError, TypeError):
                    raise TypeError(f'INTEGER Veya Float olmak zorunda!  "String" olarak da yollayabilirsiniz içinde harf olmadığı sürece. ')
            else:
                pass
    else:
        pass
    edited_Numbers = ""
    
    if ',' in reversed(str(Numbers).replace(".", ",")):
        number_split_list = str(Numbers).replace(".", ",")[::-1].split(',')
        edited_number_split_list_1 = ""
        edited_number_split_list_2 = number_split_list[0]
        
        for INDEX , number in enumerate(number_split_list[1], start=1):
            
            if INDEX % 3 == 0 and (len(str(number_split_list[1]))) != INDEX:
                edited_number_split_list_1 += f"{number}."
            else:
                edited_number_split_list_1 += number
        return edited_number_split_list_1[::-1] + "," + edited_number_split_list_2[::-1]
    else:
        
        for INDEX , number in enumerate(reversed(str(Numbers)), start=1):
        
            if INDEX % 3 == 0 and len(str(Numbers)) != INDEX:
                
                edited_Numbers += f"{number}."
            else:
                edited_Numbers += number
        return edited_Numbers[::-1]
                
class CustomDecodeError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)   
            
def terskurallı_sayı(Numbers=0):
    if not isinstance(Numbers, str):
        raise TypeError("Değerin String olması zorunludur!")
    Numbers = str(Numbers).replace(".", "")
    Numbers = Numbers.replace(",", ".")
    return Numbers


class _TokenIsNotWork(Exception):
    pass


class Discord:
    class User:
        
        def __init__(self, token):
            self.token = str(token)
            response = requests.get('https://discord.com/api/v9/users/@me', headers={'Authorization': str(self.token)})
            if response.status_code == 200:
                pass
            else:
                raise _TokenIsNotWork('Token IS NOT WORK!')
                
                
        def send_message(self, Channel_id, Message, files=None):
            payload = {'content': str(Message)}
            headers = {'Authorization': str(self.token)}
            
            if files is not None and isinstance(files, list):
                files_data = {}
                for file_name in files:
                    if os.path.getsize(file_name) > 0:
                        with open(file_name, "rb") as file:
                            files_data[os.path.basename(file_name)] = file.read()
                response = requests.post(f'https://discord.com/api/v9/channels/{Channel_id}/messages', data=payload, files=files_data, headers=headers)
            else:
                response = requests.post(f'https://discord.com/api/v9/channels/{Channel_id}/messages', data=payload, headers=headers)
                
            return response.status_code
        
        def delete_message(self, Channel_id, Message_id):
            headers = {'Authorization': str(self.token)}
            r = requests.delete(f'https://discord.com/api/v9/channels/{Channel_id}/messages/{Message_id}', headers=headers)
            return r.status_code
        
        def edit_message(self, Channel_id, Message_id, Message_Content):
            headers = {'Authorization': str(self.token)}
            payload = {'content': str(Message_Content)}
            r = requests.patch(f'https://discord.com/api/v9/channels/{Channel_id}/messages/{Message_id}', json=payload, headers=headers)
            return r.status_code
        
        def get_channel_message(self, Channel_id):
            headers = {'Authorization': str(self.token)}
            r = requests.get(f'https://discord.com/api/v9/channels/{Channel_id}/messages', headers=headers)
            if r.status_code == 200:
                messages = r.json()
                return [r.status_code, messages]
            else:
                return r.status_code
            
        def get_specific_message(self, Channel_id, Message_id):
            headers = {'Authorization': str(self.token)}
            url = f'https://discord.com/api/v9/channels/{Channel_id}/messages/{Message_id}'
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return [response.status_code, response.json()]
            else:
                return response.status_code


        def add_reaction(self, Channel_id, Message_id, emoji):
            headers = {'Authorization': str(self.token)}
            emoji = requests.utils.quote(emoji)
            url = f'https://discord.com/api/v9/channels/{Channel_id}/messages/{Message_id}/reactions/{emoji}/@me'
            response = requests.put(url, headers=headers)
            return response.status_code
        
        def remove_reaction(self, Channel_id, Message_id, emoji):
            headers = {'Authorization': str(self.token)}
            emoji = requests.utils.quote(emoji)
            url = f'https://discord.com/api/v9/channels/{Channel_id}/messages/{Message_id}/reactions/{emoji}/@me'
            response = requests.delete(url, headers=headers)
            return response.status_code


        def get_channel_info(self, Channel_id):
            headers = {'Authorization': str(self.token)}
            url = f'https://discord.com/api/v9/channels/{Channel_id}'
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return [response.status_code, response.json()]
            else:
                return response.status_code
    
        def list_guild_channels(self, Guild_id):
            headers = {'Authorization': str(self.token)}
            url = f'https://discord.com/api/v9/guilds/{Guild_id}/channels'
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return [response.status_code, response.json()]
            else:
                return response.status_code   

        def send_tts_message(self, Channel_id, Message):
            payload = {'content': str(Message), 'tts': True}
            headers = {'Authorization': str(self.token)}
            response = requests.post(f'https://discord.com/api/v9/channels/{Channel_id}/messages', data=payload, headers=headers)
            return response.status_code
        
        def send_reply_message(self, Channel_id, Message, ReplyMessage_id):
            payload = {'content': str(Message), 'message_reference': {'message_id': ReplyMessage_id}}
            headers = {'Authorization': str(self.token)}
            response = requests.post(f'https://discord.com/api/v9/channels/{Channel_id}/messages', data=payload, headers=headers)
            return response.status_code
        
        def change_user_nickname(self, Guild_id, Nickname):
            headers = {'Authorization': str(self.token)}
            payload = {'nick': str(Nickname)}
            response = requests.patch(f'https://discord.com/api/v9/guilds/{Guild_id}/members/@me/nick', json=payload, headers=headers)
            return response.status_code

        def get_user_info(self, User_id):
            headers = {'Authorization': str(self.token)}
            url = f'https://discord.com/api/v9/users/{User_id}'
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return [response.status_code, response.json()]
            else:
                return response.status_code

        def get_all_guilds(self):
            headers = {'Authorization': str(self.token)}
            url = 'https://discord.com/api/v9/users/@me/guilds'
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return [response.status_code, response.json()]
            else:
                return response.status_code
        
        def get_spesific_guild(self, Guild_id):
            headers = {'Authorization': str(self.token)}
            url = f'https://discord.com/api/v9/guilds/{Guild_id}'
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return [response.status_code, response.json()]
            else:
                return response.status_code
            
        def kick_member(self, Guild_id, Member_id):
            headers = {'Authorization': str(self.token)}
            url = f'https://discord.com/api/v9/guilds/{Guild_id}/members/{Member_id}'
            response = requests.delete(url, headers=headers)
            return response.status_code
        
        def ban_member(self, Guild_id, Member_id, delete_message_days=0):
            headers = {'Authorization': str(self.token)}
            url = f'https://discord.com/api/v9/guilds/{Guild_id}/bans/{Member_id}'
            data = {'delete_message_days': delete_message_days}
            response = requests.put(url, headers=headers, json=data)
            return response.status_code
        
        def unban_member(self, Guild_id, Member_id):
            headers = {'Authorization': str(self.token)}
            url = f'https://discord.com/api/v9/guilds/{Guild_id}/bans/{Member_id}'
            response = requests.delete(url, headers=headers)
            return response.status_code
        


        
        def get_guild_bans(self, Guild_id):
            headers = {'Authorization': str(self.token)}
            url = f'https://discord.com/api/v9/guilds/{Guild_id}/bans'
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return [response.status_code, response.json()]
            else:
                return response.status_code
            
        
        def get_guild_channels(self, Guild_id):
            headers = {'Authorization': str(self.token)}
            url = f'https://discord.com/api/v9/guilds/{Guild_id}/channels'
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return [response.status_code, response.json()]
            else:
                return response.status_code
        
        def get_guild_members(self, Guild_id):
            headers = {'Authorization': str(self.token)}
            url = f'https://discord.com/api/v9/guilds/{Guild_id}/members'
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return [response.status_code, response.json()]
            else:
                return response.status_code
            
        def get_guild_roles(self, Guild_id):
            headers = {'Authorization': str(self.token)}
            url = f'https://discord.com/api/v9/guilds/{Guild_id}/roles'
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return [response.status_code, response.json()]
            else:
                return response.status_code
            
        def create_guild_role(self, Guild_id, Role_name):
            headers = {'Authorization': str(self.token)}
            payload = {'name': str(Role_name)}
            response = requests.post(f'https://discord.com/api/v9/guilds/{Guild_id}/roles', json=payload, headers=headers)
            return response.status_code
        
        def delete_guild_role(self, Guild_id, Role_id):
            headers = {'Authorization': str(self.token)}
            response = requests.delete(f'https://discord.com/api/v9/guilds/{Guild_id}/roles/{Role_id}', headers=headers)
            return response.status_code


    class Webhook:
        def __init__(self, webhook_url):
            self.WebhookUrl = str(webhook_url)
            
        def send_webhook(self, Content='', embed=None, files=None):
            def format_embed(embed):
                formatted_embed = {}
                all_args3 = {'fields': ['name', 'value', 'inline']}
                all_args2 = {'footer': ['text', 'icon_url'], 'image': ['url'], 'thumbnail': ['url']}
                all_args1 = ['title', 'description', 'color', 'url']
    
                for arg in all_args1:
                    if arg in embed:
                        if arg == 'color':
                            formatted_embed['color'] = embed['color']
                        else:
                            formatted_embed[arg] = embed[arg]
    
                for arg, keys in all_args2.items():
                    if arg in embed:
                        formatted_embed[arg] = {}
                        for key in keys:
                            if key in embed[arg]:
                                formatted_embed[arg][key] = embed[arg][key]
    
                if 'fields' in embed:
                    fields = []
                    for field in embed['fields']:
                        field_data = {}
                        for arg in all_args3['fields']:
                            if arg in field:
                                field_data[arg] = field[arg]
                        fields.append(field_data)
                    formatted_embed['fields'] = fields
    
                return formatted_embed
    
            data = {}
    
            if Content:
                data['content'] = Content
    
            if embed:
                data['embeds'] = [format_embed(embed)]
            
            if not 'embeds' in data:
                if files is not None and isinstance(files, list):
                    files_data = {}
                    for file_name in files:
                        if os.path.getsize(file_name) > 0:
                            with open(file_name, "rb") as file:
                                files_data[os.path.basename(file_name)] = file.read()
                    response = requests.post(self.WebhookUrl, data=data, files=files_data)
                else:

                    response = requests.post(self.WebhookUrl, json=data)

                return response.status_code
            
            else:
                if files is not None and isinstance(files, list):
                    files_data = {}
                    for file_name in files:
                        if os.path.getsize(file_name) > 0:
                            with open(file_name, "rb") as file:
                                files_data[os.path.basename(file_name)] = file.read()
                    data2 = data.copy()
                    data2["embeds"] = {}

                    response = requests.post(self.WebhookUrl, json=data)
                    response2 = requests.post(self.WebhookUrl, json=data2, files=files_data)
                    return [response, response2]
                else:
                    
                    response = requests.post(self.WebhookUrl, json=data)
                
                    return response.status_code
                
        def delete_specific_message(self, Message_id):
            response = requests.delete(f'{self.WebhookUrl}/messages/{Message_id}')
            return response.status_code
        
        def get_specific_message(self, Message_id):
            response = requests.get(f'{self.WebhookUrl}/messages/{Message_id}')
            if response.status_code == 200:
                return [response.status_code, response.json()]
            else:
                return response.status_code
            
        def get_webhook_info(self):
            response = requests.get(self.WebhookUrl)
            if response.status_code == 200:
                return [response.status_code, response.json()]
            else:
                return response.status_code
                
                
        def get_messages(self):
            response = requests.get(f'{self.WebhookUrl}/messages')
            if response.status_code == 200:
                return [response.status_code, response.json()]
            else:
                return response.status_code
            
        



                
                

