function [ x, y, h, w ] = get_bounding_box( BW ) % TODO: bugfix (h and w are switched)

% BW = uint8(BW);
% BW_size = size(BW);
% height = BW_size(1);
% width = BW_size(2);
% 
% BW1 = BW;
% % BW1 = BW1(:,:);
% % idx1_first = find(BW1, 1, 'first');
% % idx1_last = find(BW1, 1, 'last');
% % y = floor(idx1_first/width);
% % y_last = floor(idx1_last/width);
% [x1_first,y1_first] = find(BW1, 1, 'first');
% [x1_last,y1_last] = find(BW1, 1, 'last');
% y = y1_first;
% y_last = y1_last;
% h = y_last - y;
% 
% BW2 = BW';
% % BW2 = BW2(:,:);
% % idx2_first = find(BW2, 1, 'first');
% % idx2_last = find(BW2, 1, 'last');
% % x = floor(idx2_first/height);
% % x_last = floor(idx2_last/height);
% [x2_first,y2_first] = find(BW2, 1, 'first');
% [x2_last,y2_last] = find(BW2, 1, 'last');
% x = y2_first;
% x_last = y2_last;
% w = x_last - x;
% 
% % TODO: bugfix (hacky translations of bounding box)
% x = x+((x+x_last)/2-x);
% y = y-((y+y_last)/2-y)/4;

stats = regionprops(BW,'BoundingBox');
BB = stats.BoundingBox;
x = BB(1);
y = BB(2);
h = BB(3);
w = BB(4);

end
