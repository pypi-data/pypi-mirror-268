# Manage your notes with pnote!

## About

*pnote* is a text file, format agnostic, note manager.
It allows to keep a consistant hierarchy of note files that you can work with.

## Getting started
Installation:
```
> pip install pnote
```

Create a new project:
```
> pnote ~/mynotes
> # See configuration in ~/mynotes/config.json
```

Open and edit today's note file:
```
> pnote ~/mynotes -t
```

## Features

Search for files:
```
> pnote ~/mynotes search -h
```

Tag files:
```
> pnote ~/mynotes tag -h
```

Manage your project:
```
> pnote ~/mynotes admin -h
```

Export your notes:
```
> pnote ~/mynotes search --subpath | pnote ~/mynotes export --json
> pnote ~/mynotes search --subpath | pnote ~/mynotes export --template template.txt
```

For more information on *pnote*:
```
> pnote -h
```