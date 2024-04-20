from pathlib import Path
from datetime import datetime
import os

class Layout:

    def __init__(self, conf, paths):
        self.conf=conf
        self.paths=paths
        self.today=datetime.today()
        self.today_backup=self.today

    def settoday(self,timestamp):
        self.today=datetime.fromtimestamp(timestamp)

    def restoretoday(self):
        self.today=self.today_backup

    def gettoday(self):
        return self.today

    def flatten(self):
        """
        List all subpath present on disk.
        """
        paths=list(Path(self.paths["files"]).rglob("*"))
        result=list()
        for p in paths:
            if os.path.isfile(p):
                result.append(p.relative_to(self.paths["files"]))
        return result

    def create(self):
        """
        Create today's note file.
        """
        file=self.todaypath()
        if not os.path.exists(file):
            open(file, 'a').close()
        return self.todaysubpath()
        
    def todayname(self):
        """
        Get today's note file name.
        """
        return self.today.strftime(self.conf["filename"])

    def todaysubdir(self):
        """
        Must be overriden by child classes
        """
        subdir=self.today.strftime(self.conf["layout"])
        if not os.path.exists(subdir):
            Path(os.path.join(self.paths["files"],subdir)).mkdir(parents=True, exist_ok=True)
        return subdir

    def todaysubpath(self):
        """
        Get the subpath of today's note file.
        """
        subdir=self.todaysubdir()
        return os.path.join(self.todaysubdir(), self.todayname())
    
    def todaypath(self):
        """
        Get the path of today's note file.
        """
        return os.path.join(self.paths["files"],self.todaysubpath())
