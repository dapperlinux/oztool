# oztool

## About
The oztool package is a graphical tool to create and edit oz profiles. Oztool can
add and remove directories to whitelists and blacklists, and supports most of the 
fields present in oz profile json.


## Building
To build this package, first install an RPM development chain:

```bash
$ sudo dnf install fedora-packager fedora-review

```

Next, setup rpmbuild directories with

```bash
$ rpmdev-setuptree
```
And place the file oztool.spec in the SPECS directory, and create a oztool-1 directory and place oztool inside:
```bash
$ mv oztool.spec ~/rpmbuild/SPECS/
$ mkdir oztool-1
$ mv oztool oztool-1
$ tar -cJvf oztool-1.tar.xz oztool-1
$ mv oztool-1.tar.xz ~/rpmbuild/SOURCES/
```

and finally, you can build RPMs and SRPMs with:
```bash
$ cd ~/rpmbuild/SPECS
$ rpmbuild -ba oztool.spec
```


