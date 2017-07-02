---
---
[back to index](index)
# Archive and Encrypt
## Make and use encrypted archive files

We use `tar` and `gpg` to pack up a directory full of files into a single,
encrypted archive file.  Later, we use the same tools to decrypt and expand
the archive file into a new direcory full of files.

**Note:** In the examples, we assume that the scripts have been copied
to the directory containing the backups.

## Create a compressed archive and encrypt it

The script, `compress.sh` will make the compressed archive for you.
Give it two bits of data:

1. the path to the directory to archive
2. a passphrase

The passphrase should be something not too long or short that you can readily type.
Here is an example,
```
cd /Volumes/lAvionBackup
./compress.sh bkp_test_dir 'sense8conspiracytheories?whatweretheythinking?'
```
This command can take a very long time.  It is packing and encrypting a lot
of data.  We have made it print the names of the files as it goes, so you
can see that it is making progress.  Either way, it's best to go off and
have a coffee break.  Or check-up on your email.  Or message with your friends.
Or read the
[EFF guide to crossing](https://www.eff.org/document/defending-privacy-us-border-guide-travelers-carrying-digital-devices).

The result of the compress command is a large file called `bkp_test_dir.tar.gz`.
It sits in the directory next to the `bkp_test_dir` original backup content.

As a detail, note that we didn't encrypt the contents of the archive.
We encrypted the archive itself.
The distinction means that the entire archived tree structure,
not only the file contents, requires the encryption key to access.

I don't have to tell you that losing the passphrase means losing the data.
Do not lose the passphrase.

## Verify the content of the compressed archive

This is an important file.  We want to verify that we can access the contents.
One way to verify is to produce a listing.

The `verify.sh` script will show you a listing of the archive contents.
Use it very similarly to the `compress.sh` script. Give it:

1. the name of the archive
2. the passphrase

```
cd /Volumes/lAvionBackup
./verify.sh bkp_test_dir.tar.gz 'sense8conspiracytheories?whatweretheythinking?'
```

## Decrypt and expand a compressed archive

Now we are in the situation where we have the archive, but not the original
from which the archive was made.

We have placed the archive on a fresh backup drive, and we want to expand
it (more or less) in place.

The `decompress.sh` script will expand the archive in place.
Use it very similarly to the `compress.sh` script. Give it:

1. the name of the archive
2. the passphrase

```
cd /Volumes/lAvionBackup
./decompress.sh bkp_test_dir.tar.gz 'sense8conspiracytheories?whatweretheythinking?'
```

Like compression and archiving, this can take a long time.  We output the
names of the files so that you can see that it's making progress.
Breath the air of the new place while you wait.  Don't watch.

The result will be a new copy of the backup files next to the archive,
in the same directory.
