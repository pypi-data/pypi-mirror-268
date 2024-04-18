import argparse
import logging

import toml
from typing import Dict

logger = logging.getLogger(__name__)


def getProperties(job_name) -> Dict[str, str]:
    # 创建参数解析器对象
    parser = argparse.ArgumentParser(description="Process some integers.")

    # 添加命令行参数 --conf，用于指定配置文件路径
    parser.add_argument('--conf', help='Configuration file path')
    parser.add_argument('--jn', help='job name file path')
    parser.add_argument('--pm', help='flink parameters file path')
    # 解析命令行参数
    arg = parser.parse_args()

    # 检查参数是否为空, 如何为空执行默认路径
    if not arg.conf or not '--conf':
        try:
            # 加载配置文件
            property_config = toml.load('../etc/config.toml')
            # 获取与调用者文件名匹配的配置信息
            configuration = property_config.get(job_name)
            # 判断参数是否声明，如果有声明: 覆盖配置文件内容
            if arg.jn is not None:
                configuration["sql_job_name"] = arg.jn
            if arg.pm is not None:
                configuration["parallelism"] = arg.pm

        except Exception as e:
            # 记录异常并抛出
            logger.error(f"Execute parsing with default path ../etc/config.toml, but cannot find file",
                         exc_info=e)
            raise
        return configuration

    try:
        # 加载配置文件
        property_config = toml.load(arg.conf)
        # 获取与调用者文件名匹配的配置信息
        configuration = property_config.get(job_name)
        # 判断参数是否声明，如果有声明: 覆盖配置文件内容
        if arg.jn is not None:
            configuration["sql_job_name"] = arg.jn
        if arg.pm is not None:
            configuration["parallelism"] = arg.pm
    except Exception as e:
        # 记录异常并抛出
        logger.error(f"An unexpected error occurred while trying to read the configuration file from {arg.conf}",
                     exc_info=e)
        raise

    # 返回配置信息
    return configuration
