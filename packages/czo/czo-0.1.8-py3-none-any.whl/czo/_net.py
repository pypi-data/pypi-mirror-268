import ipaddress
from ipaddress import IPv4Address, IPv6Address
from time import sleep
from typing import Any, Generator


class NetLib:

    @staticmethod
    def cidr(address, netmask_or_prefix) -> dict[str, Any] | ValueError:
        """
        根据指定的网络和前缀长度计算CIDR信息。

        参数:
        - network: 字符串，指定的网络地址，可以是IPv4或IPv6格式。
        - prefix: 整数，网络的前缀长度。

        返回值:
        - 字典，包含CIDR信息，包括主机数量、地址范围、网络地址、广播地址和子网掩码。
        - 如果参数无效，返回ValueError异常。

        Examples:
        >>> print(Net.cidr('192.168.1.0', 24))

        >>> print(Net.cidr('240e::0', 64))
        """

        try:
            ipType: ipaddress.IPv6Network | ipaddress.IPv4Network = ipaddress.IPv6Network if ':' in address else ipaddress.IPv4Network
            cidr = ipType(f'{address}/{netmask_or_prefix}')

            # 输出网络地址、子网掩码、广播地址等信息
            host_count = cidr.num_addresses - 2
            range = str(cidr.network_address + 1) + '-' + \
                str(cidr.broadcast_address - 1)
            network_address = str(cidr.network_address)
            broadcast_address = str(cidr.broadcast_address)
            netmask = str(cidr.netmask)
            prefixlen = cidr.prefixlen

            return {'host_count': host_count, 'range': range, 'network_address': network_address, 'broadcast_address': broadcast_address, 'prefixlen': prefixlen, 'netmask': netmask}

        except ValueError as e:
            return e

    @staticmethod
    def ipaddress_generator(number: int, isIpv6: bool = False, max: int = 254, **kwargs) -> Generator[IPv4Address, IPv6Address, None]:
        """
        生成指定数量的IP地址序列。

        Args:
        - number: 每次生成的IP地址数量。
        - isIpv6: 是否生成IPv6地址，默认为False，即生成IPv4地址。
        - max: 生成IP地址的最大数量。
        - **kwargs: 可选参数，用于指定IP地址的a、b、c、d、e、f、g、h初始值。

        Returns:
        - Generator: 生成器，每次返回number个IP地址组成的列表，直到生成max个IP地址为止。

        Examples:
        >>> for i in Net.ipaddress_generator(10, True, startNumber=1, max=100):
        ...    print(";".join(map(lambda x: f"http://{str(x)}", i)))

        """
        a: int = kwargs.get("a", 1)
        b: int = kwargs.get("b", 1)
        c: int = kwargs.get("c", 1)
        d: int = kwargs.get("d", 1)
        e: int = kwargs.get("e", 1)
        f: int = kwargs.get("f", 1)
        g: int = kwargs.get("g", 1)
        h: int = kwargs.get("h", 1)

        if isIpv6 is False:
            a_range: int = 256
            b_range: int = 256
            c_range: int = 256
            d_range: int = 255
            ipList: list = []
            count: int = 0
            for _ in range(1, max+1):
                ipList.append(ipaddress.IPv4Address(f"{a}.{b}.{c}.{d}"))
                count += 1
                d += 1

                if d == d_range:
                    d = 1
                    c = c+1
                    if c == c_range:
                        c = 1
                        b = b+1
                        if b == b_range:
                            b = 1
                            a = a+1
                            if a == a_range:
                                a = 1

                if len(ipList) % number == 0:
                    yield ipList
                    ipList = []
                if max == count and len(ipList) != 0:
                    yield ipList
        else:
            a_range: int = 65536
            b_range: int = 65536
            c_range: int = 65536
            d_range: int = 65536
            e_range: int = 65536
            f_range: int = 65536
            g_range: int = 65536
            h_range: int = 65536
            ipList: list = []
            count: int = 0
            for _ in range(1, max+1):
                ipList.append(ipaddress.IPv6Address(
                    f"{a:04x}:{b:04x}:{c:04x}:{d:04x}:{e:04x}:{f:04x}:{g:04x}:{h:04x}"))
                count += 1
                h += 1

                if h == h_range:
                    h = 1
                    g = g+1
                    if g == g_range:
                        g = 1
                        f = f+1
                        if f == f_range:
                            f = 1
                            e = e+1
                            if e == e_range:
                                e = 1
                                d = d+1
                                if d == d_range:
                                    d = 1
                                    c = c+1
                                    if c == c_range:
                                        c = 1
                                        b = b+1
                                        if b == b_range:
                                            b = 1
                                            a = a+1
                                            if a == a_range:
                                                a = 1

                if len(ipList) % number == 0:
                    yield ipList
                    ipList = []
                if max == count and len(ipList) != 0:
                    yield ipList

    @staticmethod
    def ip_in_subnet(ip_str, subnet_str):
        """

        Example:
        ip = '2a00::110:133'
        subnet = '2a00::110:0/120'

        if ip_in_subnet(ip, subnet):
            print(f"{ip} 在子网 {subnet} 内")
        else:
            print(f"{ip} 不在子网 {subnet} 内")
        """

        # 将 IP 地址和子网掩码字符串转换为 IPv4Network 对象
        ip_network = ipaddress.ip_network(subnet_str)
        # 将 IP 地址字符串转换为 IPv4Address 对象
        ip_address = ipaddress.ip_address(ip_str)
        # 判断 IP 地址是否在子网内
        return ip_address in ip_network

    @staticmethod
    def ipv6_in_range(ip_str, start_str, end_str):
        """
        Example:

        ip = '2a00::110:133'
        start = '2a00::110:13'
        end = '2a00::110:133'

        if ipv6_in_range(ip, start, end):
            print(f"{ip} 在范围 {start} - {end} 内")
        else:
            print(f"{ip} 不在范围 {start} - {end} 内")

        """

        # 将起始和结束地址字符串转换为 IPv6Address 对象
        start_address = ipaddress.ip_address(start_str)
        end_address = ipaddress.ip_address(end_str)
        # 将要判断的地址字符串转换为 IPv6Address 对象
        ip_address = ipaddress.ip_address(ip_str)
        # 判断地址是否在范围内
        return start_address <= ip_address <= end_address

        # 示例用法

    @staticmethod
    def mac_generator(number: int, max: int = 10, **kwargs):
        """
        生成MAC地址
        """
        a: int = kwargs.get("a", 255)
        b: int = kwargs.get("b", 255)
        c: int = kwargs.get("c", 255)
        d: int = kwargs.get("d", 1)
        e: int = kwargs.get("e", 1)
        f: int = kwargs.get("f", 1)
        a_range: int = 256
        b_range: int = 256
        c_range: int = 256
        d_range: int = 256
        e_range: int = 256
        f_range: int = 256
        count = 0
        macList = []
        for _ in range(1, max+1):
            macList.append(f"{a:02x}:{b:02x}:{c:02x}:{d:02x}:{e:02x}:{f:02x}")
            count += 1
            f += 1
            if f == f_range:
                f = 1
                e = e+1
                if e == e_range:
                    e = 1
                    d = d+1
                    if d == d_range:
                        d = 1
                        c = c+1
                        if c == c_range:
                            c = 1
                            b = b+1
                            if b == b_range:
                                b = 1
                                a = a+1
                                if a == a_range:
                                    a = 1
            if len(macList) % number == 0:
                yield macList
                macList = []
            if max == count and len(macList) != 0:
                yield macList
