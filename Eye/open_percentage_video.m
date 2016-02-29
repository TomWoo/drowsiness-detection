
clear; clc; close all

video_name = '..\Training_Data\Videos\Tom\20160220_110118.mp4';
v = VideoReader(video_name);
currentAxes = axes;

while(hasFrame(v))
    videoFrame = readFrame(v);
    img = image(videoFrame, 'Parent', currentAxes);
%     [in,Map] = frame2im(videoFrame);
    
    in = img.CData;
    show_eyes(in);
    
    if(wait_key('q'))
        break
    end
end

clear; clc; close all
