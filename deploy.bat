@ echo off

echo Starting Git Deployment

git init
git add .
git commit -m "commit"
git branch -M main
git remote add origin https://github.com/ZohanHaqu/searchnarwhal.git
git push -u origin main