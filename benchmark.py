import random
import time
import matplotlip.pyplot as plt
import heapq
def quick_sort(arr)
 if len(arr) <= 1:
   return arr
 pivot = arr[len(arr)//2]
 left = [x for x in arr if x < pivot]
 mid = [x for x in arr if x == pivot]
 right = [x for x in arr if x > pivot]
 return quick_sort(left) + mid + quick_sort(right)
def merge_sort(arr):
  if len(arr) <= 1:
    return arr
  mid = len(arr)//2
  left = merge_sort(arr[:mid])
  right = merge_sort(arr[mid:])
  res = []
  i = j = 0
  while  i < len(left) and j < len(right):
    if left[i] < right[j]:
      res.append(left[i]); i+=1
    else:
      res.append(right[j]); j+=1
  res.extend(left[j:]); res.extend(right[j:])
  return res

def heap_sort(arr):
  heapq.heapify(arr)
  return [ heapq.heappop(arr) for _ in range(len(arr))]
sizes = [1000, 5000, 10000, 20000]
q_times, m_times, h_times = [], [], []
for n in sizes:
  data = [random.randint(0,100000) for _ in range(n)]
  start = time.time(); quick_sort(data.copy());
q_times.append(time.time()-start)
  start = time.time(); merge_sort(data.copy));
m_times.append(time.time()-start)
  start = time.time();heap_sort(data.copy();
h_times.append(time.time()-start)
  print(f"n={n} Quick={q_times[-1]:.4f} Merge={m_times[-1]:.4f}
Heap={h_times[-1]:.4f}")
plt.plot(size, q_times, marker='o',label='Quick Sort')
plt.plot(size, m_times, marker='o',label='Merge Sort')
plt.plot(size, h_times, marker='o',label='Heap Sort')
plt.xlabel('Input Size (n)')
plt.ylabel('Time (seconds)')
plt.title('Heap vs Quick vs Merge')
plt.legend()
plt.grid(True)
plt.savefig('result.png')
plt.show()
