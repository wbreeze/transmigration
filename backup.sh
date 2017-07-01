rsync -amvz --delete --progress --exclude-from '/Users/dclo/bin/bkp.skip.list' --delete-excluded /Users/dclo /Volumes/Backup
find /Users/dclo/Library/Logs -type f -atime -2w -exec rm -- {} +
