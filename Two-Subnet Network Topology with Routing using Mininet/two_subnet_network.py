from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink

def createNetwork():
    # Initialize Mininet
    net = Mininet(controller = Controller, switch = OVSSwitch, link = TCLink)

    # Add controller
    net.addController('c0')
    info('✅ Controller added\n')

    # Add switches
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    info('✅ Switches s1 and s2 added\n')

    # Add router (implemented as a host)
    router = net.addHost('r0')

    # Add hosts for subnet 1 (172.16.20.x)
    h1 = net.addHost('h1', ip = '172.16.20.11/24', defaultRoute = 'via 172.16.20.1')
    h2 = net.addHost('h2', ip = '172.16.20.22/24', defaultRoute = 'via 172.16.20.1')
    h3 = net.addHost('h3', ip = '172.16.20.33/24', defaultRoute = 'via 172.16.20.1')
    info('✅ Hosts h1, h2, h3 added for subnet 1\n')

    # Add hosts for subnet 2 (172.16.30.x)
    h4 = net.addHost('h4', ip = '172.16.30.11/24', defaultRoute = 'via 172.16.30.1')
    h5 = net.addHost('h5', ip = '172.16.30.22/24', defaultRoute = 'via 172.16.30.1')
    h6 = net.addHost('h6', ip = '172.16.30.33/24', defaultRoute = 'via 172.16.30.1')
    info('✅ Hosts h4, h5, h6 added for subnet 2\n')

    # Add links
    # Connect hosts to switches
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s1)
    net.addLink(h4, s2)
    net.addLink(h5, s2)
    net.addLink(h6, s2)
    info('✅ Links created between hosts and switches\n')

    # Connect switches to router
    net.addLink(s1, router)
    net.addLink(s2, router)
    info('✅ Links created between switches and router\n')

    # Start network
    net.start()
    info('✅ Network started\n')

    # Configure router
    info('✅ Configuring router\n')
    # Enable IP forwarding
    router.cmd('sysctl net.ipv4.ip_forward=1')
    
    # Configure router interfaces
    router.cmd('ip addr flush dev r0-eth0')
    router.cmd('ip addr flush dev r0-eth1')
    router.cmd('ip addr add 172.16.20.1/24 dev r0-eth0')
    router.cmd('ip addr add 172.16.30.1/24 dev r0-eth1')
    
    # Add static routes if needed
    router.cmd('ip route add 172.16.20.0/24 dev r0-eth0')
    router.cmd('ip route add 172.16.30.0/24 dev r0-eth1')

    # Start CLI
    CLI(net)

    # Clean up
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    createNetwork()
