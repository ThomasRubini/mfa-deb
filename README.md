# Creating the package/repository

## Create the signed package
- Create a directory for your package, e.g., `mypackage`.
- Create a `DEBIAN/control` file with your package metadata
- Put the files you want to include in the package inside the root directory (next to DEBIAN/).
- Put your hooks (e.g. to install a symlink) in the `DEBIAN/` folder
- Run `dpkg-deb --build mypackage mypackage-latest.deb` to generate your package.

## Create the repository
Prerequisites: have a GPG key for signing, imported into your keyring.
- Create a directory for the repository, e.g., `repo`, and move your `.deb` file inside.

- Run `dpkg-scanpackages . /dev/null > Packages` to generate the `Packages` file.
- Run `gzip -9c Packages > Packages.gz` to compress the `Packages` file and generate `Packages.gz`.

- Run `apt-ftparchive release . > Release` to generate the `Release` file.
- Run `gpg --default-key <YOUR_KEY_ID> -abs -o Release.gpg Release` to sign `Release`.

# Using the package/repository

## Add the repository to apt
- Create a file `/etc/apt/sources.list.d/myrepo.list` with the following content: `deb file:/path/to/repo ./`
- Add your key to the apt trusted store with `gpg --export <YOUR_KEY_ID> > /etc/apt/trusted.gpg.d/myrepo.gpg`

## Install the package
- Run `apt update` to refresh the package list.
- Run `apt install mypackage` to install your package.
