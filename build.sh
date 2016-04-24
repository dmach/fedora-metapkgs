#!/bin/sh
set -e

mkdir -p rpm/src

for spec in *.spec; do
    rpmbuild --quiet -ba --nodeps --define "_srcrpmdir rpm/src" --define "_rpmdir rpm" $spec
done
