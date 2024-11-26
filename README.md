# 小宇宙FM播客音频下载器

## 项目描述

这是一个简单的Python脚本，用于从小宇宙FM网站下载音频文件。该脚本能够从给定的网页URL中提取音频链接，并将音频文件下载到本地。

## 功能特点

- 从小宇宙FM网页中自动提取音频文件URL
- 脚本将自动在运行路径中创建名为`download`的文件夹，用于保存所下载的音频文件
- 支持多种URL提取方式（meta标签、audio标签、JSON-LD）
- 命令行参数支持
- 处理重定向和网络请求

## 效果示例

![Screenshot](Screenshot.png)

## 环境要求

- Python 3.7+
- pip

## 使用方法

### 对于Windows(PowerShell)用户

1. 点击右上角`Code`
2. 点击`Download ZIP`，将项目保存到本地
3. 解压后打开文件夹，按住键盘`Shift`按钮的同时，在文件夹内空白处点击鼠标右键，点击`在此处打开Powershell`按钮
4. 运行`pip install -r requirements.txt`,安装项目所需依赖环境
5. 运行`python xiaoyuzhoufmdownload.py -u <音频网页URL>`，下载所需音频文件

###对于Linux / MacOS用户

```bash
# 1. 克隆项目到本地：
git clone https://github.com/david-bowiegxw/xiaoyuzhoufmdownload.git
# 2. 进入项目文件夹：
cd xiaoyuzhoufmdownload
# 3. 安装依赖环境
pip install -r requirements.txt
# 4. 运行脚本
python xiaoyuzhoufmdownload.py -u <音频网页URL>
```

## 下载示例

```bash
python xiaoyuzhoufmdownload.py -u https://www.xiaoyuzhoufm.com/episode/6740632c8d1233fb0d3a9cea
```

脚本将在`download`文件夹中保存音频文件。

## 注意事项

- 请确保遵守小宇宙FM的使用条款
- 仅用于个人学习和研究目的
- 请自觉尊重内容创作者的版权以及劳动成果

## 依赖项列表

- requests
- beautifulsoup4
- argparse（Python标准库）

## 常见问题解决

- 如果遇到权限问题，可以尝试在命令前添加 `sudo`（仅限 macOS/Linux）
- 建议使用 Python 3.7 及以上版本
- 如果安装失败，请检查 pip 是否为最新版本：`pip install --upgrade pip`

## 贡献

欢迎提交 Issues 和 Pull Requests！

## 免责声明

本脚本仅供学习交流，请勿二次传播，分发，修改，截取所下载的音频内容，请自觉遵守版权法。

## 作者

[david-bowiegxw/xiaoyuzhoufmdownload](https://github.com/david-bowiegxw/xiaoyuzhoufmdownload)

## 许可证

本项目采用 MIT 许可证。详细信息请参见 `LICENSE` 文件。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
