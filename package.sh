rm -f mypackage-latest.deb
dpkg-deb --build mypackage mypackage-latest.deb
gpg --default-key E78912536665F4C59CD0742EC7D287C8C1CAC373 --detach-sign mypackage-latest.deb
