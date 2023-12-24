### 4.1 Unsupported DNSKEY Algorithm

+ 获取dnskey的加密算法
+ 比对受支持的加密算法

### 4.2 Unsupported DS Digest Type

+ 获取ds的摘要类型
+ 比对受支持的摘要类型

### 4.3 stale Answer

### 4.4 Forged Answer

+ 验证dnssec的配置准确性

### 4.5 DNSSEC Indeterminate

AD标志位是0(验证失败)，且CD标志位是0(验证已经启用)

### 4.6 DNSSEC Bogus

AD：0 RCODE：2 CD：0

### 4.7 Signature Expired

+ 获取RRSIG信息
+ 获取当前的时间
+ 比较结束时间和当前时间

### 4.8 Signature Not Yet Valid

+ 获取RRSIG信息
+ 获取当前时间
+ 比较开始时间和当前时间

### 4.9 DNSKEY Missing

+ 直接获取dnskey，判断dnskey记录是不是none

### 4.10 RRSIGs Missing

+ 直接获取RRSIGs，判断RRSIG是不是none

### 4.11 No Zone Key Bit Set

+ 获取所有dnskey
+ 循环遍历查找zsk  用途字段 最低位是1

### 4.12 NSEC Missing