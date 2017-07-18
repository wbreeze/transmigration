---
---
[back to the index](index)
# Storing and retrieving from Amazon Glacier
## Your archive in the sky

Here you go! This is your machine's little angel spirit in heaven.

We're using a product from Amazon Web Services (AWS) that they call
"Glacier".  It is very inexpensive bulk file storage.  It can take
massive files.  Freeze them.  And deliver them back on request.

Files stored wih Glacier are not immediately available online.  Amazon will take
them into off-line storage, like tape backups.  When you ask for them,
they bring them online for a short time in order for you to
retrieve them.  This keeps the cost down.

## Setting-up with Amazon
1. You need an account with Amazon.
    If you have shopped with Amazon, you probably have one.
    Here is the link to [sign up with Amazon](https://www.amazon.com/ap/register).
1. You want to
[create MFA](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html)
   for your root account.  However, be sure to store the security token
   in your KeePass database.  If you are using your phone,
   you are using a "Virtual MFA device".
1. You will create an
   [IAM user](https://console.aws.amazon.com/iam/home?#/home)
   with all access priviliges to Amazon Glacier.
   Amazon is pretty insistent about not using your root credentials to
   access and use AWS.
1. You will create an access key.  Ensure that you have this key stored
   in your KeePass database.
1. Find the Glacier product and
   [set-up a vault](http://docs.aws.amazon.com/amazonglacier/latest/dev/working-with-vaults.html).

Amazon Glacier has extensive instructions in in its
[getting started guide](http://docs.aws.amazon.com/amazonglacier/latest/dev/amazon-glacier-getting-started.html).

### On your side
Install something for working with glacier.  Your choice:
* [Amazon CLI](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html).
* [Freeze](https://itunes.apple.com/us/app/freeze-for-amazon-glacier/id1046095491?mt=12)
* [Arq](https://www.arqbackup.com/)

Here are some items you will need to know:
* AWS Account ID
* AWS Access Key ID: <you created this earlier>
* AWS Secret Access Key: <you created this earlier>
* Region name: <you configured this for the vault>
* Output format [None]: json
* How to [set up a vault](http://docs.aws.amazon.com/amazonglacier/latest/dev/getting-started-create-vault.html)
