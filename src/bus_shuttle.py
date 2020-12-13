import math


# def solve():
#     f = open('./input/bus_shuttle.input')
#     # f = open('./input/test.input')
#     lines = f.readlines()
#     timestamp = int(lines[0])
#     bus_ids = [int(x) for x in filter(lambda e: e != "x", lines[1].split(","))]
#     min_id = math.inf
#     min_val = math.inf
#     depart_timestamp = 0
#     for bus_id in bus_ids:
#         upper = (int(timestamp/bus_id) + 1) * bus_id
#         # lower = (int(timestamp/bus_id) - 1) * bus_id
#         compare = upper - timestamp
#         print(f"bus id : {bus_id} == {timestamp} : {upper} - {compare}")
#         if compare <= min_val:
#             min_id = bus_id
#             min_val = compare
#             depart_timestamp = upper
#     print(min_id * (depart_timestamp - timestamp))


def bus_shuttle_partone():
    f = open('./input/bus_shuttle.input')
    t = int(f.readline())
    ids = [int(x) for x in filter(lambda entry: entry != "x", f.readline().split(","))]
    diff = [(x* (int(t / x) + 1) - t) for x in ids]
    print(ids[diff.index(min(diff))] * min(diff))
        

def bus_shuttle_parttwo():
    pass

if __name__ == "__main__":
    bus_shuttle_partone()