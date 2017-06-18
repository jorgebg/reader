#!/bin/sh

git add output.html state state.lock
git commit -m"update"
git push origin gh-pages
