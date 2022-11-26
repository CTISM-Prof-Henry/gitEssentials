.. _instalacao:

Instalação
==========

Este guia cobre a instalação em dois sistemas operacionais, em duas versões específicas:
Windows 10 e Linux Ubuntu 20.04 LTS. É provável que as instruções aqui funcionem para outras
versões do Windows (e.g. 7, 11), e que as instruções também funcionem para outras distribuições
do Linux (e.g. Arch, Debian, etc).

Instruções para o Windows
-------------------------

1. Baixe o git `neste link <https://git-scm.com/downloads>`__;
2. Siga o passo-a-passo do instalador;
3. No instalador do git, marque a opção que você quer adicionar o programa ao PATH do sistema;
4. Verifique se o programa foi instalado corretamente. Abra uma janela do prompt de comando
   (aperte as teclas **Logotipo do Windows** + **R**, digite `cmd` e então aperte a tecla **Enter**);
5. Se o programa não funcionar, será necessário adicionar o programa ao PATH do sistema manualmente.
   Clique com o botão direito em cima do Ícone **Meu computador**, **Propriedades**, **Recursos Avançados**,
   **Variáveis do Sistema**, onde a variável PATH se encontrar, escreva o caminho onde o git foi instalado.


Instruções para o Linux
-----------------------

1. Abra o Terminal;
2. Digite `sudo apt-get install git`;
3. Insira sua senha;
4. Feche e abra novamente o Terminal, **OU** digite `source ~/.bashrc`;
5. Teste o programa digitando `git --help`. Se uma janela como a abaixo aparecer, estará tudo certo:


|image0|


.. |image0| image:: ../imagens/instalação_git_linux_01.png
