import cv2

# Initialize variables to store mouse position
mouse_x, mouse_y = 0, 0

# Mouse callback function to update position
def mouse_callback(event, x, y, flags, param):
    global mouse_x, mouse_y
    if event == cv2.EVENT_MOUSEMOVE:
        mouse_x, mouse_y = x, y

def main():
    # Create a blank image (adjust size as needed)
    img_width, img_height = 800, 600
    img = 255 * np.ones((img_height, img_width, 3), dtype=np.uint8)

    # Create a window and set the mouse callback
    cv2.namedWindow('Mouse Position')
    cv2.setMouseCallback('Mouse Position', mouse_callback)

    while True:
        # Display the mouse position on the image
        cv2.putText(img, f"Mouse Position: ({mouse_x}, {mouse_y})", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow('Mouse Position', img)

        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
