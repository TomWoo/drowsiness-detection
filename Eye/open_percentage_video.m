
clear; clc; close all

video_name = '..\Training_Data\Videos\Tom\20160220_110118.mp4';
v = VideoReader(video_name);
currentAxes = axes;

while(hasFrame(v))
    videoFrame = readFrame(v);
    img = image(videoFrame, 'Parent', currentAxes);
%     [in,Map] = frame2im(videoFrame);
    
    in = img.CData;
    out = find_eyes(in);
%     out = rgb2gray(out);
    right_eye = out(:,1:floor(end/2),:);
%     imshow(right_eye);
    show_eyes_video(right_eye);
    
    pause(0.1);
%     if(wait_key('q'))
%         break
%     end
end

clear; clc; close all
