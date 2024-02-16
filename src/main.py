import numpy as np
import matplotlib.pyplot as plt
import segyio

# load seismic data
filename = './data/SEAM_Interpretation_Challenge_1_Depth/SEAM_Interpretation_Challenge_1_Depth.sgy'

# plot 3d seismic data

with segyio.open(filename, "r") as segyfile:
    segyfile.mmap()
    # Get basic attributes
    n_traces = segyfile.tracecount
    sample_rate = segyio.tools.dt(segyfile)
    n_samples = segyfile.samples.size
    twt = segyfile.samples
    data = segyfile.trace.raw[:]
    data = np.transpose(data)

    # Create a time axis for the data
    t = np.arange(0, n_samples, 1) * sample_rate / 1000

    # Create a 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    # Plot the data with a color map
    for i in range(0, min(n_traces, data.shape[0]), 10):
        ax.plot(t[:n_samples], np.ones(n_samples) * i, data[i, :n_samples], linewidth=0.5)

    # Set the labels
    ax.set_xlabel("Time (ms)")
    ax.set_ylabel("Trace number")
    ax.set_zlabel("Amplitude")

    # Adjust the viewing angle
    ax.view_init(elev=30, azim=45)

    ax.plot(t[:n_samples], np.ones(n_samples) * i, data[i, :n_samples], linewidth=0.5)
