---
---
These are utilities and instructions for putting a machine to death and
reincarnating it in another place.
The instructions provide for you to be completely unable to resurrect
or produce **anything**
without assistance from people on the other side.

The motivation for this comes from
[this article](https://ssd.eff.org/en/module/things-consider-when-crossing-us-border)
from the Electronic Frontier Foundation (EFF) about crossing borders.

* Q: What's better than refusing to turn-over your passwords, contacts,
  and personal data?
* A: Not having them available to begin with.

I am currently using three devices built by Apple with Apple operating systems.
This focuses on transmigrating those devices.

## Setup before and after
1. If not already using full disk encryption
    ([FileVault](https://support.apple.com/en-us/HT204837)) on MacBook, do so.
1. If not already using a password safe, such as
    [KeePassX](https://www.keepassx.org/) and
[MiniKeePass](https://itunes.apple.com/us/app/minikeepass-secure-password-manager/id451661808),
    do so now.
1. Have an [encrypted backup drive](encrypt)-- an external storage file system
    * Have the recovery key in the KeePass database.
1. If you are using security token based Multi-Factor or
    Two-Factor Authentication (2FA/MFA), with an app on your phone
    such as
    [Authy](https://itunes.apple.com/us/app/authy/id494168017),
    ensure that you have the security
    tokens stored in your KeePass database.  Why?
    * You are going to wipe clean your phone and lose the security tokens
        currently stored in Authy.
    * Hopefully, your iPhone backup will restore them, but what if you
        need one of them to get to your iPhone backup?
    * It's a good practice to follow in any case.
1. See [How to install stuff](install).

## Before crossing
1. Use iTunes to copy the latest KeePass database(s) to iPhone and iPad.
    * MiniKeePass will accept your KeepassX `.kdbx` files.
1. Use iTunes to back-up iPhone and iPad to MacBook
   [How to from Apple](https://support.apple.com/en-us/HT203977)
   * You can also back them up to iCloud
   * You can also back up your Mac to iCloud
1. [Make rsync backups](rsync#backup) of MacBook to the encrypted backup drive
1. [Tar/compress/encrypt](cryptar) the backups as archives
1. Store the encryption passphrase in KeePass
1. **Verify** the decrypted content list of the archives so you know
    that you can decrypt them.
    ([Archive and Encrypt](cryptar) instructions.)
1. In order to help your shopping, to purchase the needed capacity, make note of
    * the on-disk sizes of the backups
    * the sizes of the archive files
1. Ensure that iCloud drive has sufficient capacity for the encrypted archive
1. Move your encrypted archive onto iCloud drive.
1. Generate a long random sequence and save it in a text file- passkey
    * Thirty-two characters should be enough
    * It's a sequence that you can't memorize without a lot of effort.
     You won't even try.
1. Create a plan of contacts on the other side.
    You will share parts of the passkey with them.
    You can split-up the key different ways so that
    no-one has the full key:
    * 1st half
    * 2nd half
    * Odd characters
    * Even characters

    It's a good idea to have multiple combinations of people from
    whom you can reconstruct the passkey.
    * Note contact phone numbers using pen and paper
    * Note who gets which parts

    Generally, if a combination of the people can guess each-other, they can get
    together to reconstruct the full key.  This might be a good thing if
    you become lost.
1. Ship the passkey via
    [Signal Messenger](https://whispersystems.org/)
    to friends on the other side according to
    the plan of contacts.
    * Let them know your plans
    * Let them know how and when they should expect to hear from you
1. After enough of your contacts have confirmed that they have the passkey,
    change the iCloud password to the passkey and **verify access**.
    * verify access. This is key, because access with the passkey is the only
    way you'll reincarnate your machines.
1. [Hard reset](reset) all three devices, including loss of the passkey
    * You have now lost access to everything until your friends help you
1. Leave the backup drive behind. (It too is useless without the passkey,
    but there's absolutely no need to carry the data with you.)
1. Take the contact numbers.

## Cross to the other side
* Enjoy a little break from the network connected world.

## Once on the other side
1. Contact enough people to reassemble the passkey
1. Let everyone else know you're across
1. Obtain a new backup drive of sufficient size
1. Initialize MacBook with iCloud account and passkey
    * If iCloud restores the computer, all the better
1. Change the iCloud password to something other than the passkey
1. Install brew, git
1. Clone this repository to get the scripts
1. Install keepassx, gpg
1. Initialize the backup drive as an [encrypted device](encrypt)
    * Store the recovery key in KeePass
1. Download the backup archives from iCloud
1. [Decompress and decrypt](cryptar) the backup archives to the backup drive
1. Restore MacBook [using rsync](rsync)
1. Initialize iPhone and iPad with iCloud account (new password)
    * If iCloud restores them, all the better
1. Connect the iPhone and iPad and restore, if necessary, using iTunes
1. Remove files from iCloud
1. Update the backups of the KeePass database on the iPhone and iPad
    if desired. (It has the new backup drive recovery password.)
1. All is well. Have a drink.
