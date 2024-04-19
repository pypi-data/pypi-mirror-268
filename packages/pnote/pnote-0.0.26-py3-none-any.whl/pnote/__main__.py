#!/usr/bin/env python

import os, argparse
from pnote.project import *
from pnote.tools import *
from pnote import __version__

def main():
    ## Parse arguments
    parser = argparse.ArgumentParser(
        prog='PNote',
        description='Note management tool',
        epilog='pnote v'+__version__)
    parser.add_argument('path', help="Path to a pnote project")
    parser.add_argument('-t', '--today', help="Open today's note file", action="store_true")
    parser.add_argument('-o', '--open', help="Open specific note file")
    subparsers = parser.add_subparsers(dest="tool", help='Tool to use')
    
    # Tools
    searcht=ToolSearch()
    searcht.add_parser(subparsers)
    tagt=ToolTag()
    tagt.add_parser(subparsers)
    exportt=ToolExport()
    exportt.add_parser(subparsers)
    admint=ToolAdmin()
    admint.add_parser(subparsers)

    # Parse arguments
    args = parser.parse_args()

    ## Load project
    project=Project(args.path)

    ## Run tool
    if args.tool == "search":
        searcht.run(project,args)
    elif args.tool == "tag":
        tagt.run(project,args)
    elif args.tool == "export":
        exportt.run(project,args)
    elif args.tool == "admin":
        admint.run(project,args)
    else:
        if args.today:
            project.opentoday()
        elif args.open:
            project.open(args.open)
