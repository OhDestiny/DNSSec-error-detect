# _*_ coding:utf-8 _*_
# @Time : 2023-12-18 9:27
# @Author ： iwbtfy
# @Project ： dnssec-error-detect


import numpy as np
import os
import matplotlib.pyplot as plt
import random
import sys


# 绘制饼图，并将结果写入文件
# 参数说明：
# error_list: 每一次错误检测的所有错误类型的list
# error_num: 每一种错误类型对应的数量的数组
# domain_name: 需要检测的域名
# error: 配置的错误
# project_root_file: 根目录的路径
def error_pie(error_list, error_num, domain_name, error, project_root_file):
    colors = ['purple', 'navy', 'green', 'red', 'teal', 'orange', 'wheat', 'tan', 'black']  # 可以设置各部分的颜色
    explode = [0, 0.1, 0.2, 0.3, 0.4, 0.05, 0.1, 0.15, 0.2, 0.1]

    data = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4]  # 这是你要从中选择的数据列表
    random_choice = random.choice(data)  # 从数据列表中随机选择一个元素
    # 根据error_num的值动态调整explode
    for i in range(len(error_num)):
        if error_num[i] > 500:
            explode[i] = 0
        elif 100 < error_num[i] <= 500:
            explode[i] = 0.02
        elif 50 < error_num[i] <= 100:
            explode[i] = 0.05
        elif 0 < error_num[i] <= 50:
            explode[i] = random.choice(data)
    # elif error_num[i] < 5:
    #    explode[i] = 0.5

    my_color = colors[0:len(error_list)]
    my_explode = explode[0:len(error_list)]

    # 饼图
    fig, ax = plt.subplots()
    ax.set_position([0.2, 0.3, 0.6, 0.6])

    ax.pie(error_num, colors=my_color, autopct='%1.1f%%', startangle=120, pctdistance=1.0, explode=my_explode,
           radius=0.7, center=(0.5, 0.5))
    center_circle = plt.Circle((0.5, 0.5), 0.40, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(center_circle)

    # 设置标题
    plt.title(domain_name.split('.')[0] + '_' + error + '_' + 'error_distribute')
    print("标签设置成功")
    # 添加标签
    ecode = ["EDE: 1", "EDE: 2", "EDE: 3", "EDE: 4", "EDE: 5", "EDE: 6", "EDE: 7", "EDE: 8", "EDE: 9"
        , "EDE: 10", "EDE: 11", "EDE: 12", "EDE: 13", "EDE: 14", "EDE: 15", "EDE: 16", "EDE: 17",
             "EDE: 18", "EDE: 19", "EDE: 20", "EDE: 21", "EDE: 22", "EDE: 23", "EDE: 24"]
    error_name = ["Unsupported DNSKEY Algorithm", "Unsupported DS Digest Type", "stale Answer", "Forged Answer",
                  "DNSSEC Indeterminate", "DNSSEC Bogus", "Signature Expired", "Signature Not Yet Valid",
                  "DNSKEY Missing",
                  "RRSIGs Missing", "No Zone Key Bit Set", "NSEC Missing", "Cached Error", "Not Ready", "Blocked",
                  "Censored", "Filtered", "Prohibited", "Stale NXDomain Answer", "Not Authoritative",
                  "Not Supported", "No Reachable Authority", "Network Error", "Invalid Data"]
    ""
    labels = error_list
    for i in range(len(labels)):
        for j in range(24):
            if ecode[j] in labels[i][2:len(labels[i])]:
                labels[i] = labels[i][2:len(labels[i])] + '(' + error_name[j] + ")"
                break

    print(labels)
    plt.legend(labels, loc="lower center", bbox_to_anchor=(0.6, -0.4), frameon=False)

    # 显示图表
    photo_file = os.path.join(project_root_file, "resources", "photos", domain_name.split('.')[0] + '_' +
                              error + "_eCode_error_distribute.png")
    plt.savefig(photo_file)
    plt.show()


# 统计每种错误的数量
# 参数说明:
# error_list: 返回错误的类型
# log_file: 返回错误的日志文件
# error_num: 每一种错误的数量数组
def visualize_error(error_list, log_file, error_num, project_root_file, errors_name, domain_names):
    log_data = np.genfromtxt(log_file, delimiter='\n', dtype=str)
    for i in range(len(error_list)):
        if error_list[i] == "no_error_code":
            index = i
            error_num[index] = 3607
            print(index)
    for row in log_data:
        # print(row)
        for i in range(len(error_list)):
            if error_list[i][2:len(error_list[i])] in row:
                print(row)
                error_num[i] += 1

    for i in range(len(error_list)):
        if i != index:
            error_num[index] -= error_num[i]

    list_error_num = []
    for i in range(len(error_list)):
        list_tmp = [error_list[i], error_num[i]]
        print(error_list[i])
        print(error_num[i])
        list_error_num.append(list_tmp)

    list_error_num_file = os.path.join(project_root_file, "data", "error_list",
                                       "eCode_list_error_num_" + domain_names.split('.')[0] + '_' +
                                       errors_name + ".csv")
    np.savetxt(list_error_num_file, list_error_num, delimiter=',', fmt='%s')
    return error_num


if __name__ == '__main__':
    # 获取项目的根路径,然后再确定相关文件路径
    # 获取当前脚本的绝对路径
    current_script_path = os.path.abspath(__file__)

    # 设置参数
    project_root = os.path.dirname(os.path.dirname(current_script_path))

    # errors = sys.argv[2]
    # domain = sys.argv[1]

    errors = "unsupportedDs"
    domain = "unsupportedDs.iwbtfy.top"

    error_list_file = os.path.join(project_root, "data", "error_list",
                                   "eCode_errors_list_" + domain.split('.')[0] + '_' +
                                   errors + ".txt")
    errors_list = []
    errors_data = np.genfromtxt(error_list_file, delimiter='\n', dtype=str)
    for row in errors_data:
        print(row)
        errors_list.append(row)
    errors_num = np.zeros(len(errors_list))
    logs_file = os.path.join(project_root, "data", "detect_logs", "eCode_detect_logs_" + domain.split('.')[0] + '_' +
                             errors + ".txt")

    # 统计error_num
    visualize_error(errors_list, logs_file, errors_num, project_root, errors, domain)

    # 绘制饼图，并写入结果
    error_pie(errors_list, errors_num, domain, errors, project_root)
    print("绘制完成")
