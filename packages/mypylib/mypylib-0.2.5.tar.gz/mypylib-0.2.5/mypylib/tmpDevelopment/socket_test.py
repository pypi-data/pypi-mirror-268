import asyncio
import socket
import binascii
import struct

async def recv_packet(recv_socket):
    print("Waiting for ARP packets...")
    packet, _ = await recv_socket.recvfrom(2048)
    if packet[12:14] == b'\x08\x06':  # Check if it's an ARP packet
        print(f"Received ARP packet: {binascii.hexlify(packet)}")

async def send_packet(send_socket, src_mac, src_ip, dst_mac, dst_ip):
    # Create ARP request packet
    eth_hdr = struct.pack("!6s6s2s", binascii.unhexlify(dst_mac.replace(":", "")),
                          binascii.unhexlify(src_mac.replace(":", "")), b"\x08\x06")
    arp_hdr = struct.pack("!2s2s1s1s2s", b"\x00\x01", b"\x08\x00", b"\x06", b"\x04", b"\x00\x01")
    arp_sender = struct.pack("!6s4s", binascii.unhexlify(src_mac.replace(":", "")),
                             socket.inet_aton(src_ip))
    arp_target = struct.pack("!6s4s", binascii.unhexlify(dst_mac.replace(":", "")),
                             socket.inet_aton(dst_ip))

    arp_packet = eth_hdr + arp_hdr + arp_sender + arp_target

    # Send ARP request packet
    send_socket.sendto(arp_packet, (dst_ip, 0))
    print(f"Sent ARP packet: {binascii.hexlify(arp_packet)}")

async def main():
    interface = "ens33"
    src_mac = "00:0c:29:71:a6:d6"
    src_ip = "192.168.160.128"
    dst_mac = "ff:ff:ff:ff:ff:ff"  # Broadcast
    dst_ip = "192.168.160.128"

    # Create sockets
    recv_socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0806))
    send_socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)

    # Bind recv_socket to interface
    recv_socket.bind((interface, 0))

    # Start receiving and sending tasks
    recv_task = asyncio.create_task(recv_packet(recv_socket))
    await asyncio.sleep(1)  # Wait for receiver to start listening

    await send_packet(send_socket, src_mac, src_ip, dst_mac, dst_ip)

    await recv_task

    # Close sockets
    recv_socket.close()
    send_socket.close()

asyncio.run(main())
