function [ key_is_pressed ] = wait_key( keycode )

    while(waitforbuttonpress ~= 1)
        disp(['Press ''', keycode, ''' to quit or any other key to continue.']);
    end
    p = get(gcf, 'CurrentCharacter');
    if(p==keycode)
        key_is_pressed = true;
    else
        key_is_pressed = false;
    end

end

