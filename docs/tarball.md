---
---
[back to index](index)
# Encrypted tarball

## Creating the tarball
1. [Tar/compress/encrypt](cryptar) the backups as archives
1. Store the encryption passphrase in KeePass
1. **Verify** the decrypted content list of the archives so you know
    that you can decrypt them.
1. In order to help your shopping, to purchase the needed capacity, make note of
    * the on-disk sizes of the backups
    * the sizes of the archive files
1. Copy the tarball to iCloud or to [Amazon Glacier](glacier) using a client
   such as
   [Freeze](https://itunes.apple.com/us/app/freeze-for-amazon-glacier/id1046095491?mt=12)

## Retrieving the tarball
1. Install brew, git
1. Clone this repository to get the scripts
1. Install keepassx, gpg
1. Initialize the backup drive as an [encrypted device](encrypt)
    * Store the recovery key in KeePass
1. Download the backup archives from iCloud
1. [Decompress and decrypt](cryptar) the backup archives to the backup drive
1. Restore MacBook [using rsync](rsync)
