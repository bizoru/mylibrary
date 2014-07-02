#!/usr/bin/env python

import os
import sys
global count

args = sys.argv

if len(args) < 2:
  print "Please specify folder"
  sys.exit(1)

print "Finding PDF files"
print args[1]

def recurse(path):	
	print  'Looking Here' if path == '.' else 'Looking at: '+ path
	walk_folder(path)


def walk_folder(folder):
  if os.path.isdir(os.path.abspath(folder)):
    try:
      visit_folder(folder)
    except Exception:
      return 0
    for item in os.listdir(os.path.abspath(folder)):
      if os.path.isdir(os.path.abspath(folder)):
        walk_folder(os.path.join(os.path.abspath(folder),item))

def visit_folder(folder):
  for item in os.listdir(folder):
    if analyse(item) == "[PDF File]":
	  route = str(os.path.join(folder,item))
	  print "Route: "+ route
	  command = 'mv "' + route +'" /media/steven/Backup/pdfs'
	  os.system(command)
						

def analyse(item):
  if item.split(".")[-1] == "pdf":
    return "[PDF File]"
  if ".py" in item:
    return "[Python File]"
  if ".txt" in item:
    return "[Plain text file]"
  if ".js" in item:
  	return "[Javascript file]"
  if ".jpg" in item:
  	return "[Image File]"
  if ".png" in item:
  	return "[Image File]"
  if ".css" in item:
  	return "[CSS Stylesheet File]"
  if ".php" in item:
  	return "[PHP File]"
  if ".zip" in item:
  	return "[Compressed Zip File]"
  if ".csv"	in item:
  	return "[Comma Separated Value File]"
  return "[General File]"




recurse(args[1])

