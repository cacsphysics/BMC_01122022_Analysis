import numpy as np

filename = 'mean_vels_01122022_60t160_50to500kHzfilt.npz'


def get_vel_arrays():
    """ Reads the velocity npz file and outputs the numpy arrays
    Inputs:
        None
    Outputs:
        [P5P7, P19P21, P33P35] - velocity numpy arrays (km/s)
    """
    data = np.load(filename)
    mean_vels = data['mean_velocities']
    data.close()

    P5P7 = mean_vels[0]
    P19P21 = mean_vels[1]
    P33P35 = mean_vels[2]

    return [P5P7, P19P21, P33P35]
