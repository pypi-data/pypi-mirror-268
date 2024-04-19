from pnote.tools.tool import Tool
import argparse, os, sys, json
from datetime import datetime

class ToolExport(Tool):

    def __init__(self):
        self.template_file=None
        self.date_format=None

    def add_parser(self,subparsers):
        p = subparsers.add_parser("export", description="Export notes from subpaths in stdin")
        p.add_argument("--template", help="Export notes following a template file")
        p.add_argument("--date-format", help="Specify a format use by date in the output")
        p.add_argument("--json", help="Export notes in json format", action='store_true')

    def get_subpath_data(self, project, subpath):
        data=None
        with open(project.getpath(subpath),"r") as noteFile:
            data={
                "content":noteFile.read(),
                "created":project.getfileinfo(subpath,"created"),
                "added":project.getfileinfo(subpath,"added"),
                "id":project.getfileinfo(subpath,"id"),
                "hostname":project.getfileinfo(subpath,"hostname"),
                "platform":project.getfileinfo(subpath,"platform"),
                "tags":project.listtags(subpath),
                "subpath":subpath
            }
            if self.date_format is not None:
                data["created"]=datetime.fromtimestamp(data["created"]).strftime(self.date_format)
                data["added"]=datetime.fromtimestamp(data["added"]).strftime(self.date_format)
        return data

    def run(self, project, args):
        if args.date_format:
            self.date_format=args.date_format

        if args.template:
            if not os.path.exists(args.template):
                print("Template file not found: {}".format(args.template))
                exit(1)
            self.template_file=args.template
            for line in sys.stdin:
                subpath=line.rstrip()
                with open(self.template_file,"r") as tplFile:
                    variables=self.get_subpath_data(project,subpath)
                    for line in tplFile:
                        print(line.format(**variables),end="")
        elif args.json:
            print("[")
            first=True
            for line in sys.stdin:
                subpath=line.rstrip()
                if not first:
                    print(",",end="")
                print(json.dumps(self.get_subpath_data(project,subpath),indent=4))
                first=False
            print("]")

        