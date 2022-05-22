"""
# PART 1
import shutil
import os
# Set where the source of the files are
source = "/Users/vinhpham/Documents/GitHub/Python-Projects/python-learning/step315_file_transfer_assignment_folder_a/"
# Set the destination path to folder_b
destination = "/Users/vinhpham/Documents/GitHub/Python-Projects/python-learning/step315_file_transfer_assignment_folder_b/"
files = os.listdir(source)
for i in files:
    # We are saying move the files represented by 'i' to their new destination
    shutil.move(source+i, destination)
"""

# PART 2 & 3
import datetime, glob, os, shutil, time, tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
    

def browse_folder(self):
    # Deletes any text currently in the tkinter textbox widget.
    self.delete(1.0, END)
    
    # Allow user to select a directory.
    folder_path = filedialog.askdirectory(initialdir="/Users/vinhpham/Documents/GitHub/Python-Projects/python-learning/", mustexist=True)
    folder_path = folder_path + "/"
    print(folder_path)
    
    # Inserts selected directory into its repective (self) textbox contents
    self.insert(END, folder_path)


def copy_files(self):
    # Gets the text (from the tkinter textboxes) that was populated from the browse_folder() function.
    # In this case, the texts are the source and destination folder directories.
    src = self.txt_browse_source.get("1.0", "end-2c")
    dst = self.txt_browse_destin.get("1.0", "end-2c")

    if src == "" or dst == "":
        tk.messagebox.showinfo("Unable to copy due to an invalid directory", "Directories cannot be '/'. Please choose a valid directory.")
    else:
        # These sets the time variables required in order to determine the current time "now" and the time 24-hours ago "before",
        # which is crucial to determine which files in the source directory were modified within the last 24-hours, and which were not.
        # The For Loop below cycles through the files in the source directory.
        # With the time functions, it determines the files which were modified within the last 24-hours,
        # and copies them to the destination directory.
        seconds_in_day = 24 * 60 * 60
        now = time.time()
        before = now - seconds_in_day
            
        def last_mod_time(fname):
            return os.path.getmtime(fname)

        for fname in os.listdir(src):
            src_fname = os.path.join(src, fname)
            if last_mod_time(src_fname) > before and fname.endswith(".txt"):
                dst_fname = os.path.join(dst, fname)
                if os.path.exists(dst_fname):
                    print('{} already exists in the directory "{}" and will not be copied.'.format(fname, dst))
                else:
                    shutil.copy2(src_fname, dst_fname)
                    print('Copied: ' + fname)
                    (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(src_fname)
                    mdate = "%s" % time.ctime(mtime)
                    print('{} was last modified on {} and has been copied from the directory "{}" to the directory "{}"'.format(fname, mdate, src, dst))


def load_gui(self):
    # Widget settings
    self.master.title("Copy text files modified within the last 24 hours")
    
    self.lbl_instr_0 = tk.Label(self.master, text='Instructions:')
    self.lbl_instr_1 = tk.Label(self.master, text='(1) Click the "Browse.." buttons to choose your source and destination folders for the copy')
    self.lbl_instr_2 = tk.Label(self.master, text='(2) Once your folders are chosen, click the "Copy Files" button to initate the copy')

    self.btn_browse_source = tk.Button(self.master, text='Browse for source folder..', command=lambda: browse_folder(self.txt_browse_source))
    self.btn_browse_destin = tk.Button(self.master, text='Browse for destination folder..', command=lambda: browse_folder(self.txt_browse_destin))
    self.btn_copy_files = tk.Button(self.master, text='Copy Files', command=lambda: copy_files(self))

    self.txt_browse_source = tk.Text(self.master, width=35, height=1, bg="white")
    self.txt_browse_destin = tk.Text(self.master, width=35, height=1, bg="white")

    # Widget placements on grid
    self.lbl_instr_0.grid(row=0, column=0, rowspan=1, columnspan=3, padx=(5,5), pady=(5,5), sticky=N+E+W)
    self.lbl_instr_1.grid(row=1, column=0, rowspan=1, columnspan=3, padx=(5,5), pady=(5,5), sticky=W)
    self.lbl_instr_2.grid(row=2, column=0, rowspan=1, columnspan=3, padx=(5,5), pady=(5,5), sticky=W)

    self.btn_browse_source.grid(row=3, column=0, padx=(5,5), pady=(5,5), sticky=W)
    self.btn_browse_destin.grid(row=4, column=0, padx=(5,5), pady=(5,5), sticky=W)
    self.btn_copy_files.grid(row=5, column=0, padx=(5,5), pady=(5,5), sticky=W)

    self.txt_browse_source.grid(row=3, column=1, padx=(5,5), pady=(5,5), sticky=W)
    self.txt_browse_destin.grid(row=4, column=1, padx=(5,5), pady=(5,5), sticky=W)


# The window class is not standard, we create a Window. This class in itself is pretty basic.
class ParentWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        load_gui(self)



if __name__ == '__main__':
    # Start tk and create a window.
    root = tk.Tk()
    app = ParentWindow(root)
    # Show window
    root.mainloop()
