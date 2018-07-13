import requests, re
for page1 in range(1,int(input('请注意身体!!!!!\n请输入要下载多少页:'))+1):
    for detail_url in re.findall(r'a\shref="(.*?/)"\stitle="(.*?)"',requests.get('http://www.sexx2015.com/?',params={'form':str(page1)}).content.decode()):
        open(detail_url[1] + '.mp4', 'wb').write(requests.get(re.findall(r'a\shref="(.*?.mp4)"\sdata',requests.get(detail_url[0]).content.decode())[0]).content)