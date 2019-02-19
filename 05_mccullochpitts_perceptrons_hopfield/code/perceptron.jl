# This script simulates a Perceptron training to discriminate some inputs

using Plots
pyplot()

N = 100 # number of synapses
Ptrain = 200 # Number of training patterns
eta = 0.05 # learning rate
f = 0.3 # average fraction of active input neurons

# Initialise weights
global wvec = 0.3.*randn(N) .+ 0.5
wvec = [wvec;-0.5*N]
wvecinit = wvec # save

xtarget = floor.(rand(N) .+f)
xtrain = repeat(xtarget,1,Ptrain) # make training data by randomly flipping target bits
pflip = 0.5
for i = 1:length(xtrain)
    if xtrain[i]>0.5
        if rand()<pflip
            xtrain[i] = 0.
        end
    else
        if rand()< ( pflip*f/(1. -f))
            xtrain[i] = 1.
        end
    end
end
xnegtrain = floor.(rand(N,Ptrain) .+f)

E = zeros(Ptrain)
bias = zeros(Ptrain)
for t = 1:Ptrain
    global wvec

    # Postrain
    y = sign(sum([xtrain[:,t]; 1].*wvec))
    wvec += eta*(1-y).*[xtrain[:,t]; 1]

    # Negtrain
    y = sign(sum([xnegtrain[:,t]; 1].*wvec))
    wvec += eta*(0-y).*[xnegtrain[:,t];1]

    # Clip wveceights
    # wvec(1:end-1) = max(min(wvec(1:end-1),1),0)

    # Rescale weights between zero and one (excluding bias)
    wvecmax = maximum(wvec[1:end-1])
    wvecmin = minimum(wvec[1:end-1])
    dw = wvecmax-wvecmin
    wvec = (wvec.-wvecmin)./dw

    # Error
    yerrpos = Ptrain - sum(sign.(sum([xtrain; ones(Ptrain)'].*repeat(wvec,1,Ptrain),dims=1)))
    yerrneg = abs(sum(sign.(sum([xnegtrain; ones(Ptrain)'].*repeat(wvec,1,Ptrain)))))
    E[t] = (yerrpos + yerrneg)./(2*Ptrain)
    bias[t] = wvec[end]
end

# yvalue distributions
# yvalspos = sum([xtrain; ones(Ptrain)'].*repeat(wvec,1,Ptrain),dims=1)
# yvalsneg = sum([xnegtrain; ones(Ptrain)'].*repeat(wvec,1,Ptrain),dims=1)
# ymin = minimum([minimum(yvalspos),minimum(yvalsneg)])
# ymax = maximum([maximum(yvalspos),maximum(yvalsneg)])
# yhistvec = range(ymin,stop=ymax,length=40)
# yhistpos = histogram(yvalspos[:]),yhistvec)
# yhistneg = hist(yvalsneg,yhistvec)


# Plots

# plot error vs training time
plot(E,xlabel="Time",ylabel="Error",ylim=(-0.01,1.01),label="")
savefig("perceptron_error_vs_time.png")

# image of training input patterns
heatmap(-xtrain,colorbar=false,color=:gray,grid=false,layout = grid(2,1,heights=[0.5,0.5]),title="Postive target inputs",xaxis=nothing,ylabel="Input neurons")
heatmap!(-xnegtrain,colorbar=false,color=:gray,xlabel="Time",grid=false,title="Negative target inputs",subplot=2,ylabel="Input neurons")
savefig("perceptron_training_data.png")
