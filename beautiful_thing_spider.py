import requests
import re
class BeautifulThingSpider:
    def __init__(self,page):
        self.page = int(page)
    def get_url(self):
        for page in range(1,self.page+1):
            params = {
                'form':str(self.page)
            }
            list_url = 'http://www.sexx2015.com/?'
            list_url_response = requests.get(list_url,params=params).content.decode()
            patter1 = re.compile('a\shref="(.*?/)"\stitle="(.*?)"')
            detail_url_list = re.findall(patter1,list_url_response)
            for detail_url in detail_url_list:
                detail_url_response = requests.get(detail_url[0]).content.decode()
                patter2 = re.compile('a\shref="(.*?.mp4)"\sdata')
                download_url = re.findall(patter2,detail_url_response)[0]
                print(download_url)
                print(detail_url[1] + '.mp4....开始下载')
                download = requests.get(download_url).content
                with open(detail_url[1] + '.mp4','wb') as f:
                    f.write(download)
                    print(detail_url[1] + '.mp4....下载完毕')
if __name__ == '__main__':
    print('请注意身体!!!!!')
    page = input('请输入要下载多少页:')
    video = BeautifulThingSpider(page)
    video.get_url()
