# This script simulates a single McCulloch-Pitts neuron receiving a series of inputs from a set of binary neurons

using Plots

# neuron parameters
theta = 10 # neural threshold
N = 10 # number of input neurons
w = randn(N)

# Make input patterns
Npatterns = 20 # number of input patterns
f = 0.25 # average fraction of active neurons in each input pattern
X = 2*floor.(rand(N,Npatterns) .+f) .- 1 # Matrix of set of input patterns

# Compute output
y = sign.(w'*X)

# Plot
p1 = Plots.heatmap(-X,xlabel="",ylabel="Input neurons",colorbar=false,color=:gray,layout = grid(2,1,heights=[0.9,0.1]),ylim=(0.5,10.5),xaxis=nothing,xlim=(0,20.5))
p2 = Plots.heatmap!(-y,colorbar=false,color=:gray,xlabel="Time",subplot=2,yaxis=nothing,ylabel="Output \n neuron",xlim=(0,20.5))
savefig("MP_example.png")
