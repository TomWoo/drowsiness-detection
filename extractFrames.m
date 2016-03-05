clear
videopath = './Training_Data/Videos/Tom/20160220_110118.mp4';
video = VideoReader(videopath);
frameRate = round(video.FrameRate);
framecount=0;
segmentnum = 1;
secondspersegment = 3;
while video.hasFrame
    f = video.readFrame;
    if(mod(framecount, frameRate*secondspersegment) == 0)
        if(segmentnum~=1)
            close(write);
        end
        write = VideoWriter(sprintf('./Training_Data/Videos/Tom/segment_%g.mp4', segmentnum));
        write.FrameRate = frameRate;
        open(write);
        segmentnum=segmentnum+1;
    end
    writeVideo(write, f);
    framecount=framecount+1;
end
close(write);
