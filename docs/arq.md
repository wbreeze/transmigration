---
---
[back to index](index)
# Backup with Arq
Arq is a backup solution for the Mac that will use Amazon Cloud storage.
It will also encrypt all of your backups, so that only someone with the
encryption passkey (you) can read them.

## Setup
[Download Arq](https://www.arqbackup.com/)
from the Apple app store.

You will need an Amazon account and a Glacier file vault. See
[these instructions about glacier](glacier).
* Be sure to store all of the Amazon credentials (they are multiple)
  in your password safe.
* Store the Amazon MFA device recovery key in your password safe.

## Backing up
Arq does a really nice job of keeping a fresh backup using off-site, secure
storage:

1. Introduce Arq the Amazon Glacier file vault.
1. Add your home directory to the backup.
1. Generate and store your backup encryption key with your password safe.
1. Backup your password safe separately.

**Note** You are lost without all of these credentials: storage
identifiers, keys, MFA device recovery, backup encryption key.
Absolutely you must be able to retrieve them from your password safe.

## Restoring
Use your password safe to find all of the credentials requested by
Arq in order to access and retrieve your backup.
