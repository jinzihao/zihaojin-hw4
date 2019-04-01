#!/usr/bin/env python
import code
from scapy.all import sniff, send, IP, UDP, DNS, DNSRR

def dns_action(packet):
    # code.interact(local=locals())
    if (packet[1].src == '10.1.2.1') and \
            (packet[3].qd.qname == 'foo.local' or packet[3].qd.qname == 'foo.local.') and \
            (packet[3].qd.qtype == 1):
        reply_packet = IP(src=packet[1].dst, dst=packet[1].src, ihl=packet[1].ihl, flags=packet[1].flags) / \
                    UDP(sport=packet[2].dport, dport=packet[2].sport) / \
                 DNS(id=packet[3].id, qr=1, opcode=0, rd=packet[3].rd, ra=1, aa=1, rcode=0, qdcount=packet[3].qdcount,
                     ancount=1, nscount=0, arcount=0, qd=packet[3].qd, an=DNSRR(rrname=packet[3].qd.qname, type=1,
                                                                                ttl=3600, rdata='10.3.3.1'))
        # packet.show()
        # reply_packet.show()
        send(reply_packet, iface='s1-eth2')

sniff(iface='s1-eth2', filter="udp dst port 53", prn=dns_action)

