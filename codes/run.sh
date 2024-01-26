#!/bin/bash

# 初始化变量
domain_name=""                 # 要检测的域名
error=""                       # 要检测的错误类型
help_flag=0                    # 是否打印帮助页的标志位

# 显示帮助函数
show_help(){
  echo "Usage: $0 -d domain_name -e error"
  echo "    -d  指定要检测的域名"
  echo "    -e  指定要检测的错误类型"
}

# 使用getopts 处理选项
while getopts "d:e:h" opt; do
  case $opt in
    d)
      domain_name="$OPTARG"
      help_flag=$(expr $help_flag + 1)
      ;;
    e)
      error="$OPTARG"
      help_flag=$(expr $help_flag + 1)
      ;;
    h)
      help_flag=1
      ;;
    \?)
      echo "Invalid option: -$OPTARG"
      exit 1
      ;;
  esac
done

# 判断help的flag，是否要输出help指令
if [ $help_flag -lt 2 ]; then
  show_help
  exit 0
fi

echo "domain_name: $domain_name"
echo "error: $error"

python3 detect_dnssec_configuration_errors_Ecode.py "$domain_name" "$error"
python3 analyze_visualize_error_logs_Ecode.py $domain_name $error

echo "DONE"
