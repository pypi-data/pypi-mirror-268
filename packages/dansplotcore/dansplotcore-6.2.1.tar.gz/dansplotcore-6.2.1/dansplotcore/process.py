import math

def bucket(l, bucket_count=None):
    if bucket_count == None:
        bucket_count = math.ceil(len(l) / 10)
    data_min = min(l)
    data_max = max(l)
    data_range = data_max - data_min
    bucket_size = data_range / bucket_count * 1.001
    buckets = [0 for _ in range(bucket_count)]
    for i in l:
        index = math.floor((i - data_min) / bucket_size)
        buckets[index] += 1
    return [(data_min + i * bucket_size, v) for i, v in enumerate(buckets)]
