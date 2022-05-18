# Find the secret server walkthrough

1) Find the address of kali instance

```ip addr```

```
3: eth1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 08:00:27:d4:ee:5d brd ff:ff:ff:ff:ff:ff
    inet 10.175.34.140/24 brd 10.175.34.255 scope global eth1
```

2) Check the routes on the kali machine

```route```

```
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface

default         10.1.0.1        0.0.0.0         UG    0      0        0 adlab0
10.1.0.0        0.0.0.0         255.255.255.0   U     0      0        0 adlab0
10.175.34.0     0.0.0.0         255.255.255.0   U     0      0        0 eth1
172.16.88.0     10.175.34.1     255.255.255.0   UG    0      0        0 eth1
192.168.241.0   10.175.34.1     255.255.255.0   UG    0      0        0 eth1
```
Kali is connected to 10.175.34.0/24 , 172.16.88.0/24 and 192.168.241.0/24 networks on eth1.

The task says the wenservers are on 172.16.88.81 and 192.168.241.12 and 192.168.222.199

However Kali isn't connected to 192.168.222.0/24 so cannot access 192.168.222.199

Add the network to the route table

```
ip route add 192.168.222.0/24 via 10.175.34.1
```

to delete just change add to del