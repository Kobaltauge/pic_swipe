# pic_swipe
Picture sort Tinder style

Program let you select a folder with all the pictures to sort. It shows the picture in a viewer window. With the cursor key the picture will be moved in two folders. One to delete the other to store for further sort.


Requirements

tkinter
opencv


Usage

With a file picker choose a picture in the folder. The folder will be processed.
Cursor keys left and right jump from one picture to the next.
Cursor key up moves tht picture in the "delete" folder.
Cursor key down move the picture in the "sort" folder.


Known issues
- The output folders a hardcoded
- The moved picture are still in the "list". Error if you retry to view them.
- End of list is not catched
- No reload function for the folder
- Viewer is hard coded to 800x600. Picture ratio will be ignored
