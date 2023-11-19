# _*_ coding:utf-8 _*_
# @Time : 2023-10-30 12:08
# @Author ： iwbtfy
# @Project ： DNSSec-configuration-error-detection


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
    explode = [0, 0.1, 0.2, 0.3, 0.4, 0.05, 0.1, 0, 15]

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
        elif 0 <= error_num[i] <= 50:
            explode[i] = random.choice(data)
       # elif error_num[i] < 5:
        #    explode[i] = 0.5

    my_color = colors[0:len(error_list)]
    my_explode = explode[0:len(error_list)]

    # 饼图
    plt.pie(error_num, colors=my_color, autopct='%1.1f%%', startangle=120, pctdistance=1.15, explode=my_explode,
            radius=0.7)
    center_circle = plt.Circle((0, 0), 0.40, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(center_circle)

    # 设置标题
    plt.title(domain_name.split('.')[0] + '_' + error + '_' + 'error_distribute')

    # 添加标签
    labels = error_list
    for i in range(len(labels)):
        labels[i] = labels[i].replace(';', '').replace(' ', '', 1)
	
    print(labels)
    plt.legend(labels, loc="lower center", bbox_to_anchor=(0.5, -0.1), frameon=False)

    # 显示图表
    photo_file = os.path.join(project_root_file, "resources", "photos", domain_name.split('.')[0] + '_' +
                              error + "_error_distribute.png")
    plt.savefig(photo_file)
    plt.show()


# 统计每种错误的数量
# 参数说明:
# error_list: 返回错误的类型
# log_file: 返回错误的日志文件
# error_num: 每一种错误的数量数组
def visualize_error(error_list, log_file, error_num):
    log_data = np.genfromtxt(log_file, delimiter='\n', dtype=str)
    for row in log_data:
        for i in range(len(error_list)):
            if error_list[i] == row:
                error_num[i] += 1
    return error_num


if __name__ == '__main__':
    # 获取项目的根路径,然后再确定相关文件路径
    # 获取当前脚本的绝对路径
    current_script_path = os.path.abspath(__file__)

    # 设置参数
    project_root = os.path.dirname(os.path.dirname(current_script_path))
    errors = sys.argv[2]
    domain = sys.argv[1]
    error_list_file = os.path.join(project_root, "data", "error_list", "errors_list_" + domain.split('.')[0] + '_' +
                                   errors + ".txt")
    errors_list = []
    errors_data = np.genfromtxt(error_list_file, delimiter='\n', dtype=str)
    for row in errors_data:
        print(row)
        errors_list.append(row)
    errors_num = np.zeros(len(errors_list))
    logs_file = os.path.join(project_root, "data", "detect_logs", "detect_logs_" + domain.split('.')[0] + '_' +
                             errors + ".txt")

    # 统计error_num
    visualize_error(errors_list, logs_file, errors_num)

    # 绘制饼图，并写入结果
    error_pie(errors_list, errors_num, domain, errors, project_root)
