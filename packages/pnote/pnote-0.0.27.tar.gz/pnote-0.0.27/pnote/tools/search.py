from pnote.tools.tool import Tool
import argparse, os

class ToolSearch(Tool):

    def add_parser(self,subparsers):
        p = subparsers.add_parser("search", description="Perform search operation on your notes")
        p.add_argument("-g", "--grep", help="Grep an expression")
        p.add_argument("-n", "--name", help="Search for a note path")
        p.add_argument("-i", "--ignore-case", help="Ignore case during search", action='store_true')
        p.add_argument("-t", "--tag", help="Search for a note with a tag")
        p.add_argument("-c", "--content-only", help="Show content only", action='store_true')
        p.add_argument("-s", "--subpath-only", help="Show file subpath only", action='store_true')
        p.add_argument("--last-created", help="Get last n created note files")
        p.add_argument("--last-added", help="Get last n added note files")

    def catsubpath(self,project,subpath):
        with open(project.getpath(subpath),"r") as fp:
            for line in fp:
                print(line,end="")

    def catsubpaths(self, project, subpaths, content_only=False, subpath_only=False):
        first=True
        for subpath in subpaths:
            if subpath_only:
                print(subpath)
                continue
            if not content_only:
                if not first:
                    print()
                    self.printsubpath(subpath)
            self.catsubpath(project,subpath)
            first=False

    def run(self, project, args):
        ignore_case=True if args.ignore_case else False
        content_only=True if args.content_only else False
        subpath_only=True if args.subpath_only else False

        if content_only and subpath_only:
            print("content and file-path options cannot be used at the same time")
            exit(1)
        if args.grep:
            first=True
            for entry in project.grep(args.grep, ignore_case):
                subpath=entry[0]
                if subpath_only:
                    print(subpath)
                    continue
                if not content_only:
                    if not first:
                        print()
                    self.printsubpath(subpath)
                for line in entry[1]:
                    ln=line[0]
                    content=line[1]
                    if content_only:
                        print(content)
                    else:
                        print("L{}: {}".format(ln,content))
                first=False

        elif args.tag:
            self.catsubpaths(project, project.searchtag(args.tag),content_only,subpath_only)

        elif args.last_created:
            subpaths=project.listlastcreated()
            self.catsubpaths(project, subpaths[-abs(int(args.last_created)):],content_only,subpath_only)

        elif args.last_added:
            subpaths=project.listlastadded()
            self.catsubpaths(project, subpaths[-abs(int(args.last_added)):],content_only,subpath_only)

        else:
            if args.name:
                self.catsubpaths(project, project.find(args.name,ignore_case),content_only,subpath_only)
            else:
                self.catsubpaths(project, project.find(None),content_only,subpath_only)

