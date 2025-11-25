import yaml
import os

def load_config(config_path: str = "config/spm_config.yaml") -> dict:
    """加载 SP M 配置文件"""
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"配置文件不存在：{config_path}")
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

# 全局配置实例
GLOBAL_CONFIG = load_config()