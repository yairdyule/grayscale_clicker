import pyautogui as pgi


x, y = pgi.position()
to_return_to = {'x':x, 'y':y} #location of the mouse before program execution
accessibility_in_menu = {"x":2089, "y":15} #location of the accessibility icon in the menu
color_filter_in_accessibility = {'x':2100, 'y':210} #location of grayscale within that icon


#mouse to the icon, click it to open accessibility shortcut
pgi.moveTo(accessibility_in_menu["x"], accessibility_in_menu["y"], duration=.00001, 
tween=pgi.easeInOutQuad)
pgi.click()

#inside acc. shortcut, click the grayscale option
pgi.moveTo(color_filter_in_accessibility['x'], color_filter_in_accessibility['y'], duration=.00001, tween=pgi.easeInOutQuad)
pgi.click()

#return mouse to its original location
pgi.moveTo(to_return_to['x'], to_return_to['y'], duration=.001, tween=pgi.easeInOutQuad)

#TODO: another script to execute this one at a certain time of day
#ex: sunset occurs, gs_clicker is executed automatically