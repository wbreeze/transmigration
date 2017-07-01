rsync -amvz --delete --progress --exclude-from '/Users/dclo/Documents/p/transmigration/bkp.skip.list' --delete-excluded /Users/dclo/bkp_test_dir /Volumes/lAvionBackup
find /Users/dclo/Library/Logs -type f -atime -2w -exec rm -- {} +
