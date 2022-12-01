
.. _resolvendo-conflitos:

Resolvendo conflitos
====================

Um conflito ocorre quando duas versões do repositório estão dessincronizadas, e é impossível determinar quais
modificações devem ser preservadas, e quais devem ser descartadas. Estas versões não são commits diferentes,
mas sim repositórios distintos: por exemplo, um repositório remoto e um repositório local. As modificações introduzidas
no repositório remoto podem vir quando clonamos este repositório em outra máquina, que não o nosso computador pessoal,
modificamos o código e enviamos ao repositório remoto; ou então quando um colega de trabalho introduz estas modificações
a partir do seu computador pessoal.

É possível ver que um conflito ocorreu quando tentamos dar um ``git push`` e a seguinte tela aparece:

|image0|

Para auxiliá-lo na compreensão deste fenômeno, é disponibilizado um repositório de código-fonte [#]_, usado nas imagens
desta Seção. O que vemos na imagem acima está basicamente dizendo que não podemos enviar o código-fonte para o GitHub
pois existem modificações nos arquivos que ainda não colocamos no repositório local. Precisamos então baixá-las, usando
o comando ``git pull``.

Às vezes, o git consegue conciliar ambas as duas versões de código-fonte (local e remota). Porém, quando isto não é
possível, nós mesmos teremos que resolver o conflito que ocorreu nos arquivos. Saberemos que é necessário fazer isto
quando, ao dar um ``git pull``, a tela

|image1|

Ou então a tela

|image2|

aparecer. Dependendo de qual tela aparecer, teremos que seguir caminhos diferentes:

.. only:: latex

   -  Primeira tela: siga para a :numref:`resolvendo-conflitos-tela-1`
   -  Segunda tela: siga para a :numref:`resolvendo-conflitos-tela-2`
   -  Nenhuma das duas: siga para a :numref:`resolvendo-conflitos-tela-3`

.. only:: html

   -  Primeira tela: siga para a Seção :ref:`resolvendo-conflitos-tela-1`
   -  Segunda tela: siga para a Seção :ref:`resolvendo-conflitos-tela-2`
   -  Nenhuma das duas: siga para a Seção :ref:`resolvendo-conflitos-tela-3`

.. toctree::
   :maxdepth: 2
   :hidden:

   resolvendo_conflitos_tela_1
   resolvendo_conflitos_tela_2
   resolvendo_conflitos_tela_3

.. |image0| image:: ../../imagens/conflito_1.png
.. |image1| image:: ../../imagens/conflito_2.png
.. |image2| image:: ../../imagens/conflito_3.png

.. [#] Disponível em `<https://github.com/CTISM-Prof-Henry/gitTest>`__. Acesso em 01/12/2022.