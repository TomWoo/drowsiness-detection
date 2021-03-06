
clear; clc; close all
% s = get(0,'screensize');
% s_width = s(3);
% s_height = s(4);

path1 = '..\Training_Data\images\sapiro\';
path2 = '..\Training_Data\images\Tom\';
images = {
%     [path1 'right_1.png']
%     [path1 'right_2.png']
%     [path1 'right_3.png']
%     [path1 'right_4.png']
%     [path1 'right_5.png']
%     [path1 'right_6.png']
%     [path1 'right_7.png']
%     [path1 'right_8.png']
    [path2 'right_1.png']
    [path2 'right_2.png']
    [path2 'right_3.png']
    [path2 'right_4.png']};

for idx = 1:numel(images)
    image_name = images{idx};
    in = imread(image_name);
    
%     subplot(3,4,1);
%     imshowpair(in, I, 'montage');
%     
%     subplot(3,4,2);
%     histogram(I);
%     
%     subplot(3,4,3);
%     out1 = edge(I,'prewitt','vertical');
%     out2 = edge(I,'prewitt','horizontal');
%     imshowpair(out1, out2, 'montage');
%     
%     subplot(3,4,4);
%     out1 = edge(I,'Canny','vertical');
%     out2 = edge(I,'Canny','horizontal');
%     imshowpair(out1, out2, 'montage');
%     
%     subplot(3,4,5);
%     out1 = edge(I,'Sobel','vertical');
%     out2 = edge(I,'Sobel','horizontal');
%     imshowpair(out1, out2, 'montage');
    
%     subplot(3,4,6);
    show_eyes(in);
    
    if(wait_key('q'))
        break
    end
end

clear; clc; close all
