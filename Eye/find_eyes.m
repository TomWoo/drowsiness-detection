function out = find_eyes(in)

%To detect Eyes
EyeDetect = vision.CascadeObjectDetector('EyePairBig');
%Read the input Image
I1 = in;

BB=step(EyeDetect,I1);

% figure,imshow(I1);
rectangle('Position',BB,'LineWidth',4,'LineStyle','-','EdgeColor','b');
title('Eyes Detection');
Eyes=imcrop(I1,BB);
% figure,imshow(Eyes);
out = Eyes;

end
