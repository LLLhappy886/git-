from .config import GLOBAL_CONFIG
import requests

def install_package(package_name: str, version: str = "latest") -> bool:
    """安装指定包"""
    mirror = GLOBAL_CONFIG["mirror"]
    storage_path = GLOBAL_CONFIG["storage_path"]
    max_retries = GLOBAL_CONFIG["max_retries"]

    print(f"从镜像源 {mirror} 下载包：{package_name}=={version}")
    print(f"存储路径：{storage_path}")

    # 模拟下载逻辑
    for retry in range(max_retries):
        try:
            response = requests.get(f"{mirror}/packages/{package_name}/{version}")
            response.raise_for_status()
            print(f"包 {package_name}=={version} 安装成功！")
            return True
        except requests.exceptions.RequestException as e:
            print(f"下载失败（重试 {retry+1}/{max_retries}）：{e}")
    print(f"包 {package_name} 安装失败！")
    return False

def uninstall_package(package_name: str) -> bool:
    """卸载指定包"""
    print(f"卸载包：{package_name}")
    # 模拟卸载逻辑
    return True