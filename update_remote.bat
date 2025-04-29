@echo off
echo Updating Git remote to point to the new GitHub repository...

cd /d "F:\Bryte Idea\project-horizon"

"C:\Program Files\Git\bin\git.exe" remote remove origin
"C:\Program Files\Git\bin\git.exe" remote add origin https://github.com/bryteidea/project-horizon.git
"C:\Program Files\Git\bin\git.exe" add .
"C:\Program Files\Git\bin\git.exe" commit -m "Update README formatting"
"C:\Program Files\Git\bin\git.exe" push -u origin main

echo Remote URL updated. Check for any errors above.
pause 