# DNSSec-error-detect

#### 介绍

本项目基于 RFC8914 等标准，全面梳理DNSSEC的错误配置类型，通过命令行和脚本的形式发数据包请求开展DNSSEC的错误配置检测。

## 1. 项目介绍

![framework](/resources/photos/dnssec_configuration_framework.png)

## 2. 项目目录介绍

+ codes
  + analyze_visualize_error_logs.py  ------------->分析error日志，并将其可视化
  + detect_dnssec_configuration_errors.py ------------->检测域名的错误配置，并将日志写入文件       
  + get_recursion_dnssec_nameservers.py ------------->筛选支持dnssec的递归服务器
+ data
  + nameservers
    + dns_nameserver_re_dnssec_1000.txt------------->1000个支持dnssec的递归服务器
    + dns_nameservers_original.csv------------->原始的未经过筛选的服务器
    + dns_nameservers_processed_by_label.csv------------->经过标签筛选的服务器
  + error_list
  + detect_logs
+ docs
+ resources
  + photos

## 3. 使用说明

+ 进入codes目录，直接 传入域名和错误类型两个参数运行shell脚本即可
  示例：
  
  ```shell
  ./run.sh iwbtfy.top ds
  ```

## 4. 项目参与者

-------------------------------------

+ illuminate
+ iwbtfy

-------------------------------------

## 5. 参与贡献

1. Fork 本仓库
2. 新建 Feat_xxx 分支
3. 提交代码
4. 新建 Pull Request

#### 特技

1. 使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2. Gitee 官方博客 [blog.gitee.com](https://blog.gitee.com)
3. 你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解 Gitee 上的优秀开源项目
4. [GVP](https://gitee.com/gvp) 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目
5. Gitee 官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6. Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)
