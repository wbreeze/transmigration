echo "Archiving $1"
echo "With password '$2'"
tar -cvz --options gzip:compression-level=9 $1 | gpg2 --symmetric --batch --passphrase $2 >$1.tar.gz
