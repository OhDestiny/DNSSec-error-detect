#!/bin/bash

echo "sub_domain_name: $1"

# 相关配置文件的路径
etc_directory="/etc/named.conf"
zone_directory="/var/named/$1.iwbtfy.top.zone"
key_directory="/var/named/$1_keys"
iwbtfy_zone_directory="/var/named/iwbtfy.top.zone"
iwbtfy_key_directory="/var/named/keys"

# 创建一个子域的域配置文件
touch $zone_directory

# 写入域配置
echo "\$TTL 600
$1.iwbtfy.top.	IN	SOA	ns	admin.$1.iwbtfy.top. (
                3
                1H
                5M
                2D
                6H )
$1.iwbtfy.top.	IN	NS	ns.$1.iwbtfy.top.
$1.iwbtfy.top.	IN	MX  10  mail.$1.iwbtfy.top.
ns	           	IN	A	123.207.59.193
mail		        IN	A	123.207.59.193
@               IN	A	123.207.59.193" >> $zone_directory

# 创建子域对应的keys的文件夹
mkdir $key_directory

# 生成keys
cd $key_directory
# dnssec-keygen -f KSK -a RSASHA1 -r /dev/urandom -b 512 -n ZONE $1.iwbtfy.top.
ksk=$(dnssec-keygen -f KSK -a RSASHA256 -r /dev/urandom -b 2048 -n ZONE $1.iwbtfy.top. | grep iwbtfy)
echo $ksk
# dnssec-keygen -a RSASHA1 -r /dev/urandom -b 512 -n ZONE $1.iwbtfy.top.
zsk=$(dnssec-keygen -a RSASHA256 -r /dev/urandom -b 1024 -n ZONE $1.iwbtfy.top. | grep iwbtfy)
echo $zsk

# 将keys写入到域配置中
echo "\$INCLUDE \"$key_directory/$ksk.key\"
\$INCLUDE \"$key_directory/$zsk.key\" " >> $zone_directory

# 生成ds记录
ds=$(dnssec-dsfromkey -2 $ksk.key)
echo $ds
# 将ds记录写入上一级的域配置中
echo "$1             IN      NS      ns1.$1
ns1.$1         IN      A       123.207.59.193
$ds" >> $iwbtfy_zone_directory

# 使用key签名域配置
dnssec-signzone -K $key_directory -o $1.iwbtfy.top. /var/named/$1.iwbtfy.top.zone
dnssec-signzone -K $iwbtfy_key_directory -o iwbtfy.top. /var/named/iwbtfy.top.zone

# 在/etc/named.conf添加这个子域
echo "zone \"$1.iwbtfy.top\" IN {
  type master;
  auto-dnssec maintain;
  update-policy local;
  file \"$1.iwbtfy.top.zone.signed\";
  key-directory \"$key_directory\";
};" >> $etc_directory