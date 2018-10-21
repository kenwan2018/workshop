import time  
import math  
from collections import deque  
import numpy as np  
  
class DGIM(object):  
    def __init__(self, num, error = 0.5):  
        self.num = num  
        self.error = error  
  
        #maximum number of the same size buckets  
        self.max_num = max(math.ceil(1/self.error), 2)  
  
        #datastructure to store the buckets  
        self.queues = []  
        max_index = int(math.ceil(math.log(num)/math.log(2)))  
        self.queues = [deque() for _ in range(max_index + 1)]  
  
        self.timestamp = 0  
        self.oldest_bucket_timestamp = -1  
  
    def update(self, element):  
        self.timestamp = (self.timestamp + 1) % (2 * self.num)  
  
        if(self.oldest_bucket_timestamp >= 0 and self.is_bucket_too_old(self.oldest_bucket_timestamp)):  
            self.drop_oldest_bucket()  
  
        if element == 0:  
            return  
        #if the new element is 1  
        carry_over = self.timestamp  
        if self.oldest_bucket_timestamp == -1:  
            self.oldest_bucket_timestamp = self.timestamp  
        for queue in self.queues:  
            queue.appendleft(carry_over)  
            if len(queue) <= self.max_num:  
                break  
            last = queue.pop()  
            second_last = queue.pop()  
            carry_over = second_last  
            if last == self.oldest_bucket_timestamp:  
                self.oldest_bucket_timestamp = second_last  
  
    def is_bucket_too_old(self, bucket_timestamp):  
        return (self.timestamp - bucket_timestamp) % (2 * self.num) >= self.num  
  
    def drop_oldest_bucket(self):  
        for queue in reversed(self.queues):  
            if len(queue) > 0:  
                queue.pop()  
                break  
        self.oldest_bucket_timestamp = -1  
        for queue in reversed(self.queues):  
            if len(queue) > 0:  
                self.oldest_bucket_timestamp = queue[-1]  
                break  
  
    def get_count(self):  
        result = 0  
        max_value = 0  
        power_of_two = 1  
        for queue in self.queues:  
            queue_length = len(queue)  
            if queue_length > 0:  
                max_value = power_of_two  
                result += queue_length * power_of_two  
            power_of_two = power_of_two << 1  
        result -= math.floor(max_value/2)  
        return int(result)  
  
    def num_buckets(self):  
        result = 0  
        for queue in self.queues:  
            result += len(queue)  
        return result  
  
#main()  
start_time = time.time()  
f = open('./engg5108_stream_data1.txt')  
stream = f.read(10000)  
num = 1000  
dgim = DGIM(num)  
  
for element in xrange(10000):  
    dgim.update(int(stream[element]))  
dgim_result = dgim.get_count()  
  
print '**********'  
print "Note: The newer income element has smaller timestamp and index starts from 0.\ni.e., The last bit in the .txt file holds index = 0"  
print '**********'  
end_time = time.time()  
print "Running time %.3f seconds." % (end_time - start_time)  
print "This stream contains {0} ones in the last {1} bits.".format(dgim_result, num)  
print "The size and timestamp of the buckets are as follows."  
  
bucket_size = 1  
for queue in dgim.queues:  
    if len(queue) == 0:  
        break  
    print "bucket size: {0}, number of buckets: {1}, timestamps of buckets: {2}"\  
          .format(' '*(3-len(str(bucket_size)))+str(bucket_size), len(queue), (2*num-np.array(queue))%num)  
    bucket_size = bucket_size << 1
