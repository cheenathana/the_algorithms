from configparser import ConfigParser
import sys
import csv
import argparse

# Setting up CLI Parser
parser = argparse.ArgumentParser()
parser.add_argument('inifile', type=str)
parser.add_argument('csvfile', type=str)
parser.add_argument('--collapsed', action='store_true')
args = parser.parse_args()

# Setting up inifile parser
inip = ConfigParser()
inip.read(args.inifile)

with open(args.csvfile, 'wt') as f:
    w = csv.writer(f)
    isheaderwritten = True

    for section in inip.sections():
        if args.collapsed:
            if isheaderwritten:
                w.writerow(['header'] + list(inip[section].keys()))
                isheaderwritten = False
                
            w.writerow([section] + list(inip[section].values()))
            continue
    
        for k,v in inip.items(section):
            w.writerow((section, k, v))
