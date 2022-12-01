.. _trabalhando-localmente:

Trabalhando localmente
======================

.. only:: latex

   Uma vez que um repositório é clonado, utilizaremos um conjunto restrito de comandos para trabalhar localmente (ou
   seja, sem enviar os dados para a nuvem, apenas no nosso computador). Na linha de comando do computador, e dentro da
   pasta do repositório, utilizaremos os comandos ``git status``, ``git add``, ``git restore``, e ``git commit``. Você
   pode ver uma explicação detalhada para cada um deles na :numref:`comandos`. No momento, é mais interessante saber que
   cada um dos comandos desempenha uma função diferente, e que a **ordem** em que eles são usados importa. Ou seja,
   utilizar o comando ``git commit`` (que cria um checkpoint) sem antes preparar os arquivos com ``git add`` não fará
   sentido.

   Para auxiliar na compreensão da ordem de uso dos comandos, o seguinte fluxograma, adaptado do material de Fabrício
   Cabral [CABRAL2022]_, é mostrado abaixo:

   |image0|

.. only:: html

   Uma vez que um repositório é clonado, utilizaremos um conjunto restrito de comandos para trabalhar localmente (ou
   seja, sem enviar os dados para a nuvem, apenas no nosso computador). Na linha de comando do computador, e dentro da
   pasta do repositório, utilizaremos os comandos ``git status``, ``git add``, ``git restore``, e ``git commit``. Você
   pode ver uma explicação detalhada para cada um deles na Seção :ref:`comandos`. No momento, é mais interessante saber
   que cada um dos comandos desempenha uma função diferente, e que a **ordem** em que eles são usados importa. Ou seja,
   utilizar o comando ``git commit`` (que cria um checkpoint) sem antes preparar os arquivos com ``git add`` não fará
   sentido.

   Para auxiliar na compreensão da ordem de uso dos comandos, o seguinte fluxograma, adaptado do material de Fabrício
   Cabral [#]_, é mostrado abaixo:

   |image1|


.. |image0| image:: ../imagens/git_fluxo_comum.png
      :scale: 100 %

.. |image1| image:: ../imagens/git_fluxo_comum.svg
      :scale: 100 %

.. [#] Disponível em `<https://github.com/fabriciofx/gitflowchart>`__. Acesso em 30/11/2022.

.. [CABRAL2022] Cabral, Fabrício. Git flowchart. Disponível em `<https://github.com/fabriciofx/gitflowchart>`__.
   Acesso em 30/11/2022.