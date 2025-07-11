# Two-Subnet Network Topology with Routing using Mininet

This project demonstrates a simple two-subnet network topology with routing capabilities using Mininet. The network consists of two subnets connected through a router, allowing hosts in different subnets to communicate with each other.

## Network Topology

```
Subnet 1 (172.16.20.0/24)          Subnet 2 (172.16.30.0/24)
┌─────────────────┐                ┌─────────────────┐
│   Switch s1     │                │   Switch s2     │
│                 │                │                 │
│ h1: 172.16.20.11│                │ h4: 172.16.30.11│
│ h2: 172.16.20.22│                │ h5: 172.16.30.22│
│ h3: 172.16.20.33│                │ h6: 172.16.30.33│
└─────────┬───────┘                └─────────┬───────┘
          │                                  │
          └─────────── Router r0 ────────────┘
                    172.16.20.1/24
                    172.16.30.1/24
```

## Prerequisites

Before running this project, you need to install the following dependencies:

### 1. Install Mininet (Commands for Ubuntu)

```bash
sudo apt-get update
sudo apt-get install -y mininet
sudo apt-get install -y tcproute
```

## Usage

### 1. Run the Network Topology

```bash
cd "Two-Subnet Network Topology with Routing using Mininet"
sudo python3 two_subnet_network.py
```

### 2. Testing Commands

Once the Mininet CLI is active, you can test the network connectivity:

#### Test connectivity within Subnet 1:
```bash
mininet> h1 ping h2
mininet> h2 ping h3
```

#### Test connectivity within Subnet 2:
```bash
mininet> h4 ping h5
mininet> h5 ping h6
```

#### Test connectivity between subnets (routing):
```bash
mininet> h1 ping h4
mininet> h6 ping h2
```

#### Test router connectivity:
```bash
mininet> h1 ping 172.16.20.1
mininet> h4 ping 172.16.30.1
```

#### View network topology:
```bash
mininet> net
```

#### Check host configurations:
```bash
mininet> h1 ifconfig
mininet> h4 ifconfig
```

#### Test traceroute between subnets:
```bash
mininet> h1 traceroute h4
```

## Network Configuration Details

- **Subnet 1**: 172.16.20.0/24
  - Hosts: h1 (172.16.20.11), h2 (172.16.20.22), h3 (172.16.20.33)
  - Gateway: 172.16.20.1 (router interface)

- **Subnet 2**: 172.16.30.0/24
  - Hosts: h4 (172.16.30.11), h5 (172.16.30.22), h6 (172.16.30.33)
  - Gateway: 172.16.30.1 (router interface)

- **Router**: r0 with two interfaces
  - Interface 1: 172.16.20.1/24 (connected to Subnet 1)
  - Interface 2: 172.16.30.1/24 (connected to Subnet 2)

## Cleanup

To exit the Mininet CLI and clean up the network:
```bash
mininet> exit
```

The script will automatically clean up all network resources when you exit.

## Learning Objectives

This project demonstrates:
- Network subnetting concepts
- Router configuration and IP forwarding
- Inter-subnet communication
- Network topology design
- Mininet network emulation
