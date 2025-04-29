@echo off
echo Setting up Git repository for Project Horizon...

cd /d "F:\Bryte Idea\project-horizon"

"C:\Program Files\Git\bin\git.exe" init
"C:\Program Files\Git\bin\git.exe" config user.name "Ron Avis"
"C:\Program Files\Git\bin\git.exe" config user.email "ronavis@gmail.com"
"C:\Program Files\Git\bin\git.exe" remote add origin https://github.com/bryteidea/project-horizon.git
"C:\Program Files\Git\bin\git.exe" add .
"C:\Program Files\Git\bin\git.exe" commit -m "Add Project Horizon brand assets and updated README banner"
"C:\Program Files\Git\bin\git.exe" branch -M main
"C:\Program Files\Git\bin\git.exe" push -u origin main

echo Repository setup complete. Check for any errors above.
pause 