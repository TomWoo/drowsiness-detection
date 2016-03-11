function [ out ] = get_eye( in )
    x = cell2mat(in);
    I = rgb2gray(x);

    bg_thickness = 10;
    num_iterations = 300;

    mask = zeros(size(I));
    mask(bg_thickness:end-bg_thickness,bg_thickness:end-bg_thickness) = 1;
    foreground = activecontour(I, mask, num_iterations, 'edge');
    out1 = uint8(mask).*I;
    [ x, y, w, h ] = get_bounding_box(foreground);
    out = insertShape(out1, 'Rectangle', [ x, y, w, h ], 'Color', 'red');
%     out2 = foreground;
%     foreground = insertShape(uint8(255*foreground), 'circle', [10 30 30], 'LineWidth', 5);
%     imshowpair(out1, out2, 'montage');
    
%     disp(w/h);
end
