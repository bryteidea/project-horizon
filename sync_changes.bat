@echo off
echo Syncing changes with GitHub...

cd /d "F:\Bryte Idea\project-horizon"

"C:\Program Files\Git\bin\git.exe" add .
"C:\Program Files\Git\bin\git.exe" commit -m "Remove batch files"
"C:\Program Files\Git\bin\git.exe" push origin main

echo Changes synced. Check for any errors above.
del "%~f0" 