.. _resolvendo-conflitos-tela-1:

Definindo o método de conciliação de conflitos
==============================================

|image0|

Nesta imagem, o git não sabe como você quer conciliar os conflitos, e
está perguntando à você o que deve fazer (no texto escrito em amarelo).
Neste curso, vamos usar a opção **merge**, rodando o seguinte comando:

.. code:: bash

   git config pull.rebase false

Rode novamente o comando ``git pull origin main``:

|image1|

Siga para :ref:`este link <resolvendo-conflitos-tela-2>` para continuar
o tutorial.

.. |image0| image:: ../../imagens/conflito_2.png
.. |image1| image:: ../../imagens/conflito_3.png
