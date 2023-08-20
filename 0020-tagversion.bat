@echo off
echo Create a tag locally
git tag -a v1.0.0 -m "Version 1.0.1"

echo Push the tag to GitHub
git push origin v1.0.1
