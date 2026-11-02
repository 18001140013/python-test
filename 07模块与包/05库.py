# 安装三方的库: 项目/.venv/lib/pyversion/site-packages
# .venv：项目虚拟环境，库都是独立份的，与其他项目不冲突
# 安装工具 pip
# 三方库存放的站点：pypi.org
# pip常用命令:
# pip install libName -- 下载指定库
# pip install -i 镜像地址 libName --- 指定镜像 境外访问不到的问题
# pip list --查看当前所有依赖库
# pip uninstall libNme --卸载掉指定库
# 库的组成部分：包 + 模块
# 我们开发常用的模块，是python自带的库，叫系统库，反之叫三方库，反之叫自定义库。
import requests

result = requests.get('https://www.baidu.com')
print(result.status_code)
print(result.text)