% PEAKS GENERATION PROGRAM OF ANY SIGNAL DATA WITH ITS LOCATIONS, PEAKS AND WIDTHS IN DESCENDING ORDER

%% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% AUTHOR: DR. RAJNISH MALLICK
% DATE: 2021 DECEMBER 16

% INPUT: SIGNAL DATA IN .XLSX FORMAT
% OUTPUT IN AN ARRAY NAMED LOCS
%% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clear all
close all
clf
%%%%%%%

data = readtable('2021_12_16_Time period of recorded signal.xlsx');
subdata = data(:,1:2);
size(subdata)

ysubdata = data(:,2);
A = table2array(ysubdata);

[pks,locs,w,p] = findpeaks(A,'NPeaks',5,'SortStr','descend')

%% Plotting of Signal peaks
figure(1)
subplot(3,1,1)
plot(A)

subplot(3,1,2)
findpeaks(A)

subplot(3,1,3)
findpeaks(A,'NPeaks',5,'SortStr','descend')


%% Plotting of Signal
figure(2)
findpeaks(A,'NPeaks',5,'SortStr','descend')



%results : Peaks in descending order
%88
%159
%105
%123
%140




