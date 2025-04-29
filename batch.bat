@echo off
echo Creating backup of manhattan-project folder...
xcopy /E /I /H manhattan-project manhattan-project-backup

echo Renaming folder to project-horizon...
ren manhattan-project project-horizon

cd project-horizon

echo Deleting manhattan_project.code-workspace file...
del manhattan_project.code-workspace

echo Updating references in text files...
:: Find and replace in Python files
for /R %%f in (*.py) do (
    powershell -Command "(Get-Content '%%f') -replace 'manhattan-project', 'project-horizon' | Set-Content '%%f'"
    powershell -Command "(Get-Content '%%f') -replace 'manhattan_project', 'project_horizon' | Set-Content '%%f'"
)

:: Find and replace in Markdown files
for /R %%f in (*.md) do (
    powershell -Command "(Get-Content '%%f') -replace 'manhattan-project', 'project-horizon' | Set-Content '%%f'"
    powershell -Command "(Get-Content '%%f') -replace 'manhattan_project', 'project_horizon' | Set-Content '%%f'"
)

:: Find and replace in YAML/config files
for /R %%f in (*.yml *.yaml *.json *.toml *.ini) do (
    powershell -Command "(Get-Content '%%f') -replace 'manhattan-project', 'project-horizon' | Set-Content '%%f'"
    powershell -Command "(Get-Content '%%f') -replace 'manhattan_project', 'project_horizon' | Set-Content '%%f'"
)

:: Find and replace in HTML and text files
for /R %%f in (*.html *.txt) do (
    powershell -Command "(Get-Content '%%f') -replace 'manhattan-project', 'project-horizon' | Set-Content '%%f'"
    powershell -Command "(Get-Content '%%f') -replace 'manhattan_project', 'project_horizon' | Set-Content '%%f'"
)

echo Conversion complete! The folder has been renamed to project-horizon.
echo A backup of the original folder was created as manhattan-project-backup.
echo You can now open the project-horizon.code-workspace file.
pause
