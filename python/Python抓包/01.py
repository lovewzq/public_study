from scapy.all import *

#设置网卡
ifs="Intel(R) Dual Band Wireless-AC 3168"

packt1 = sniff(iface=ifs,count=2)

#保存获取的数据包
wrpcap("pc2.pcap",packt1)