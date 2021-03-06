---
---
[Back to index](index)
# rsync
## Using rsync for backup and restore

The `rsync` utility will synchronize files between two separate directories
or file systems.  It is like a copy, but does not copy all of the files all
of the time.  Instead, it copies only those files that have changed.

I use little shell scripts so that I don't have to remember all of the
settings every time I use them.

I keep all of these files in the `bin` sub-directory of my home directory.
I keep that as one of the directories on my PATH environment variable.

## Backup

`backup.sh` is the script for making a backup.

The directory `/Users/dclo/bkp_test_dir` is the test directory that I want backed-up.
The directory `/Volumes/lAvionBackup` is the mounted location of the backup disk.

The script uses a file, `bkp.skip.list` with a list of directories to skip (not copy).

- Among those directories is the place that iTunes puts movies.
- Another is the place where browsers keep their caches.
- Another is the place where Docker keeps its images.
- The ubiquitous MacOS .DS_Store files

The main reason to skip those is that they contain large amounts of data
that is readily recoverable from elsewhere.  This helps reduce the size of the
backups and the time needed to make them.

A second thing the script does is clean-up the log files that Mac OS keeps
on my computer.  These build-up over time and take-up space.

## Restore

`restore.sh` is the script for restoring a backup.

The `rsync` command going the other way is similar, however, I don't want it
to delete or exclude any files.  It preserves file permissions and times.

`rsync` is a little tricky about directories.
In the source specification, ending with a slash means to put the contents
of the directory in the destination. Without the ending slash, it creates the named
directory in the destination.
