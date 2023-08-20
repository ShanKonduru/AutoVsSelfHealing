@echo off
echo Create a tag locally
git tag -a v1.1.1 -m "Version 1.1.1"

echo Push the tag to GitHub
git push origin v1.1.1
