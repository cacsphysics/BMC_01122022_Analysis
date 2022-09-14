# BMC_01122022_Analysis
A repository containing notes on the 01122022 Dataset. A walkthrough will be provided for: to help others follow the analysis and for record keeping on my end.


The primariy objective is to investigate the Taylor scale on 90+ dataset. The analysis will have a spatial component and a temporal component.

- The first step is to create a python script that uses the h5py module to open the HDF5 file and output the data for various quantities.
  - I used the HDFView [API](https://www.hdfgroup.org/downloads/hdfview/) to learn the tree structure of the h5 file.
  - Then I tested the time variable and the magnetic field variables by making plots: [bfields_time_num10.png](https://github.com/cacsphysics/BMC_01122022_Analysis/blob/main/Figures/bfields_time_num10.png) and [bmag_time_num10.png](https://github.com/cacsphysics/BMC_01122022_Analysis/blob/main/Figures/bmag_time_num10.png).
  - I did not write python functions to load teh bdot data.

- In the second step I created various figures to double check the time window ([60, 160us]) and the HPF frequency (50Khz).
  - The time window is okay
  - The HPF frequency makes sense to me
- Before moving on I want to organize the mean velocity computations
  - I want to create a h5 file containing the velocities for easier transferability and usability.
    - The motivation for converting to the information to a HDF5 file is due mainly because I have grown accustomed to working with the h5py module.
- (Fourth Step) Compute the autocorrelation times for |**B**|.
  - Computed the autocorrelation times at p5, with an average of 2.1us with a 0.5us spread. [Figure](https://github.com/cacsphysics/BMC_01122022_Analysis/blob/main/Figures/magnitude_correlation_times_p5_all.png)
- (Fifth Step) Perform the richardson extrapolation. 
