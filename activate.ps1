# Use this in PowerShell

# for Venv
Set-ExecutionPolicy Unrestricted -Scope Process
.venv/scripts/Activate
$host.ui.RawUI.WindowTitle = 'Debug (Django)'
py .\projetos\manage.py runserver localhost:35001