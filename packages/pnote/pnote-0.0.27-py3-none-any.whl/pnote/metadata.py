import os, json, platform, socket, sqlite3
from datetime import datetime
from pathlib import Path

class Metadata:

    def __init__(self, paths):
        self.paths=paths
        self.today=datetime.today()

        ## Create folders
        self.paths["metadata"]=os.path.join(self.paths["root"], "metadata.db")

        ## Init database
        self.con=sqlite3.connect(self.paths["metadata"])
        cur=self.con.cursor()
        tables=cur.execute("""SELECT name FROM sqlite_master WHERE type='table' AND name='files'; """).fetchall()

        if len(tables) == 0:
            cur.execute("CREATE TABLE files(id INTEGER PRIMARY KEY AUTOINCREMENT, subpath TEXT UNIQUE, created REAL, added REAL, hostname TEXT, platform TEXT);")
            self.con.commit()
            cur.execute("CREATE TABLE tags(id INTEGER, name TEXT, FOREIGN KEY(id) REFERENCES files(id));")
            self.con.commit()
            cur.execute("CREATE TABLE cache(name TEXT PRIMARY KEY, value TEXT);")
            self.con.commit()


    def create(self, subpath, created):
        """
        Create a new note file entry.
        """
        cur=self.con.cursor()
        cur.execute("""INSERT INTO files(subpath,created,added,hostname,platform) values('{}','{}','{}','{}','{}')""".format(
            subpath,
            created.timestamp(),
            datetime.today().timestamp(),
            socket.gethostname(),
            platform.platform()
        ))
        self.con.commit()

    def getfileinfo(self, subpath, name):
        """
        Get associated info (name argument e.g hostname) with a subpath.
        """
        subpath_id=self.subpathid(subpath, True)
        cur=self.con.cursor()
        cur.execute('SELECT {} FROM files WHERE id="{}"'.format(name,subpath_id))
        return list(cur.fetchone())[0]

    def setcache(self, name, value):
        """
        Set the value of a cache entry.
        """
        cur=self.con.cursor()
        cur.execute('SELECT value FROM cache WHERE name="{}"'.format(name))
        if cur.fetchone() is None:
            cur.execute('INSERT INTO cache values("{}","{}")'.format(name,value))
        else:
            cur.execute('UPDATE cache SET value="{}" WHERE name="{}"'.format(value,name))
        self.con.commit()

    def getcache(self,name):
        """
        Get the value of a cache entry.
        """
        cur=self.con.cursor()
        cur.execute('SELECT value FROM cache WHERE name="{}"'.format(name))
        result=cur.fetchone()
        if result is None:
            return None
        return result[0]

    def subpathid(self, subpath, required=False):
        """
        Get the id (sqlite id) of a subpath. If required=True then abort if subpath not found. 
        """
        cur=self.con.cursor()
        cur.execute('SELECT id FROM files WHERE subpath="{}"'.format(subpath))
        result=cur.fetchone()
        if result is not None:
            return list(result)[0]
        if required:
            print("Subpath not found: "+subpath)
            exit(1)
        return None
    
    def delete(self,subpath, ignore_error=False):
        """
        Delete subpath and its associated tags from the metadata.
        """
        cur=self.con.cursor()
        subpath_id=None
        if ignore_error:
            subpath_id=self.subpathid(subpath, False)
        else:
            subpath_id=self.subpathid(subpath, True)
        if subpath_id is None:
            return
        cur.execute('DELETE FROM tags WHERE id={}'.format(subpath_id))
        cur.execute('DELETE FROM files WHERE id={}'.format(subpath_id))
        self.con.commit()

    def addtag(self, subpath, tag):
        """
        Attach a tag to a specific subpath.
        """
        taglist=self.listtags(subpath)
        if tag not in taglist:
            cur=self.con.cursor()
            subpath_id=self.subpathid(subpath, True)
            cur.execute('INSERT INTO tags(id, name) VALUES({},"{}")'.format(subpath_id,tag))
            self.con.commit()
        else:
            print("{} as already be tagged with {}".format(subpath,tag))

    def deletetag(self, subpath, tag):
        """
        Delete a tag attached to a specific subpath.
        """
        cur=self.con.cursor()
        subpath_id=self.subpathid(subpath, True)
        cur.execute('DELETE FROM tags WHERE id={} AND name="{}"'.format(subpath_id,tag))
        self.con.commit()

    def obliteratetag(self, tag):
        """
        Remove all occurences of a tag from the database.
        """
        cur=self.con.cursor()
        cur.execute('DELETE FROM tags WHERE name="{}"'.format(tag))
        self.con.commit()

    def searchtag(self,tag):
        """
        Get all subpaths associated with a specific tag.
        """
        cur=self.con.cursor()
        ids=[i[0] for i in cur.execute('SELECT id FROM tags WHERE name="{}"'.format(tag)) ]
        subpaths=[cur.execute('SELECT subpath FROM files WHERE id={}'.format(i)).fetchone()[0] for i in ids]
        return subpaths

    def listtags(self, subpath=None):
        """
        List either all tags (subpath is None), or the ones associated with a subpath.
        """
        cur=self.con.cursor()
        if subpath is not None:
            subpath_id=self.subpathid(subpath, True)
            tags=[i[0] for i in cur.execute('SELECT DISTINCT name FROM tags WHERE id={}'.format(subpath_id)) ]
        else:
            tags=[i[0] for i in cur.execute('SELECT DISTINCT name FROM tags') ]
        return tags

    def fix_deleted(self, dry=True):
        """
        Search for files deleted by the user and update database accordingly.
        """
        cur=self.con.cursor()
        for result in cur.execute("SELECT subpath FROM files"):
            subpath=result[0]
            path=os.path.join(self.paths["files"], subpath)
            if not os.path.exists(path):
                if dry:
                    print("Deletion detected => " + subpath)
                else:
                    print("Fixing file deletion => " + subpath)
                    self.delete(subpath)

    def fix_new(self, layout, dry=True):
        """
        Search for new files added by the user and update the database accordingly.
        """
        cur=self.con.cursor()
        for subpath in layout.flatten():
            result=cur.execute('SELECT * from files where subpath="{}"'.format(subpath))
            if len(result.fetchall()) <= 0 :
                if dry:
                    print("New file detected => "+str(subpath))
                else:
                    print("Fixing new file => "+str(subpath))
                    self.create(subpath,layout.gettoday())

    def flatten_ordered(self, desc=False, ordby="created"):
        """
        List all subpaths present in the database. Results are sorted (DESC and ASC) by creation date.
        """
        cur=self.con.cursor()
        if desc:
            result=cur.execute("SELECT subpath FROM files ORDER BY {} DESC".format(ordby))
        else:
            result=cur.execute("SELECT subpath FROM files ORDER BY {} ASC".format(ordby))
        result=[subpath[0] for subpath in result.fetchall()]
        return result
