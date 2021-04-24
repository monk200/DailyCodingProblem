"""
Daily Coding Problem #17

Suppose we represent our file system by a string in the following manner:
The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:
dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.
The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:
dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty
second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.
We are interested in finding the longest (number of characters) absolute path to a file within our file system. For
example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length
is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to a file
in the abstracted file system. If there is no file in the system, return 0.

Note:
The name of a file contains at least a period and an extension.
The name of a directory or sub-directory will not contain a period.
"""


# I feel like there's a recursive solution to this that would be cleaner
def longestDir(dir):
    if "." not in dir:      # no file extensions exist
        return 0

    lines = dir.split("\\n")        # split dir into a list where each element is a folder or file
    currDir = []
    t_index = 0     # keeps track of the \t's to know what is inside other folders
    longest = ""        # contains current longest directory

    index = 0
    while index < len(lines):
        line = lines[index]
        if index == 0:      # always append "dir"
            currDir.append(line)
        elif "." in line:     # reached a file
            currDir.append("/" + line[t_index+2:])      # appending in this form removes the \t's and adds the / where necessary
            # creates an absolute path to a file
            currCount = ""
            for word in currDir:        # create directory path
                currCount += word
            if len(currCount) >= len(longest):       # checks if length of this path is longest so far
                longest = currCount
            # backtrack
            currDir.pop()
        elif line[t_index: t_index+2] == "\\t":        # in one tab farther than the last line indicating a subfolder/subfile
            currDir.append("/" + line[t_index+2:])      # appending in this form removes the \t's and adds the / where necessary
            t_index += 2
        else:       # backtrack
            currDir.pop()
            t_index -= 2
            index -= 1
        index += 1

    return longest


# preceding the directory with an r is neccessary because the escape character is used
assert longestDir(r"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext") == "dir/subdir2/subsubdir2/file2.ext", "Should be dir/subdir2/subsubdir2/file2.ext"     # checks the given case
assert longestDir(r"dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext") == "dir/subdir2/file.ext", "Should be dir/subdir2/file.ext"     # checks the given case

