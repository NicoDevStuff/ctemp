#! /usr/bin/env bash

rm -rf ~/.local/bin/cprojgen/
cp -r $PWD/ ~/.local/bin/cprojgen/

rm -rf ~/.local/bin/ctemp
cp $PWD/run.sh ~/.local/bin/ctemp
