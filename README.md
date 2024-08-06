# ESpeak as Say

This is a hyper niche RPM package that essentially installs a bash script to `/usr/bin/say`
allowing programs that expect the old `say` to instead call espeak.

This is an RPM package because I use Bazzite and it seemed really weird and
annoying to setup a whole blue build image and constantly publish new images
all for what could just be a layered RPM package.

# Building the Package Locally

1. Drop into a distrobox for fedora if necessary
2. `dnf install fedora-packager rpmdevtools`
3. `rpmdev-setuptree`
4. `VER=( cat .release-please-manifest.json | jq -r '.["."]' ) tar --transform 's,^,espeak-as-say-$VER/,' -czvf ~/rpmbuild/SOURCES/espeak-as-say-$VER.tar.gz *`
5. `rpmbuild -ba espeak-as-say.spec`
5. Return to your normal terminal
6. `rpm-ostree install $HOME/rpmbuild/RPMS/x86_64/espeak-as-say-1.0.0-1.fc40.x86_64.rpm`
7. Reboot into new ostree
8. Enjoy TTS from IINACT + Cactbot I guess.
