set -xe

rm -f repo/mypackage-latest.deb
dpkg-deb --build mypackage repo/mypackage-latest.deb
debsigs --sign=origin -k E78912536665F4C59CD0742EC7D287C8C1CAC373 repo/mypackage-latest.deb
