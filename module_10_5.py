from multiprocessing import Pool
import time

def read_info(name):
    all_data = []
    with open(name) as file:
        for line in file:
            if line != '':
                all_data.append(line)
            else:
                break

filenames = [f'files/file {number}.txt' for number in range(1, 5)]

# start_time = time.time()
# for file in filenames:
#     read_info(file)
# end_time = time.time()
# print(f"время выполнения  {end_time - start_time}")

if __name__ == '__main__':
    start_time = time.time()
    with Pool(2) as p:
        p.map(read_info, filenames)
    end_time = time.time()
    print(f"время выполнения  {(end_time - start_time)}")

