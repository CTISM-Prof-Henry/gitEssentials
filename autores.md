# Instruções para autores

Caso você queira gerar uma documentação derivada deste repositório, siga os passos listados abaixo.

## Para gerar a documentação em HTML

Siga o tutorial do repositório https://github.com/henryzord/sphinxTutorial.

## Para gerar a documentação em PDF (e-book)

1. Siga o tutorial do repositório https://github.com/henryzord/sphinxTutorial;
2. Gere o arquivo main.tex usando o comando `make latex`;
3. Adicione as seguintes linhas no arquivo main.tex:
   
   **Antes:**

   ```latex
   \pagestyle{empty}
   \sphinxmaketitle
   \pagestyle{plain}
   \sphinxtableofcontents
   \pagestyle{normal}
   \phantomsection\label{\detokenize{index::doc}}
   ```
   
   **Depois:**

   ```latex
   \pagestyle{empty}
   \sphinxmaketitle
   % adiciona folha em branco para folha de rosto
   \blankpage
   \blankpage
   % adiciona folha em branco para folha de rosto
   \pagestyle{plain}
   \sphinxtableofcontents
   \pagestyle{normal}
   \phantomsection\label{\detokenize{index::doc}}
   ```
   
4. Fontes utilizadas no documento (para calofão):
   
   * Serifada: TeX Gyre Termes (genérica de Times New Roman)
   * Sem serifa: TeX Gyre Heros (genérica de Helvetica)
   * Monoespaçada: txtt
   * Tamanho da fonte: 12pt
   