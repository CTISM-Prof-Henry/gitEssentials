# conda activate sphinx
export PATH=$PATH:node_modules/.bin
mmdc -i docsource/imagens/fork_pull_request_diagrama.mmd -o docsource/imagens/fork_pull_request_diagrama.png
mmdc -i docsource/imagens/guia_rapido_diagrama.mmd -o docsource/imagens/guia_rapido_diagrama.png
mmdc -i docsource/imagens/git_fluxo_comum.mmd -o docsource/imagens/git_fluxo_comum.png
mmdc -i docsource/imagens/fork_pull_request_diagrama.mmd -o docsource/imagens/fork_pull_request_diagrama.svg
mmdc -i docsource/imagens/guia_rapido_diagrama.mmd -o docsource/imagens/guia_rapido_diagrama.svg
mmdc -i docsource/imagens/git_fluxo_comum.mmd -o docsource/imagens/git_fluxo_comum.svg
make remove_latex_files
make github
make latex
python replace.py
(cd _build/latex && pdflatex main.tex)
(cd _build/latex && pdflatex main.tex)

