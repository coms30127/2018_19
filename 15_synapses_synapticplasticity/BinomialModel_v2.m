%Stochastic synaptic models: Binomial release model
%This code generates nsamples from a binomial distribution

nsamples = 1000; %Number of samples
q = 1; %Postsynaptic amplitude (~ postsynaptic receptors)
Prel = 0.5; %Release probability
N = 5; %Number of release sites

responses = q.*binornd(N, Prel, nsamples,1);


figure
hist(responses, N*5, 'k')
h = findobj(gca,'Type','patch');
h.FaceColor = 'r';
xlabel('response');
ylabel('frequency');
set(gca, 'FontSize', 15);
box off;
set(gcf, 'Color', 'w');
xlim([0 N*q]);