set -xe

rm -f mypackage-latest.deb
dpkg-deb --build mypackage mypackage-latest.deb
debsigs --sign=origin -k E78912536665F4C59CD0742EC7D287C8C1CAC373 mypackage-latest.deb
