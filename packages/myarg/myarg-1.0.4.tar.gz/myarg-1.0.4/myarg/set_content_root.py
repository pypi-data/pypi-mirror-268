import argparse
import sys


def set_content_root():
    # 创建参数解析器对象
    parser = argparse.ArgumentParser(description="Process some integers.")

    # 添加命令行参数 --rp，用于指定配置文件路径
    parser.add_argument('--rp', help='Content Root Path')

    # 解析命令行参数
    arg = parser.parse_args()

    if arg.rp is not None:
        # 设置模块系统路径
        sys.path.append(arg.rp)
