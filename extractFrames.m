clear
videopath = './Training_Data/Videos/Tom/20160220_110118.mp4';
video = VideoReader(videopath);
frameRate = round(video.FrameRate);
i=0;
num = 1;
while video.hasFrame
    f = video.readFrame;
    if(mod(i, frameRate*3) == 0)
        if(num~=1)
            close(write);
        end
        write = VideoWriter(sprintf('./Training_Data/Videos/Tom/segment_%g.mp4', num));
        write.FrameRate = frameRate;
        open(write);
        num=num+1;
    end
    writeVideo(write, f);
    i=i+1;
end
close(write);
