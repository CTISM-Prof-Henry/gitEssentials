@REM activate sphinx environment before running this file!
@REM conda activate sphinx
@echo 'Removing LaTeX files...'
@call make.bat remove_latex_files
@echo 'Generating HTML files and moving to docs'
@call make.bat github
@echo 'Generating LaTeX files'
@call make.bat latex
@call python replace.py
@echo 'Building PDF...'
@cd _build\latex
@pdflatex main.tex
@pdflatex main.tex
@cd ..\..
@echo 'Success!'