import numpy as np
import time

start = time.time()
array = np.random.rand(1000,1000)
finish = time.time() 
print(f"creation time = {finish-start}s\n")
print(f"created array \n {array[0][:10]}\n")


array_to_bytes = array.tobytes()
print(f"converted to bytes \n {array_to_bytes[:10]}\n")

recreated = np.frombuffer(array_to_bytes).reshape(1000,1000)
print(f"recreated from bytes \n {recreated[0][0:10]}")
