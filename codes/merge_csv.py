# _*_ coding:utf-8 _*_
# @Time : 2024-03-06 11:50
# @Author ： iwbtfy
# @Project ： dnssec-error-detect

import pandas as pd
import os

file_list = ["eCode_list_error_num_dnskeyMissing_dnskeyMissing.csv",
             "eCode_list_error_num_noZoneKey_noZoneKey.csv",
             "eCode_list_error_num_nsecMissing_nsecMissing.csv",
             "eCode_list_error_num_rrsigMissing_rrsigMissing.csv",
             "eCode_list_error_num_signatureExpired_signatureExpired.csv",
             "eCode_list_error_num_signatureNotValid_signatureNotValid.csv",
             "eCode_list_error_num_unsupportedDnskey_unsupportedDnskey.csv",
             "eCode_list_error_num_unsupportedDs_unsupportedDs.csv"]

current_script_path = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(current_script_path))

df_dnskeyMissing = pd.read_csv(os.path.join(project_root, "data", "error_list", file_list[0]))
df_noZoneKey = pd.read_csv(os.path.join(project_root, "data", "error_list", file_list[1]))
df_nsecMissing = pd.read_csv(os.path.join(project_root, "data", "error_list", file_list[2]))
df_rrsigMissing = pd.read_csv(os.path.join(project_root, "data", "error_list", file_list[3]))
df_signatureExpired = pd.read_csv(os.path.join(project_root, "data", "error_list", file_list[4]))
df_signatureNotValid = pd.read_csv(os.path.join(project_root, "data", "error_list", file_list[5]))
df_unsupportedDnskey = pd.read_csv(os.path.join(project_root, "data", "error_list", file_list[6]))
df_unsupportedDs = pd.read_csv(os.path.join(project_root, "data", "error_list", file_list[7]))

merged_df = pd.concat([df_dnskeyMissing, df_noZoneKey, df_nsecMissing, df_rrsigMissing, df_signatureExpired
                       , df_signatureNotValid, df_unsupportedDnskey, df_unsupportedDs], axis=1)

merged_df.to_csv(os.path.join(project_root, "data", "error_list", "merge_csv.csv"))
# csv文件列表

# 循环打开csv，读取csv，写入新的csv
