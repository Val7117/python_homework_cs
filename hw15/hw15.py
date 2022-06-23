#!/usr/bin/env python3

# Import ipaddress module

import ipaddress


# Creating Router class

class Router:
    """
    A class is used to represent a router using the name of the model and the number of ports the router has.
    ...
    Attributes
    ----------
    model: str
        The model/name/vendor of the router
    num_of_ports: int
        The number of ports the router has. All ports have the format like eth1, eth2, snd so on.

    Methods
    -------
    add_ipv4(ip, interface)
        Assigns the ip address to the interface. Default mask is /32.
    show_ip_table(self)
        Prints the IP table line by line.
    remove_ipv4(self, ip)
        Removes the IPv4 address from IP table. Default mask is /32.
    add_route(self, destination, next_hop)
        Adds route to the IP route table. Default mask is /32.
    remove_route(self, destination)
        Removes the route to the destination from the IP route table. Default mask is /32.
    show_ip_route(self)
        Shows IP route table.
    """

# Create two additional dictionaries for storing info about IP table and ip routes.
    ip_table = dict()
    ip_routes = dict()

    def __init__(self, model, num_of_ports):
        """
        Parameters
        ----------
        model: str
            The model of the router.
        num_of_ports: int
            The number of ports the router has.
        """

        self.model = model
        self.num_of_ports = num_of_ports
        # Adding ports to the IP table dict in the format like eth1, eth2, ..., eth{num_of_ports}.
        # Assigns to each port 'Not defined' since no ip addresses have been assigned yet.
        # Print that the router with defined model and the number of ports have been created.
        for port in range(1, num_of_ports + 1):
            self.ip_table.update({f"eth{port}": "Not defined"})
        print(f"{self.model} router with {num_of_ports} ports has been created.")

    def add_ipv4(self, ip, interface):
        """
        Assigns the IPv4 address to the interface. Default mask is /32. If you want to define another mask,
        then simply add /mask to the ip address. Example: '192.168.1.1/24' - mask 255.255.255.0 or /24.
        Make sure to define the correct port.

        Parameters:
        ----------
        ip: str
            The IPv4 address you want to assign to the interface. Example: "10.0.0.1/24".
            Make sure to define a mask, otherwise the default mask /32 will be set.
        interface: str
            The interface you want to assign the ip address to. Make sure to define the correct interface.
            Use show_ip_table() method to see all available interfaces.

        Raises
        ------
        There is no such interface
            If there is no such interface in the router. Use show_ip_table() method to see all available
            interfaces.

        """
        # If the interface is in IP table then update IP table and assign the IPv4 address to the
        # corresponding interface.
        # Get a network address from entered ip address and add the pair network:interface
        # to the ip route table. Print {ip} address is assigned to interface {interface}
        # If the interface is not in IP table then return 'There is not such interface'.

        if interface in self.ip_table:
            ipv4 = ipaddress.ip_interface(ip).compressed
            self.ip_table.update({interface: ipv4})
            route = ipaddress.ip_network(ipv4, strict=False).compressed
            self.ip_routes.update({route: f"{ipv4} {interface}"})
            print(f"{ipv4} is assigned to interface {interface}")
        else:
            return print("There is no such interface")

    def show_ip_table(self):
        """
        Prints the IP table line by line.
        """
        print("Interface                IPv4 Address/Mask")
        print("----------------------------------------------------------")
        for i in self.ip_table:
            print(f"{i}                     {self.ip_table[i]}")

    def add_route(self, destination, next_hop):
        """
        Adds route to the IP route table. If the route is added, prints the result and "ok".
        If the route is not added, prints the result and "exception".
        ! Be careful, if there was a gateway to the network you have just added,
        the result will be "exception" and the newly-defined route will be added,
        but the old route to the exact same network will be deleted.

        Parameters:
        -----------
        destination: str
            The IPv4 address of the destination network.
        next_hop: str
            The IPv4 address of the next hop.
        """

        # Creates 2 global variable for additional purpose
        # Defines length of IP route table for additional checking.
        # For all routes in IP route table search if there is a gateway to the newly-defined network.
        # If such a gateway exists, then add the pair new_destination:new_next_hop to the IP route table.
        # Print the details and the result - "ok"
        # If such a gateway does not exist, then print the details and the result - "exception".
        global new_destination
        global new_next_hop
        length = len(self.ip_routes)
        for route in self.ip_routes:
            if ipaddress.ip_interface(next_hop) in ipaddress.ip_network(route, strict=False):
                new_destination = ipaddress.ip_network(destination, strict=False).compressed
                new_next_hop = ipaddress.ip_interface(next_hop).compressed
                continue
        self.ip_routes.update({new_destination: new_next_hop})
        if length < len(self.ip_routes):
            return print(f"Adding route to {new_destination} via {new_next_hop} - ok")
        else:
            return print(f"Adding route to {ipaddress.ip_network(destination, strict=False).compressed} via {ipaddress.ip_interface(next_hop).compressed} - exception")

    def remove_route(self, destination):
        """
        Removes the route to the destination from the IP route table.

        Parameters:
        -----------
        destination: str
            IPv4 address of the network to which you want to delete the route from IP route table.
            Make sure to define a mask, otherwise the default mask /32
            will be set.

        Raises:
        -------
        There is no such destination network.
            If there is not the IPv4 of the destination network in the IP route table.
        """

        # If there is the IPv4 of the destination network in the IP route table, then remove
        # this destination network and the IPv4 address of the next hop to that network from
        # the IP route table.
        # If there is no the IPv4 of the destination network in the IP route table, then
        # print "There is no such destination network".
        if ipaddress.ip_network(destination, strict=False).compressed in self.ip_routes:
            delete = ipaddress.ip_network(destination, strict=False).compressed
            self.ip_routes.pop(delete)
            print(f"Network {destination} is removed from IP Route table")
        else:
            print("There is no such destination network")

    def remove_ipv4(self, ip):
        """
        Removes the IPv4 address from IP table. Make sure to define a mask, otherwise the default mask /32
        will be set.

        Parameters:
        -----------
        ip: str
            The IPv4 address you want to remove.

        Raises:
        ------
        Address is not found in IP table.
            If you want to remove IPv4 address that does not exist.
        """

        # Search through the IP table. If the ip address you want to remove is found, then set IPv4 address
        # as "Not defined". Also delete this IP network from IP route table.
        # Otherwise return {ip} address is not found in IP table.
        for i in self.ip_table:
            if self.ip_table[i] == ipaddress.ip_interface(ip).compressed:
                self.ip_table.update({i: "Not defined"})
                for j in self.ip_routes:
                    if j == ipaddress.ip_network(ip, strict=False).compressed:
                        delete = ipaddress.ip_network(ip, strict=False).compressed
                self.ip_routes.pop(delete)
                return print(f"{ip} was removed from IP table")
        else:
            return print(f"{ip} address is not found in IP table")

    def show_ip_route(self):
        """
        Shows IP route table.
        """
        print("Destination Network                      Gateway")
        print("----------------------------------------------------------")
        for j in self.ip_routes:
            print(f"{j}                             {self.ip_routes[j]}")

