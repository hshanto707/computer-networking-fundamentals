# Simulating a Two-Subnet Network Topology in Mininet with One Switch

This project demonstrates a network topology with one switch connecting two subnets, each containing two hosts. This lab shows how subnets work and why hosts in different subnets cannot communicate without routing.

## Network Topology

```
IP Subnet 1 (192.168.0.0/24)          IP Subnet 2 (192.168.1.0/24)
┌─────────────────┐                    ┌─────────────────┐
│   Host h10      │                    │   Host h20      │
│ 192.168.0.10/24 │                    │ 192.168.1.20/24 │
│                 │                    │                 │
│   Host h11      │                    │   Host h21      │
│ 192.168.0.11/24 │                    │ 192.168.1.21/24 │
└─────────┬───────┘                    └─────────┬───────┘
          │                                      │
          └───────────── Switch br0 ─────────────┘
```

## Prerequisites

Install Mininet on Ubuntu:
```bash
sudo apt-get update
sudo apt-get install -y mininet
```

Ensure Python 3 is installed: `python3 --version`

## Usage

### Run the Network
```bash
cd "Simulating a Two-Subnet Network Topology in Mininet with One Switch"
sudo python3 two_subnet_topo.py
```

### Test Connectivity
Once in Mininet CLI:

#### Test within same subnet (should work):
```bash
mininet> h10 ping -c 3 h11    # Subnet 1
mininet> h20 ping -c 3 h21    # Subnet 2
```

#### Test across subnets (should fail):
```bash
mininet> h10 ping -c 3 h20    # Cross-subnet
mininet> h11 ping -c 3 h21    # Cross-subnet
```

#### View network info:
```bash
mininet> net                   # Show topology
mininet> h10 ifconfig          # Check IP config
mininet> pingall               # Test all connections
mininet> exit                  # Cleanup and exit
```

## Network Configuration

- **Subnet 1 (192.168.0.0/24)**: h10 (192.168.0.10), h11 (192.168.0.11)
- **Subnet 2 (192.168.1.0/24)**: h20 (192.168.1.20), h21 (192.168.1.21)
- **Switch br0**: Open vSwitch connecting all hosts

## Key Learning Points

- **Subnet isolation**: Hosts in different subnets cannot communicate without routing
- **Layer 2 switching**: Switch operates at Layer 2, only forwards within same subnet
- **IP addressing**: Understanding subnet masks and network boundaries
- **Network troubleshooting**: Using ping to test connectivity

## Expected Results

- ✅ **Same subnet**: Hosts can ping each other
- ❌ **Different subnets**: Hosts cannot ping each other (no routing configured)

## Why Cross-Subnet Pings Fail

The switch `br0` operates as a Layer 2 device and can only forward traffic within the same subnet. Without a router or Layer 3 configuration, packets between different subnets cannot be routed. 