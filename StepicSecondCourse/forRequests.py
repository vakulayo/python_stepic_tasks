import requests

par = {'key1': 'value', 'key2': 'value2'}
r = requests.get('https://echo.free.beeceptor.com', params=par)
print(r.text)
print(r.url)

rr = requests.get('https://stepik.org/media/attachments/course67/3.6.2/008.txt')
l = rr.text.strip().splitlines()
print(len(rr.text.splitlines()))


word = ''
file_name = '699991.txt'
file_text = ""
while word != 'We':
    req =  requests.get('https://stepik.org/media/attachments/course67/3.6.3/' + file_name)
    file_text = req.text.strip()
    file_name = file_text.splitlines()[0]
    word = file_name[0:2]
print("----------------------------------------------")
print(file_text)