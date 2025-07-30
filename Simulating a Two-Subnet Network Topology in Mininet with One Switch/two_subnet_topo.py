from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info

class TwoSubnetTopo(Topo):
    def build(self):
        # Add bridge
        br0 = self.addSwitch('br0', cls = OVSKernelSwitch, failMode = 'standalone')

        # Add hosts for subnet 192.168.1.0/24
        h20 = self.addHost('h20', ip = '192.168.1.20/24')
        h21 = self.addHost('h21', ip = '192.168.1.21/24')

        # Add hosts for subnet 192.168.0.0/24
        h10 = self.addHost('h10', ip = '192.168.0.10/24')
        h11 = self.addHost('h11', ip = '192.168.0.11/24')

        # Add links between hosts and bridge
        self.addLink(h20, br0)
        self.addLink(h21, br0)
        self.addLink(h10, br0)
        self.addLink(h11, br0)

def start_network():
    """Initialize and start the network"""
    topo = TwoSubnetTopo()
    net = Mininet(topo=topo, switch=OVSKernelSwitch)
    net.start()

    info('*** Network is ready\n')
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    start_network()
