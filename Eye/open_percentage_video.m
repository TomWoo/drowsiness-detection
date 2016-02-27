
clear; clc; close all

video_name = '\Training_Data\Videos\Tom\20160220_110118.mp4';

path1 = '\Training_Data\images\sapiro\';
path2 = '\Training_Data\images\Tom\';
images = {
    [path1 'right_1.png']
    [path1 'right_2.png']
    [path1 'right_3.png']
    [path1 'right_4.png']
    [path1 'right_5.png']
    [path1 'right_6.png']
    [path1 'right_7.png']
    [path1 'right_8.png']
    [path2 'right_1.png']
    [path2 'right_2.png']
    [path2 'right_3.png']
    [path2 'right_4.png']};

bg_thickness = 10;

for idx = 1:numel(images)
    image_name = images{idx};
    in = imread(image_name);
    I = rgb2gray(in);
    
    subplot(3,4,1);
    imshowpair(in, I, 'montage');
    
    subplot(3,4,2);
    histogram(I);
    
    subplot(3,4,3);
    out1 = edge(I,'prewitt','vertical');
    out2 = edge(I,'prewitt','horizontal');
    imshowpair(out1, out2, 'montage');
    
    subplot(3,4,4);
    out1 = edge(I,'Canny','vertical');
    out2 = edge(I,'Canny','horizontal');
    imshowpair(out1, out2, 'montage');
    
    subplot(3,4,5);
    out1 = edge(I,'Sobel','vertical');
    out2 = edge(I,'Sobel','horizontal');
    imshowpair(out1, out2, 'montage');
    
    subplot(3,4,6);
    mask = zeros(size(I));
    mask(bg_thickness:end-bg_thickness,bg_thickness:end-bg_thickness) = 1;
    foreground = activecontour(I, mask, 300, 'edge');
    imshowpair(uint8(mask).*I, foreground, 'montage');
    
    while(waitforbuttonpress ~= 1)
        disp('Press ''q'' to quit or any other key to continue.');
    end
    p = get(gcf, 'CurrentCharacter');
    if(p=='q') % Press 'q' to exit.
        break
    end
end

clear; clc; close all
