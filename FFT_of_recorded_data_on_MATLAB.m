%% %%%%  FFT code for a noisy data %%%%%%%%%%%
% AUTHOR: DR. RAJNISH MALLICK
% DATE: 2021 DECEMBER 31

% INPUT: SIGNAL DATA IN .XLSm FORMAT
% OUTPUT IN Hz

%%
clear all
close all
%% %%%%%
% TEST
% Fs = 1000;                    % Sampling frequency
% T = 1/Fs;                     % Sampling period
% L = 1000;                     % Length of signal
% t = (0:L-1)*T;                % Time vector
% 
% x1 = cos(2*pi*50*t);          % First row wave with wave frequency of 50
% x2 = cos(2*pi*150*t);         % Second row wave with wave frequency of 100
% x3 = cos(2*pi*300*t);         % Third row wave with wave frequency of 150
% 
% X = [x1; x2; x3];
% 
% figure(1)
% for i = 1:3
%     subplot(3,1,i)
%     plot(t(1:100),X(i,1:100))
%     title(['Row ',num2str(i),' in the Time Domain'])
% end

% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% %% For algorithm performance purposes, fft allows you to pad the input with trailing zeros. In this case, pad each row of X with zeros so that the length of each row is the next higher power of 2 from the current length. Define the new length using the nextpow2 function.
% n = 2^nextpow2(L);
% 
% %Specify the dim argument to use fft along the rows of X, that is, for each signal.
% dim = 2;
% 
% %Compute the Fourier transform of the signals.
% Y = fft(X,n);
% 
% % Calculate the double-sided spectrum and single-sided spectrum of each signal.
% P2 = abs(Y/L);
% P1 = P2(:,1:n/2+1);
% P1(:,2:end-1) = 2*P1(:,2:end-1);
% 
% 
% % In the frequency domain, plot the single-sided amplitude spectrum for each row in a single figure.
% for i=1:3
%     subplot(3,1,i)
%     plot(0:(Fs/n):(Fs/2-Fs/n),P1(i,1:n/2))
%     title(['Row ',num2str(i),' in the Frequency Domain'])
% end
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%55

%%
data = readtable('FINAL_TIME_AXIS.xlsm');
subdata = data(1:1000,7:11);
size(subdata)
A = table2array(subdata);
t = A(127:160,1);
y1 = A(127:160,2);


figure(1)
subplot(3,1,1)
% t = A(127:160,1);
% y1 = A(127:160,2);
t = A(:,1);
y1 = A(:,2);
plot(t,y1)
xlabel('Time (milli seconds)')
ylabel('Amplitude')
%xlim([0 t(end)])
grid on;

% [d,s] = xlsread('1.5V.csv');
t = A(:,1)*1E-3;                                        % Convert To ‘seconds’ From ‘milliseconds’
v = A(:,2);                                             % Voltage (?)
L = length(t);
Ts = mean(diff(t));                                     % Sampling Interval (sec)
Fs = 1/Ts;                                              % Sampling Frequency
Fn = Fs/2;                                              % Nyquist Frequency
vc = v - mean(v);                                       % Subtract Mean (‘0 Hz’) Component
FTv = fft(vc)/L;                                        % Fourier Transform
Fv = linspace(0, 1, fix(L/2)+1)*Fn;                     % Frequency Vector (Hz)
Iv = 1:length(Fv);                                      % Index Vector

figure(1)

subplot(3,1,2)
plot(t,vc)
xlabel('Time (milli seconds)')
ylabel('Amplitude')
%xlim([0 t(end)])
grid on;


subplot(3,1,3)
plot(Fv, abs(FTv(Iv))*2)
grid
xlabel('Frequency (Hz)')
ylabel('Amplitude')




