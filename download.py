import requests

def download(url):
    print("开始下载：",url)
    response=requests.get(url,verify=False)
    print("下载完成")
    filename=url.split(r"/")[-1]
    with open(filename,mode='wb') as file_obj:
        file_obj.write(response.content)

if __name__ == '__main__':
    url_list=[r"https://i.tuiimg.net/006/2522/2.jpg",
              r"https://i.tuiimg.net/006/2522/3.jpg",
              r"https://i.tuiimg.net/006/2522/4.jpg"]
    for item in url_list:
        download(item)
