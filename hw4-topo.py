#!/usr/bin/env python
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, Node
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.topo import Topo
import code
import time

class HW4Topo(Topo):
    def build(self):
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')

        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')

        # self.addLink(node1=s1, node2=s2, bw=100, intfName1="s1-eth0", intfName2="s2-eth0", delay="0ms")
        # self.addLink(node1=s2, node2=s3, bw=100, intfName1="s2-eth1", intfName2="s3-eth0", delay="0ms")
        #
        # self.addLink(node1=s1, node2=h1, bw=100, intfName1="s1-eth1", intfName2="h1-eth0", delay="0ms")
        # self.addLink(node1=s1, node2=h2, bw=100, intfName1="s1-eth2", intfName2="h2-eth0", delay="0ms")
        # self.addLink(node1=s2, node2=h3, bw=100, intfName1="s2-eth2", intfName2="h3-eth0", delay="100ms")
        # self.addLink(node1=s3, node2=h4, bw=100, intfName1="s3-eth1", intfName2="h4-eth0", delay="0ms")
        # self.addLink(node1=s3, node2=h5, bw=100, intfName1="s3-eth2", intfName2="h5-eth0", delay="0ms")

        self.addLink(node1=s1, node2=s2, bw=100, delay="0ms")
        self.addLink(node1=s2, node2=s3, bw=100, delay="0ms")

        self.addLink(node1=s1, node2=h1, bw=100, delay="0ms")
        self.addLink(node1=s1, node2=h2, bw=100, delay="0ms")
        self.addLink(node1=s2, node2=h3, bw=100, delay="1500ms")
        self.addLink(node1=s3, node2=h4, bw=100, delay="0ms")
        self.addLink(node1=s3, node2=h5, bw=100, delay="0ms")

def aggNet():
    net = Mininet(topo=HW4Topo(), link=TCLink, controller=RemoteController(name='c0', ip='127.0.0.1', port=6633))

    net.get("h1").setIP("0.0.0.0", 32, "h1-eth0")
    net.get("h2").setIP("0.0.0.0", 32, "h2-eth0")
    net.get("h3").setIP("0.0.0.0", 32, "h3-eth0")
    net.get("h4").setIP("0.0.0.0", 32, "h4-eth0")
    net.get("h5").setIP("0.0.0.0", 32, "h5-eth0")

    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    aggNet()