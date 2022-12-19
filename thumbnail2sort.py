import argparse
import os
import glob
import shutil

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--thumbnailfolder', required=True)
parser.add_argument('-m', '--movfolder', required=True)
parser.add_argument('-o', '--outfolder', required=True)
args = parser.parse_args( )

f_thu = args.thumbnailfolder
f_mov = args.movfolder
f_out = args.outfolder

files = glob.glob(f"{f_thu}\\**\\*",recursive=True)

print (files)
for file in files:
  fileglob = file.replace('[', '*').replace(']', '[]]').replace('*', '[[]')
  f_from = glob.glob(f"{f_mov}\\**\\{os.path.basename(os.path.splitext(os.path.relpath(fileglob,f_thu))[0])}",recursive=True)
  f_to = f"{f_out}{os.path.splitext(os.path.relpath(file,f_thu))[0]}"

  print("from")
  print(f_from)
  print("to")
  print(f_to)

  if len(f_from) == 1 and os.path.isfile(f_from[0]):
    os.makedirs(os.path.dirname(f_to),exist_ok=True)
    shutil.move(f_from[0],f_to)