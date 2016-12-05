# allow_ssh_ip_address
add IP address to white list

# 部署
- 安装 iptables-persistent
- 添加 IP 地址的 CGI: /usr/lib/cgi-bin/allow-ssh-ip-address.py
- 查看当前用户名的 CGI： /usr/lib/cgi-bin/whoami.cgi。当前用户要有 sudo 权限
- allow-ssh-ip-address 修改 iptables 配置文件的脚本


