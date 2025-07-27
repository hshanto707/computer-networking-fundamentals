from mininet.net import Mininet
from mininet.topo import Topo
from mininet.cli import CLI

class SimpleTopo(Topo):
    def build(self):
        # Add two hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')

        # Add one switch
        s1 = self.addSwitch('s1')

        # Add links between hosts and switch
        self.addLink(h1, s1)
        self.addLink(h2, s1)

# Create and start the network
if __name__ == '__main__':
    topo = SimpleTopo()  # Create topology
    net = Mininet(topo=topo)  # Initialize Mininet
    net.start()  # Start the network
    
    print('Testing network connectivity with ping...')
    net.pingAll()  # Test connectivity between hosts
    
    CLI(net)  # Launch Mininet CLI for manual testing
    net.stop()  # Stop the network
