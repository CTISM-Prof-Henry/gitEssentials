.. _resolvendo-conflitos-tela-1:

Definindo o método de conciliação de conflitos
==============================================

|image0|

Nesta imagem, o git não sabe como os conflitos devem ser conciliados, e está nos perguntando o que ele deve fazer
(texto escrito em amarelo). Neste material, usaremos a opção **merge**, rodando o seguinte comando:

.. code:: bash

   git config pull.rebase false

Rode novamente o comando ``git pull origin main``:

|image1|

.. only:: latex

   Siga para a :numref:`resolvendo-conflitos-tela-2` para finalizar a resolução de conflitos.

.. only:: html

   Siga para a Seção :ref:`resolvendo-conflitos-tela-2` para finalizar a resolução de conflitos.

.. |image0| image:: ../../imagens/conflito_2.png
.. |image1| image:: ../../imagens/conflito_3.png
