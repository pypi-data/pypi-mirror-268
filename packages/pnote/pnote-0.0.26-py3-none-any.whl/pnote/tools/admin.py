from pnote.tools.tool import Tool
import argparse
from datetime import datetime

class ToolAdmin(Tool):

    def add_parser(self,subparsers):
        self.p = subparsers.add_parser("admin", description="Manage your notes tags")
        self.p.add_argument("--fix-dry", help="fix new and deleted note files (DRY RUN)", action='store_true')
        self.p.add_argument("--fix", help="fix new and delete note files", action='store_true')
        self.p.add_argument("--import", help="Import file(s) to notes", nargs="+", dest="imports")
        self.p.add_argument("--timestamp", help="Timestamp to use for file(s) import")
        self.p.add_argument("--file-infos", help="Get note file(s) infos", action='store_true')
        self.p.add_argument("--subpath", help="")
        self.p.add_argument("-s", "--subpaths", help="Subpath to use for file(s) infos", nargs="+")

    def run(self, project, args):
        if args.fix_dry:
            project.fix(True)
        elif args.fix:
            project.fix(False)
        elif args.imports:
            if args.timestamp:
                for f in args.imports:
                    project.addfile(f,int(args.timestamp))
            else:
                for f in args.imports:
                    project.addfile(f)
        elif args.file_infos:
            if args.subpaths:
                subpaths=args.subpaths
            else:
                subpaths=project.find(None)
            first=True
            for subpath in subpaths:
                if not first:
                    print()
                print("=> "+subpath)
                ts_created=project.getfileinfo(subpath,"created")
                ts_added=project.getfileinfo(subpath,"added")
                print("Created on: "+str(datetime.fromtimestamp(int(ts_created))))
                print("Added on: "+str(datetime.fromtimestamp(int(ts_added))))
                print("Added with host: "+str(project.getfileinfo(subpath,"hostname")))
                print("Added host infos: "+str(project.getfileinfo(subpath,"platform")))
                print("Tags: "+str(project.listtags(subpath)))
                first=False
        else:
            self.p.print_help()
