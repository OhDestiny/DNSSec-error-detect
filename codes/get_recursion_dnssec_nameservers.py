# _*_ coding:utf-8 _*_
# @Time : 2023-10-29 10:53
# @Author ： iwbtfy
# @Project ： DNSSec-configuration-error-detection

import subprocess
import numpy as np
import os


# 筛选递归服务器
# flag字段中含有RA ---> recursion available
# 参数说明
# nameserver：需要检测的dns服务器ip
def is_recursion(nameserver):
    # 定义dig命令和参数
    dig_command = ['dig', '+norecurse', 'example.com', '@' + nameserver]

    # 执行dig命令
    try:
        dig_output = subprocess.check_output(dig_command)
    except subprocess.CalledProcessError as e:
        print("Error running dig:", e)
        exit(1)

    # 在输出中查找包含"flags"的行
    flags_line = None
    for line in dig_output.split('\n'):
        if "flags".encode("utf-8") in line:
            flags_line = line
            break

    # 从含有flags的行中进一步查询是否有RA字段
    if "ra".encode("utf-8") in flags_line:
        return True
    else:
        return False


# 筛选递归服务器中的支持dnssec的递归服务器
# flag字段中含有AD ---> authenticated data
# 参数说明
# nameserver：需要检测的dns服务器ip
def is_dnssec(nameserver):
    # 定义dig命令和参数
    dig_command_two = ['dig', '+norecurse', 'example.com', '@' + nameserver]

    # 执行dig命令
    try:
        dig_output = subprocess.check_output(dig_command_two)
    except subprocess.CalledProcessError as e:
        print("Error running dig:", e)
        exit(1)

    # 在输出中查找包含"flags"的行
    flags_line = None
    for line in dig_output.split('\n'):
        if "flags".encode("utf-8") in line:
            flags_line = line
            break

    # 从含有flags的行中进一步查询是否有RA字段
    if "ad".encode("utf-8") in flags_line:
        return True
    else:
        return False


if __name__ == '__main__':
    # 获取项目的根路径,然后再确定相关文件路径
    # 获取当前脚本的绝对路径
    current_script_path = os.path.abspath(__file__)

    # 获取当前脚本所在的目录（即项目的根路径）
    project_root = os.path.dirname(os.path.dirname(current_script_path))

    csv_file = os.path.join(project_root, "data", "nameservers", "dns_nameservers_processed_by_label.csv")
    csv_file_recursion = os.path.join(project_root, "data", "nameservers", "dns_nameservers_recursion.csv")
    csv_file_re_dnssec = os.path.join(project_root, "data", "nameservers", "dns_nameservers_recursion_dnssec.csv")

    nameservers_recursion_list = []
    nameservers_re_dnssec_list = []

    # 使用loader按行读取CSV文件
    nameservers_data = np.loadtxt(csv_file, delimiter=',', dtype=str)  # 使用dtype=str将数据读取为字符串

    # 循环判断是否是递归名称服务器
    for row in nameservers_data:
        print(row)
        if is_recursion(row):
            nameservers_recursion_list.append(row)
            print("RA")

    # 将判断结果写入csv文件
    np.savetxt(csv_file_recursion, nameservers_recursion_list, delimiter=',', fmt='%s')

    # 使用loader按行读取CSV文件
    recursion_nameservers_data = np.loadtxt(csv_file_recursion, delimiter=',', dtype=str)  # 使用dtype=str将数据读取为字符串

    # 循环判断是否支持dnssec的递归名称服务器
    for row in recursion_nameservers_data:
        print(row)
        if is_dnssec(row):
            nameservers_recursion_list.append(row)
            print("AD")

    # 将判断结果写入csv文件
    np.savetxt(csv_file_re_dnssec, nameservers_recursion_list, delimiter=',', fmt='%s')
