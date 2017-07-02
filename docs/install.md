---
---
[back to index](index)
# How to install stuff
## We stand on the shoulders of giants

Here are pointers to help install the tools necessary to get through
all of this.  These are MacOS specific.


* I use `umask 0002` at the top of my `.bash_profile` to enable write
    access to groups, by default, on new files.  This allows me to share
    my HomeBrew installations across multiple users on the same machine.
* [Homebrew](https://brew.sh/)
    ```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    ```
* Git `brew install git`
* GPG `brew install ggp2`
* [KeePassX](https://www.keepassx.org/) Downloads includes a MacOS binary.
* Command line tools `xcode-select --install`
    Or use the Developer Tools
    [download](https://developer.apple.com/download/more/)
