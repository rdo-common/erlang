#!/bin/bash
# Usage:
#    ./otp-get-patches.sh /path/to/otp OTP_R14B01 fedora-R14B01
#
# Note:
#    We do NOT update erlang.spec or the git index at all.
#    For now, take a look at the patch-list-*.txt files
#    generated in the tmpdir manually copy and adapt them
#    to erlang.spec. Then handle the otp-*.patch files:
#
#        git rm -f otp-00*.patch
#        mv tmp.foobar/otp-00*.patch .
#        git add otp-00*.patch
#
#    We could only automate this if we added the required patch
#    specific spec file conditionals to the commit message somehow,
#    and then had this script transfer the conditionals into erlang.spec.

otp_dir="${1:?'Fatal: otp git repo dir required'}"
otp_upstream="${2:?'Fatal: git ref to upstream release required'}"
otp_fedora="${3:?'Fatal: git ref to branch with fedora patches required'}"

set -e
# set -x

tmpdir="$(mktemp -d --tmpdir="$PWD")"

pushd "$otp_dir"
git format-patch -o "$tmpdir" "${otp_upstream}..${otp_fedora}" > "$tmpdir/patch-list.txt"
popd

test -s "$tmpdir/patch-list.txt"

echo "# start of autogenerated patch tag list" > "$tmpdir/patch-list-tags.txt"
echo "# start of autogenerated prep patch list" > "$tmpdir/patch-list-prep.txt"
n=1
while read patch
do
	otppatch="$(dirname "$patch")/otp-$(basename "$patch")"
	mv -f "$patch" "$otppatch"
	echo "Patch$n: $(basename "$otppatch")" >> "$tmpdir/patch-list-tags.txt"
	base="$(basename "$patch" ".patch" | sed 's/^00[0-9][0-9]-//')"
	backupext=".$(echo -n "$base" | tr -c -s '[:alnum:]' '_')"
	echo "%patch$n -p1 -b ${backupext}" >> "$tmpdir/patch-list-prep.txt"
	n=$(($n + 1))
done < "$tmpdir/patch-list.txt"
echo "# end of autogenerated patch tag list" >> "$tmpdir/patch-list-tags.txt"
echo "# end of autogenerated prep patch list" >> "$tmpdir/patch-list-prep.txt"

echo "Results in tmp dir \`$tmpdir':"
echo
cat "$tmpdir/patch-list-tags.txt"
echo
cat "$tmpdir/patch-list-prep.txt"

echo
echo "Run \`rm -rf \"$(basename "$tmpdir")\"' when you are finished with the files."
# End of file.
