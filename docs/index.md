---
---
# Crossing over
These are utilities and instructions for putting a computing device to death and
reincarnating it in another place.

When crossing a national border, these instructions provide for you to
bring your devices, but to be completely unable to resurrect or produce
**any data** without assistance from people on the other side.

The motivation comes from
[this article](https://ssd.eff.org/en/module/things-consider-when-crossing-us-border)
from the Electronic Frontier Foundation (EFF) about entering the United States.

* Q: What's better than refusing to turn-over your passwords, contacts,
  and personal data?
* A: Not having them available to begin with.

I am currently using three devices built by Apple with Apple operating systems.
This focuses on transmigrating those devices.

As a bonus, regardless of whether you are crossing a national border:
* you will have set-up and verified reliable backup and recovery
  of data on your devices.
* you will have practiced safely keeping and using secure passwords.
* you will have practiced using encryption technologies to safely store
  and share confidential data.

## Time
All of this takes time.  The backups can take hours, even a day the first
time you run them. Plan ahead.
You might want to test (and this also takes time):
* Using the backup and restore procedures on some small amount of data,
    to verify that they will work and you know how to use them.
* Using the local backup as insurance for a trial-run of the entire
    procedure before you travel.

It's best to practice and measure the time for all of these operations well
in advance of your trip.  Keep the backup fresh.
Allow yourself double the time to complete everything before you depart.

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
1. [How to install stuff](install) contains references for installing
   some of the software you might need, depending on the methods you
   select for backup, storage, and recovery.

## Before crossing
1. Use iTunes to copy the latest KeePass database(s) to iPhone and iPad.
    * MiniKeePass will accept your KeepassX `.kdbx` files.
1. Use iTunes to back-up iPhone and iPad to MacBook
   [How to from Apple](https://support.apple.com/en-us/HT203977)
   * You can also back them up to iCloud
   * You can't really back up your Mac to iCloud, not the way you can
     do with the iOS devices.  The best you can do is keep your Documents
     and Desktop folder there, and your system settings.
     [Some thoughts about iCloud](icloud) tells why I don't prefer
     iCloud as my Mac backup solution.
1. [Make rsync backups](rsync#backup) of MacBook to the encrypted backup drive
   * We are making a backup of our entire user directory.
1. Use one of several methods to put a backup in the cloud:
    * [encrypted tarball](tarball)
    * [iCloud backup](icloud) of Documents and Desktop
    * [Arq on Amazon](arq)
1. Copy your KeePass password database to iCloud.
1. Generate a long random sequence and save it in a text file- passkey
    * By "long", we mean more than a couple of dozen characters.
      Knowing the length of the passkey facilitates exhaustive search.
      However, if the key is long enough, that hardly matters.
    * It's a sequence that you can't memorize without a lot of effort.
      You won't even try.
    * It's a sequence that some friends will possibly read to you on the phone.
1. Create a plan of contacts on the other side.
    You will share parts of the passkey with them.
    You can split-up the key different ways so that
    no-one has the full key (See [splitting passwords](splits))

    It's a good idea to have multiple combinations of people from
    whom you can reconstruct the passkey.
    * Note contact phone numbers using pen and paper
    * Note who has which parts

    Generally, if a combination of the people can guess each-other, they can get
    together to reconstruct the full key.  This might be a good thing if
    you become lost.
1. Ship the passkey via
    [Signal Messenger](https://whispersystems.org/)
    or other end-to-end secure channel
    to friends on the other side, according to the plan of contacts.
    * Let them know your plans
    * Let them know how and when they should expect to hear from you
1. After enough of your contacts have confirmed that they have the passkey,
    change the iCloud password to the passkey and **verify access**.
    * verify access. This is key, because access with the passkey is the only
    way you'll access your KeePass database and reincarnate your machines.
    * You verify access to iCloud by simply logging out and logging back
    in again, making sure you can see the file(s) stored there.
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
1. Optionally, obtain a new backup drive of sufficient size.
   If you're using cloud backup, like Arq, this isn't really necessary.
1. Find a place with good internet
1. Initialize MacBook with iCloud account and passkey
1. If you want to initialize your iPhone and/or iPad now with the passkey,
   you can do that.  If you do, you'll have to enter the new iCloud account
   password after you change it.
1. Install KeePass and copy your password database from iCloud to your computer.
    * Do not delete the iCloud copy just yet.
      Restoring your backup could overwrite
      this newer one that you just pulled down from the cloud.
1. Use one of the three methods to recover your backup:
    * [encrypted tarball](tarball)
    * [iCloud backup](icloud) of Documents and Desktop
    * [Arq on Amazon](arq)
1. Ensure the freshest copy of your KeePass password database is on your
   machine.  If you copied the database to iCloud right after making the
   backup, then they are the same.
1. Change the iCloud password to something other than the passkey and
   (of course) record it in your KeePass database.
1. Initialize the iPhone and iPad with iCloud account and new password
    * If iCloud restores them, well that was easy!
1. Connect the iPhone and iPad
    * Restore them using the iTunes backup if iCloud did not restore them.
1. Update the backups of the KeePass database on the iPhone and iPad
    (It has the new backup drive recovery and iCloud passwords.)
    * It's now safe to delete the password database copy stored on iCloud.
1. All is well. Have a drink.
