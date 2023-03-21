### 创建用户
```bash
useradd -m -d /home/jli jli
passwd jli
```
赋予sudo权限，用管理员编辑/etc/sudoers，增加行
```
jli  ALL=(ALL:ALL) ALL
```
注意用x！保存退出

### 修改hostname
```
sudo vim /etc/hostname
```

### 修改hosts文件
```
sudo vim /etc/hosts
hosts文件中添加如下内容
218.193.209.170 chem170
218.193.209.171 chem171
218.193.209.172 chem172
218.193.209.173 chem173
218.193.209.174 chem174
192.168.132.74 chem74
192.168.132.75 chem75
192.168.132.76 chem76
192.168.132.77 chem77
192.168.132.78 chem78
192.168.132.79 chem79
192.168.132.97 chem97
````