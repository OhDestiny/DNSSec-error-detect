# _*_ coding:utf-8 _*_
# @Time : 2023-10-30 12:07
# @Author ： iwbtfy
# @Project ： DNSSec-configuration-error-detection

import subprocess
import numpy as np
import os
import sys


# 检测dnssec的配置错误并且写入文件
# 参数说明
# errors: 配置的错误(如果不知道可以填NULL)       domain_name: 需要检测的域名
# nameserver_file: 使用的递归服务器的文件路径    key_file: 根服务器的key的路径
# logs: 存储日志的列表                         record_types: 需要查询域名的记录类型
# project_root_file: 项目的根路径
def detect_error(errors, domain_names, nameserver_file, key_file, logs, record_types, project_root_file):
    log_file = os.path.join(project_root_file, "data", "detect_logs",
                            "detect_logs_" + domain_names.split('.')[0] + '_' +
                            errors + ".txt")
    nameserver_re_dnssec = np.loadtxt(nameserver_file, delimiter=',', dtype=str)
    errors_set = set()
    for nameserver in nameserver_re_dnssec:
        # 创建dig命令
        dig_command = ['dig', '@' + nameserver, '+sigchase', '+trusted-key=' + key_file, domain_names, record_types]
        try:
            # 日志
            logs.append(nameserver)
            result = subprocess.check_output(dig_command)
            lines = result.splitlines()
            if lines:
                last_line = lines[-1]
                if not last_line:
                    last_line = lines[-2]
                print(last_line)
                errors_set.add(last_line)
            # 保存日志
            logs.append(result)
        except subprocess.CalledProcessError as e:
            errors_set.add("DIG command failed")
            logs.append("DIG command failed")
            print("connection time out")
        except FileNotFoundError:
            print('DIG command not found. Make sure dig is installed on your system.')

    # 将log这个list写入txt文件
    np.savetxt(log_file, logs, delimiter=',', fmt='%s')
    # 将error_set 写入txt文件
    error_list = list(errors_set)
    error_list_file = os.path.join(project_root_file, "data", "error_list",
                                   "errors_list_" + domain_names.split('.')[0] + '_' +
                                   errors + ".txt")
    np.savetxt(error_list_file, error_list, delimiter=',', fmt='%s')


if __name__ == '__main__':
    # 获取项目的根路径,然后再确定相关文件路径
    # 获取当前脚本的绝对路径
    current_script_path = os.path.abspath(__file__)

    # 设置参数
    project_root = os.path.dirname(os.path.dirname(current_script_path))
    csv_file_re_dnssec = os.path.join(project_root, "data", "nameservers",
                                      "dns_nameserver_re_dnssec_1000.txt")  # 支持dnssec的递归服务器路径
    root_key_file = os.path.join(project_root, "resources", "root.key")
    domain_name = sys.argv[1]
    record_type = "A"
    error = sys.argv[2]
    log = []

    detect_error(error, domain_name, csv_file_re_dnssec, root_key_file, log, record_type, project_root)
