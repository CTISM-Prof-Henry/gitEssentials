# conda activate sphinx
export PATH=$PATH:node_modules/.bin
mmdc -i docsource/imagens/fork_pull_request_diagrama.mmd -o docsource/imagens/fork_pull_request_diagrama.png
mmdc -i docsource/imagens/guia_rapido_diagrama.mmd -o docsource/imagens/guia_rapido_diagrama.png
make github
make latex
(cd _build/latex && pdflatex main.tex)
(cd _build/latex && pdflatex main.tex)
