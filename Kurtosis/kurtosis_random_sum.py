import numpy as np
import cacs_library as cl
import matplotlib.pyplot as plt

import openData as od
import index_finders as infi
import compute_pdf as cp
import basic_tools as bt

find_index = infi.find_Index

plt.style.use('presentation.mplstyle')
norm_struct = cl.structure_function.normalized_structure_function


def gen_random_shot_array(nums):
    if type(nums) != int:
        raise Exception(
            f'nums variable should be an integer. The value of nums was {nums}.')

    time = od.get_b_time()[0]
    random_data = np.zeros([nums, time.shape[0]])
    for i in range(0, nums):
        random_data[i] = np.random.normal(size=time.shape)

    return [random_data]


time = od.get_b_time()[0]
index1 = find_index(time, 60)
index2 = find_index(time, 160)

time = time[index1:index2]
dt = 0.2*1e-6
delay_index = cp.get_delay_index(dt)[0]
random_data1 = gen_random_shot_array(nums=int(50))[0]
random_data2 = gen_random_shot_array(nums=int(50))[0]
random_sum = random_data1 + random_data2

#random_mag = bt.get_mag(random_data1, random_data2, random_data3)
kurt_temp_list = []

shot_lim = np.linspace(1, 50, 50)
for shot_range in shot_lim:
    incrs = np.asarray([])
    for num in np.arange(0, int(shot_range)):
        incrs = np.append(incrs, random_sum[num][index1:index2])

    kurtosis = norm_struct(incrs, power=4)
    kurt_temp_list.append(kurtosis)

plt.figure()
plt.ylabel('Kurtosis (sum)')
plt.xlabel('Shot Average Size')
plt.plot(shot_lim, kurt_temp_list, 'o')
plt.ylim([2.9, 3.1])
# plt.show()
plt.savefig('kurt_random_sum_shot_size.png')
plt.close()
