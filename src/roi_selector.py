import cv2
from copy import deepcopy

# Initialize global variables
list_of_rectangles = []
confirmed_rectangles = []
drawing = False
undo_stack = []
redo_stack = []
current_rectangle = []  # Moved this to global scope

def draw_rectangle(event, x, y, flags, params):
    global drawing, undo_stack, redo_stack, current_rectangle

    img, _ = params

    if event == cv2.EVENT_LBUTTONDOWN:
        undo_stack.append((deepcopy(list_of_rectangles), deepcopy(confirmed_rectangles)))  
        redo_stack.clear()
        drawing = True
        list_of_rectangles.append([(x, y), (x, y)])  # Initialize with same corner
        current_rectangle = list_of_rectangles[-1]

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        current_rectangle[1] = (x, y)
        update_image(img)

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            current_rectangle[1] = (x, y)
            update_image(img)

def update_image(img):
    temp_img = img.copy()
    for rectangle in list_of_rectangles:
        if len(rectangle) == 2:
            cv2.rectangle(temp_img, rectangle[0], rectangle[1], (0, 255, 0), 2)
    for rectangle in confirmed_rectangles:
        if len(rectangle) == 2:
            cv2.rectangle(temp_img, rectangle[0], rectangle[1], (0, 0, 255), 2)
    cv2.imshow('ROI Selector', temp_img)


def get_rois(images_np):
    global list_of_rectangles, confirmed_rectangles, undo_stack, redo_stack
    drawing = False

    rois = []

    for img in images_np:
        list_of_rectangles.clear()
        confirmed_rectangles.clear()
        undo_stack.clear()
        redo_stack.clear()

        cv2.namedWindow('ROI Selector', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('ROI Selector', img.shape[1], img.shape[0])
        cv2.imshow('ROI Selector', img)
        cv2.setMouseCallback('ROI Selector', draw_rectangle, [img, confirmed_rectangles])

        last_key = None

        while True:
            key = cv2.waitKey(1) & 0xFF

            if key != 255 and key != last_key:
                print(f"Key pressed: {key}, Current ROIs: {list_of_rectangles}")
                last_key = key

            if key == ord("c"):
                break

            elif key == ord("n"):
                undo_stack.append((deepcopy(list_of_rectangles), deepcopy(confirmed_rectangles)))
                redo_stack.clear()
    
                for rectangle in list_of_rectangles:
                    label = input(f"Please enter a label for rectangle {rectangle}: ")
                    rectangle.append(label)
    
                confirmed_rectangles.extend(deepcopy(list_of_rectangles))
                list_of_rectangles.clear()
                update_image(img)


            elif key == 26:  # Ctrl+Z
                if undo_stack:
                    redo_stack.append((deepcopy(list_of_rectangles), deepcopy(confirmed_rectangles)))
                    list_of_rectangles, confirmed_rectangles = undo_stack.pop()
                    update_image(img)
                else:
                    print("No actions to undo.")

            elif key == 25:  # Ctrl+Y
                if redo_stack:
                    undo_stack.append((deepcopy(list_of_rectangles), deepcopy(confirmed_rectangles)))
                    list_of_rectangles, confirmed_rectangles = redo_stack.pop()
                    update_image(img)
            
            elif key == ord("q"):
                print("Exiting program.")
                exit()


        rois.append(confirmed_rectangles.copy())
        cv2.destroyAllWindows()

    return rois
