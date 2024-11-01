# HS-Share-Usage
 Scripts to gather detailed information about a Hammerspace share.
 + hs-share-usage.py - Prompts for drive and can total the share or individual top level directories.
 + hs_all_dir_usage.py - Prompts for drive letter then walks the directory structure and lists file count and size for each directory. Saves output to a CSV file.
  - Future
    - Clean up output from the 'hs sum' command. It currently is dumping into a single cell since it looks like: {6.942 KFILES, 123.1 MBYTES}
