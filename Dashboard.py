#
# FILENAME.
#       Dashboard.py - Dashboard Application.
#
# FUNCTIONAL DESCRIPTION.
#       The app collects important information in dashboard. 
#
# NOTICE.
#       Author: visualge@gmail.com (Count Chu)
#       Created on 2019/7/20
#

#
# Include standard packages.
#

import argparse
import logging
import pdb
import os
import json

#
# Include specific packages.
#

import ssl
import pandas
import datetime
import urllib.request
import Stock

#
# Build argument parser and return it.
#
    
def buildArgParser():

    parser = argparse.ArgumentParser(
                description='Build ...')
                
    #
    # Standard arguments
    #
                
    parser.add_argument(
            "-v", 
            dest="verbose", 
            action='store_true',    
            help="Verbose log") 
            
    parser.add_argument(
            '--log',
            dest='logFn',
            help='A name of a log file.')             
            
    #
    # Anonymous arguments.
    #
               
    '''
    parser.add_argument(
            'file',
            help='A file') 
    '''
       
    #
    # Specific arguments
    #     
 
    '''
    parser.add_argument(
            '-d',
            dest='dir',
            required=True,
            help='A directory that contains files')     
    '''
       
    parser.add_argument(
            '--images',
            dest='imagesDir',
            help='A directory that contains images') 
            
    parser.add_argument(
            "-start", 
            type=int,
            default=4,
            dest="start", 
            help="Input start")              
            
    parser.add_argument(
            "-steps", 
            type=int,
            default=12,
            dest="steps", 
            help="Input steps")     

    parser.add_argument(
            "-a", 
            dest="alg", 
            default='ncc',
            help="Input ncc or gauss")            

    parser.add_argument(
            "--step", 
            dest="step", 
            action='store_true',    
            help="Enable step. Press '>.' for next step and '<,' for previous step")            
            
    return parser
    
def readConfig(jsonFn):   
    if not os.path.exists(jsonFn):
        return None

    f = open(jsonFn, 'r')
    lines = f.readlines()
    jsonStr = ''.join(lines)
    jsonObj = json.loads(jsonStr)
    f.close()
    
    return jsonObj   
    
def main():    

    #
    # Parse arguments
    #
    
    args = buildArgParser().parse_args()
    
    #
    # Enable log if -v
    #
    
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG, format='%(message)s')
    logging.info(args)
    
    #
    # Check arguments.
    #
    
    #
    # Open a log file if --log
    #
    
    if args.logFn != None:
        logF = open(args.logFn, 'w')
        
    #
    # Read config.
    #
    
    jsonFn = 'Dashboard.json'
    jsonObj = readConfig(jsonFn)
    
    #
    # Override args
    #
    
    if jsonObj != None:
        if 'dataSet' in jsonObj and 'imagesDir' in jsonObj['dataSet']:
            args.imagesDir = jsonObj['dataSet']['imagesDir']
            print('Override imagesDir = %s' % args.imagesDir)       

    #
    # Read file names if -d.
    #

    fileNames = []
    #pdb.set_trace()
    if 'dir' in args and args.dir != None:
        for fn in os.listdir(args.dir):
            path = os.path.join(args.dir, fn)
            if not os.path.isdir(path):
                fileNames.append(path)            
    
    #pdb.set_trace()
    
    #
    # Here is core function.
    #
    
    for stockId in jsonObj['twStockIdList']:
        info = Stock.getCurrentTwStock(stockId)
        print(info)
    
    #
    # Close the log file if --log
    #
    
    if args.logFn != None:
        logF.close()

if __name__ == '__main__':

    main()