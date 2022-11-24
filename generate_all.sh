mmdc -i docsource/source/fork_pull_request_diagrama.mmd -o docsource/imagens/fork_pull_request_diagrama.svg
mmdc -i docsource/source/guia_rapido_diagrama.mmd -o docsource/imagens/guia_rapido_diagrama.svg
make github
make latex
(cd _build/latex && pdflatex main.tex)
(cd _build/latex && pdflatex main.tex)
