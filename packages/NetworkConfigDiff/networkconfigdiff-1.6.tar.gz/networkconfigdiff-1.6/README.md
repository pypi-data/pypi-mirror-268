# 什么是NetworkConfigDiff
一个轻量级的模块,帮助比较网络设备的配置文件。比较特别的是，他计算两个网络设备的配置文件之间的差异，同时会考虑他所在的层级  
这个模块依赖于python的原生模块`difflib`，同时思路参考了`diffplus`的思路
# 为什么需要这个模块
我没有找到一个合适的模块提供这样一个上下文差异，只是基于缩进配置。
拿`difflib`来说，虽然代码中提供了参数选择上下文的行数，但是我们知道只是提供上下几行的代码是无法准确定位配置的。如
```
acl name qos advance
 rule 5 name 5 permit ip destination 192.168.9.94 0
 rule 10 name 10 permit ip destination 192.168.8.30 0
 rule 15 name 15 permit ip destination 192.168.152.41 0
 rule 20 name 20 permit ip destination 192.168.248.141 0
 rule 25 name 25 permit ip destination 192.168.0.14 0
 rule 30 name 30 permit ip destination 192.168.168.208 0
 rule 35 name 35 permit ip destination 192.168.168.226 0
 rule 40 name 40 permit ip destination 192.168.169.31 0
 rule 45 name 45 permit ip destination 192.168.169.34 0
 rule 50 name 50 permit ip destination 192.168.169.37 0
 rule 55 name 55 permit ip destination 192.168.169.40 0
 rule 60 name 60 permit ip destination 192.168.169.43 0
 rule 65 name 65 permit ip destination 192.168.29.218 0
 rule 70 name 70 permit ip destination 192.168.7.175 0
 rule 75 name 75 permit ip destination 192.164.9.29 0
 rule 80 name 80 permit ip destination 192.186.8.12 0
 rule 85 name 85 permit ip destination 10.10.164.103 0
```
当我们更改`rule 85`的时候，`difflib`给出的数据为
```
 rule 70 name 70 permit ip destination 192.168.7.175 0
 rule 75 name 75 permit ip destination 192.164.9.29 0
 rule 80 name 80 permit ip destination 192.186.8.12 0
- rule 85 name 85 permit ip destination 10.10.164.103 0
+ rule 85 name 85 permit ip destination 10.10.164.103 01
                                                       ^
```
从差异信息完全不知道是`acl name qos advance`下的数据。
但是当我们运维时，我们是需要这方面信息来提供精确配置寻找。
所以`NetworkConfigDiff`产生了。
# 如何使用它
## 从文件读取
```
    text_a = open('./diff_text/10.86.102.241.txt', 'r', encoding='utf8').read()
    text_b = open('./diff_text/change_10.86.102.241.txt', 'r', encoding='utf8').read()
    differ, from_all_info, to_all_info = ConfigDiff(text_b, text_a).get_content_dict_and_diff()
    print(differ, from_all_info, to_all_info)
```
### 文件内容
```
#text_a 也就是旧配置
acl name qos advance
 rule 1 name 1 permit source 127.0.0.1 0
 rule 5 name 5 permit vpn-instance vpn1 source 10.240.192.0 0.0.0.255
 rule 10 name 10 permit vpn-instance vpn1 source 10.216.196.138 0
 rule 15 name 15 permit ip destination 192.168.152.41 0
 rule 20 name 20 permit ip destination 192.168.248.141 0
 rule 25 name 25 permit ip destination 192.168.0.14 0
# text_b 也就是新配置
acl name qos advance
 rule 1 name 1 permit source 127.0.0.2 0
 rule 5 name 5 permit vpn-instance vpn1 source 10.240.192.0 0.0.0.255
 rule 10 name 10 permit vpn-instance vpn1 source 10.216.196.138 0
 rule 15 name 15 permit ip destination 192.168.152.41 0
 rule 20 name 20 permit ip destination 192.168.248.141 0
 rule 25 name 25 permit ip destination 192.168.0.14 0
```
## 结果为
```
# differ 携带上下文的差异信息
  acl name qos advance
-  rule 1 name 1 permit source 127.0.0.2 0
?                                      ^

+  rule 1 name 1 permit source 127.0.0.1 0
?                                      ^
# 携带上下文的新配置信息
acl name qos advance
 rule 1 name 1 permit source 127.0.0.2 0
 
# 携带上下文的旧配置信息
acl name qos advance
 rule 1 name 1 permit source 127.0.0.1 0
 
# 新配置中携带上下文的字典信息
{'acl name qos advance': {' rule 1 name 1 permit source 127.0.0.2 0': {}}}

# 旧配置中携带上下文的字典信息
{'acl name qos advance': {' rule 1 name 1 permit source 127.0.0.1 0': {}}}
```
**注** 因为是手工恢复配置,所以没有恢复配置中应该存在的 # 或 ！

# 限制
1、目前不支持三层之上嵌套配置