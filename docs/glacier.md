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

### On your side

* Install the Amazon Command Line Interface
[Amazon CLI](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html).
* Amazon Glacier has extensive instructions in in its
[getting started guide](http://docs.aws.amazon.com/amazonglacier/latest/dev/amazon-glacier-getting-started.html).

Here are some items you will need to know:
* AWS Account ID
* AWS Access Key ID: <you created this earlier>
* AWS Secret Access Key: <you created this earlier>
* Region name: <you configured this for the vault>
* Output format [None]: json

Use the `aws configure` command to set defaults for your AWS commands.

## Writing a file to the vault
1. If you have not already,
    [set up a vault](http://docs.aws.amazon.com/amazonglacier/latest/dev/getting-started-create-vault.html)
1. You can verify that you have a vault and working connection to AWS Glacier
    by issuing the command,
```
aws glacier list-vaults --account-id <id>
```
   (substitude your acount id <id>). Will give a list of your vaults.
1. Get a sha-256 checksum of the archive file:
```
> openssl sha -sha256 bkp_test_dir.tar.gz
SHA256(bkp_test_dir.tar.gz)= 9aa53bda171e4d5d3b5347ff6b24ff6b5434fe06bbe0048f45c4063dbc2188d0
```
   * The command is `openssl sha -sha256 <archive_filename>`
   * The sha256 checksum is that long string of digits,
     `9aa53bda171e4d5d3b5347ff6b24ff6b5434fe06bbe0048f45c4063dbc2188d0`

1. Now use AWS CLI to push the file:
```
aws glacier upload-archive --account-id - \
  --checksum 9aa53bda171e4d5d3b5347ff6b24ff6b5434fe06bbe0048f45c4063dbc2188d0 \
  --archive-description bkp_test_dir.tar.gz \
  --vault-name backup --body /Volumes/lAvionBackup/bkp_test_dir.tar.gz
```
    Depending on your uplink speed, this can take a while.
    Remember, it is called "Glacier."
    You won't get any output/feedback until it is finished.
    Then it will print some JSON.  Something like this,
```
{
  "archiveId": "kKB7ymWJVpPSwhGP6ycSOAekp9ZYe_--zM_mw6k76ZFGEIWQX-ybtRDvc2VkPSDtfKmQrj0IRQLSGsNuDp-AJVlu2ccmDSyDUmZwKbwbpAdGATGDiB3hHO0bjbGehXTcApVud_wyDw",
  "checksum": "9aa53bda171e4d5d3b5347ff6b24ff6b5434fe06bbe0048f45c4063dbc2188d0",
  "location": "/0123456789012/vaults/my-vault/archives/kKB7ymWJVpPSwhGP6ycSOAekp9ZYe_--zM_mw6k76ZFGEIWQX-ybtRDvc2VkPSDtfKmQrj0IRQLSGsNuDp-AJVlu2ccmDSyDUmZwKbwbpAdGATGDiB3hHO0bjbGehXTcApVud_wyDw"
}
```

1. Save that JSON output in a KeePass entry.  You will need the information
    to retrieve the data.
