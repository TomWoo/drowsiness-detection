%To detect Eyes
EyeDetect = vision.CascadeObjectDetector('EyePairBig');
%Read the input Image
I1 = imread('Tom.png');

BB=step(EyeDetect,I1);

figure,imshow(I1);
rectangle('Position',BB,'LineWidth',4,'LineStyle','-','EdgeColor','b');
title('Eyes Detection');
Eyes=imcrop(I1,BB);
figure,imshow(Eyes);
% 
I1 = imread('openEye.png');
I1 = rgb2gray(I1)
plot(1:size(I1,1) , mean(I1,2));
hold on
 I2 = imread('closedEye.png');
I2 = rgb2gray(I2)
plot(1:size(I2,1) , mean(I2,2) , 'r');