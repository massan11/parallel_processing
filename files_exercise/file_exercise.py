import threading

def generate_file(n):
    filename = f"file_{n}.txt"
    with open(filename, "w") as f:
        for i in range(1, n * 1_000_001):
            f.write(f"{i}\n")
    print(f"{filename} created successfully.")

def main():
    threads = []
    for i in range(1, 11):
        thread = threading.Thread(target=generate_file, args=(i,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
