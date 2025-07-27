# Simulating a Simple Network with Mininet

This project demonstrates a basic network topology using Mininet, consisting of two hosts connected through a single switch. This lab serves as an introduction to Mininet network emulation and basic networking concepts.

## Network Topology

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Host h1   │────│  Switch s1  │────│   Host h2   │
└─────────────┘    └─────────────┘    └─────────────┘
```

## Prerequisites

Before running this project, you need to install the following dependencies:

### 1. Install Mininet (Commands for Ubuntu)

```bash
sudo apt-get update
sudo apt-get install -y mininet
```

### 2. Python Requirements

Ensure Python 3 is installed on your system:
```bash
python3 --version
```

## Usage

### 1. Run the Network Topology

```bash
cd "Simulating a Simple Network with Mininet"
sudo python3 simple_topo.py
```

### 2. Testing Commands

Once the Mininet CLI is active, you can test the network connectivity:

#### Test connectivity between hosts:
```bash
mininet> h1 ping h2
mininet> h2 ping h1
```

#### View network topology:
```bash
mininet> net
```

#### Check host configurations:
```bash
mininet> h1 ifconfig
mininet> h2 ifconfig
```

#### Test network connectivity from specific host:
```bash
mininet> h1 ping -c 4 h2
```

#### Check switch information:
```bash
mininet> s1 ifconfig
```

## Network Configuration Details

- **Host h1**: Automatically assigned IP address by Mininet
- **Host h2**: Automatically assigned IP address by Mininet
- **Switch s1**: OpenFlow-enabled switch connecting both hosts

## Automatic Testing

The script automatically performs connectivity tests using `net.pingAll()`, which tests ping reachability between all hosts in the network. The output will show:

```
*** Ping: testing ping reachability
h1 -> h2
h2 -> h1
*** Results: 0% dropped (2/2 received)
```

## Cleanup

To exit the Mininet CLI and clean up the network:
```bash
mininet> exit
```

The script will automatically clean up all network resources when you exit.

## Learning Objectives

This project demonstrates:
- Basic Mininet network emulation
- Simple network topology creation
- Host-to-host connectivity testing
- Mininet CLI interaction
- Network troubleshooting fundamentals
- Understanding of switches and hosts in a network
