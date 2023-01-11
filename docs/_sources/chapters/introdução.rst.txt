.. _introducao:

Introdução
==========

Este material organiza o conhecimento sobre o uso de git e Github. O git é uma ferramenta de **versionamento**. Quando
estamos trabalhando no desenvolvimento de um trabalho que demora muito tempo para ser concluído (por exemplo,
desenvolver um algoritmo, um software, ou até mesmo escrever um relatório de estágio), é desejável que possamos salvar
versões **intermediárias** do nosso trabalho, de maneira que possamos recuperá-lo no futuro. Por exemplo, a primeira
versão de um software pode possuir uma funcionalidade que foi removida em uma segunda versão; se, todavia, deseja-se
reimplementar esta funcionalidade na terceira versão do software, como faríamos para recuperar o código-fonte, se ele
já foi excluído? Com o git, isto é possível!

O git foi desenvolvido por `Linus
Torvalds <https://en.wikipedia.org/wiki/Linus_Torvalds>`__ em 2005 para
desenvolver o Linux, dado que ele precisava, justamente, controlar as
diversas versões das funcionalidades implementadas neste sistema operacional.

O git é um programa instalado no seu computador. A maneira mais popular de
usar o git é pela linha de comando, através de sua CLI (*command line interface*).
É possível também usar o git com programas com interfaces gráficas, e também dentro
de ambientes de desenvolvimento integrado (IDEs, na sigla em inglês), como Pycharm,
VS Code, etc, porém este material lhe ensinará a mexer no git pela linha de comando.

Colocamos em uma pasta no nosso computador o código-fonte que desejamos versionar
(em outras palavras, salvar versões dele). Uma pasta do git é chamada de
**repositório**. O git cria um *checkpoint* para cada versão dos arquivos neste
repositório. Na terminologia do git, os *checkpoints* são chamados de *commits*.

O git é uma ferramenta totalmente *offline*, desconectada da Internet. Ou seja,
por mais que tenhamos diversos commits do nosso código-fonte, eles ficarão salvos
no nosso computador, localmente. Se nosso computador estragar, perderemos todo
nosso trabalho!

Para isto, foram criados sites para salvar commits na nuvem. O GitHub é, na data
de escrita deste material, o site mais popular neste sentido. Existem outros, como
GitLab, GitKraken, BitBucket, etc. Este material, no entanto, usará o GitHub como
padrão.

É incorreto e ineficiente usar outros métodos para manter controle de versão de
código-fonte, como por exemplo:

-  Salvar o código em uma conversa com si mesmo no Whatsapp;
-  Enviar um e-mail para si mesmo com o código;
-  Usar um programa que não foi feito para este propósito (e.g.
   Microsoft Word, ou Google Docs);
-  Salvar o código-fonte em um arquivo na nuvem (por exemplo no Google
   Drive).

O git não apenas resolve o problema de salvar código-fonte de uma
maneira eficiente, como também apresenta soluções para trabalhar
colaborativamente. Ou seja, caso dois ou mais programadores precisem
trabalhar no mesmo código, o git tem as ferramentas necessárias para
integrar as modificações.
