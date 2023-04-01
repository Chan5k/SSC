import os
import time

def test_disk_speed():
    file_size = 1024 * 1024 * 100 # 100 MB
    file_path = "/tmp/test_file"
    with open(file_path, "wb") as f:
        f.write(os.urandom(file_size))
    print("Testing disk read speed...")
    start_time = time.time()
    with open(file_path, "rb") as f:
        f.read()
    end_time = time.time()
    read_speed = file_size / (end_time - start_time) / 1000000
    print("Read speed: {:.2f} MB/s".format(read_speed))
    print("Testing disk write speed...")
    start_time = time.time()
    with open(file_path, "wb") as f:
        f.write(os.urandom(file_size))
    end_time = time.time()
    write_speed = file_size / (end_time - start_time) / 1000000
    print("Write speed: {:.2f} MB/s".format(write_speed))
    os.remove(file_path)

if __name__ == "__main__":
    test_disk_speed()
