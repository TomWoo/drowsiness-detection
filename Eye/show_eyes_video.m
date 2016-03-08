function [ ] = show_eyes_video( in )
    
    I = rgb2gray(in);

    bg_thickness = 20;
    num_iterations = 300;

    mask = zeros(size(I));
    mask(bg_thickness:end-bg_thickness,1:end-3*bg_thickness) = 1;
    foreground = activecontour(I, mask, num_iterations, 'edge');
    out1 = uint8(mask).*I;
    [ x, y, w, h ] = get_bounding_box(foreground);
    out1 = insertShape(out1, 'Rectangle', [ x, y, w, h ], 'Color', 'red');
    out2 = foreground;
%     foreground = insertShape(uint8(255*foreground), 'circle', [10 30 30], 'LineWidth', 5);
    imshowpair(out1, out2, 'montage');
    
    disp(w/h);
    
end
