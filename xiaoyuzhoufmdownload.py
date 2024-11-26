import os
import requests
import argparse
from bs4 import BeautifulSoup

def extract_audio_url(url):
    # 添加 User-Agent 头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    # 发送请求获取网页内容
    response = requests.get(url, headers=headers, allow_redirects=True)
    if response.status_code != 200:
        print(f"无法获取网页内容，状态码: {response.status_code}")
        return None

    # 使用 BeautifulSoup 解析网页内容
    soup = BeautifulSoup(response.content, 'html.parser')

    # 尝试从 meta 标签中提取音频 URL
    meta_audio_url = soup.find("meta", property="og:audio")
    if meta_audio_url:
        return meta_audio_url["content"]

    # 尝试从 audio 标签中提取音频 URL
    audio_tag = soup.find("audio")
    if audio_tag and "src" in audio_tag.attrs:
        return audio_tag["src"]

    # 尝试从 JSON-LD 中提取音频 URL
    json_ld = soup.find("script", type="application/ld+json")
    if json_ld:
        try:
            data = json.loads(json_ld.string)
            if "@type" in data and data["@type"] == "MediaObject" and "contentUrl" in data:
                return data["contentUrl"]
        except json.JSONDecodeError:
            pass

    print("无法找到音频文件的 URL")
    return None

def download_file(url, filename):
    # 检查并创建 download 文件夹
    download_folder = "download"
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    # 构建完整的文件路径
    file_path = os.path.join(download_folder, filename)

    # 添加 User-Agent 头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    # 下载文件
    response = requests.get(url, headers=headers, stream=True)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
        print(f"文件已下载到: {file_path}")
    else:
        print(f"下载失败，状态码: {response.status_code}")

def main():
    # 创建 ArgumentParser 对象
    parser = argparse.ArgumentParser(description="下载音频文件到当前路径下的 download 文件夹")
    
    # 添加 -u 参数
    parser.add_argument('-u', '--url', type=str, required=True, help='音频文件的网页链接')
    
    # 解析命令行参数
    args = parser.parse_args()
    
    # 获取 URL
    url = args.url
    
    # 提取音频文件的实际 URL
    audio_url = extract_audio_url(url)
    if not audio_url:
        print("无法提取音频文件的 URL")
        return
    
    # 从 URL 中提取文件名
    filename = audio_url.split('/')[-1]
    
    # 下载文件
    download_file(audio_url, filename)

if __name__ == "__main__":
    main()