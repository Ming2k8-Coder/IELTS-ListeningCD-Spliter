@ echo off
echo IELTS ListeningCD Spliter by MingCoder-2k8 (https://github.com/Ming2k8-Coder/IELTS-ListeningCD-Spliter)
:venv
if exist .venv\ (
    echo .venv exist!
    .venv\Scripts\activate
    process.py .\.working\configIELTS-NTV.py
    goto end
) else (
    echo .venv not Found!
    goto create.venv
)
:create.venv
python --version 3>NUL
if errorlevel 1 goto errorNoPython
python -m venv .venv
goto venv
:errorNoPython
echo Python not installed! Plese installed
goto end
:end
pause
