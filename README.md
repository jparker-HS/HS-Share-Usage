# HS-Share-Usage
 Scripts to gather detailed information about a Hammerspace share.
 + hs-share-usage.py - Prompts for drive and can total the share or individual top level directories.
 + hs_all_dir_usage.py - Prompts for drive letter then walks the directory structure and lists file count and size for each directory. Saves output to a CSV file.
 + hs-dir-walk.py - Python script to gather directory stats, specifically dir size and num of files then format the output for Prometheus metrics use.
  - Future
    - Clean up output from the 'hs sum' command. It currently is dumping into a single cell since it looks like: {6.942 KFILES, 123.1 MBYTES}
 + HSTK-dir-report.py - No input required script that generates directory usage reports in CSV format for Hammerspace shares. 