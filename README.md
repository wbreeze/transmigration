# Transmigration
## The soul of a new machine
These are utilities and instructions for putting a machine to death and
reincarnating it in another place.
The instructions provide for you to be completely unable to resurrect
or produce **anything**
without assistance from people on the other side.

I am currently using three devices built by Apple with Apple operating systems.
This focuses on transmigrating those devices.

### Note about the subtitle
The subtitle is a rip from the title of a non-fiction book by Tracy Kidder,
published by Little, Brown and Company in 1981.
There is really no parallel between this and what the book is about.
The parallel stops at the title.

I recommend
[the book](https://en.wikipedia.org/wiki/The_Soul_of_a_New_Machine)
if you're interested in computing technology and how it is (or was) made.

* It won both a Pulitzer Prize and a National Book Award in 1982.
* It's a thrilling read.

## Before crossing
1. If not already using full disk encryption on MacBook, do so.
1. Have an encrypted backup drive-- an external storage file system
    * Have the recovery key in the KeePass database.
1. Copy latest KeePass database(s) to iPhone and iPad
    * It doesn't matter that you know the password because you will lose
      access to this file.
1. Back-up iPhone and iPad to MacBook using iTunes
1. Make rsync backups of MacBook to the encrypted backup drive
1. Tar/compress/encrypt the backups as archives
1. Store the encryption password in KeePass
1. **Verify** the decrypted content list of the archives so you know
    that you can decrypt them.
1. Make note of
    * the on-disk sizes of the backups
    * the sizes of the archive files
1. Ship the encrypted archive files to Amazon Glacier
1. Store the Amazon Glacier coordinates and keys in KeePass
1. **Verify** that the archives can be retrieved from Amazon Glacier
1. Place a copy of the KeePass database in Apple Cloud storage- KPCloud file
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
1. Ship the passkey via Signal Messenger to friends on the other side according to
    the plan of contacts.
    * Let them know your plans
    * Let them know how and when they should expect to hear from you
1. After enough of your contacts have confirmed that they have the passkey,
    change the iCloud password to the passkey and **verify access**.
    * verify access. This is key, because access with the passkey is the only
    way you'll reincarnate your machines.
1. Hard reset all three devices, including loss of the passkey
    * You have now lost access to everything until your friends help you
1. Leave the backup drive behind. (It too is useless without the passkey,
    but there's absolutely no need to carry the data with you.)
1. Take the contact numbers

## Cross to the other side

## Once on the other side
1. Obtain a new backup drive of sufficient size
1. Contact enough people to reassemble the passkey
1. Let everyone else know you're across
1. Initialize MacBook with iCloud account and passkey
1. Change the iCloud password to something other than the passkey
1. Install brew, git
1. Clone this repository to get the scripts
1. Install keepassx, amazon
1. Open the KPCloud file
    * It contains the Amazon Glacier information
1. Request the backup archives from Amazon Glacier
1. Install gpg
1. Initialize the backup drive as an encrypted device
    * Store the recovery key in KeePass
1. Retrieve backup archives from Amazon Glacier
1. Decompress and decrypt the backup archives to the backup drive
1. Restore MacBook using rsync
1. Initialize iPhone and iPad with iCloud account (new password)
1. Connect the iPhone and iPad and restore using iTunes
1. Remove files from Amazon Glacier as wanted
    * Remove access information from KeePass as wanted
1. Update the backups of the KeePass database on the iPhone and iPad
    if desired. (It has the new backup drive recovery password.)
1. All is well. Have a drink.
