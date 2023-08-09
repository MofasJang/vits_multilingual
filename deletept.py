import glob
import os
pt_files = glob.glob("../dataset/aishell3/*/*.spec.pt")
for pt_file in pt_files:
    os.remove(pt_file)