.. _enviando-para-nuvem:

Enviando para nuvem
===================

Depois que terminarmos de salvar as modificações localmente, é interessante enviá-las para um repositório remoto, de
maneira que exista outra cópia dos nossos commits, em outro computador. Convencionou-se chamar de "nuvem" qualquer
serviço que é ofertado na Internet. Portanto, para clareza de explicação, iremos nos referir ao GitHub como um servidor
na nuvem, apesar que, estritamente falando, ele é um servidor remoto para armazenamento de repositórios git.

.. only:: latex

   Para que seja possível enviar os commits para o GitHub, é necessário primeiro que o repositório remoto exista. Como
   este material começa criando um repositório remoto na :numref:`criando-repositorios`, nos resta apenas enviar o código
   com ``git push``.

.. only:: html

   Para que seja possível enviar os commits para o GitHub, é necessário primeiro que o repositório remoto exista. Como
   este material começa criando um repositório remoto na Seção :ref:`criando-repositorios`, nos resta apenas enviar o
   código com ``git push``.

O fluxograma abaixo foi adaptado do material de Fabrício Cabral no seu repositório [#]_, e mostra como enviamos o
código-fonte para o repositório remoto:

|image0|

.. only:: latex

   Note que quando **clonamos** um repositório, o nosso repositório remoto já possui uma versão remota. Pode ser que, no
   processo de enviar o código-fonte para o repositório remoto, apareçam conflitos no código. Isto ocorre porque as
   versões local e remota estão **desincronizadas**. Em outras palavras, existem modificações em uma das duas versões que
   não estão presentes na outra versão. Contudo, o git consegue identificar exatamente onde estes conflitos estão, e
   oferece ferramentas para conciliar as versões diferentes. Um guia de como resolver estes conflitos é apresentado na
   :numref:`resolvendo-conflitos`.

.. only:: html

   Note que quando **clonamos** um repositório, o nosso repositório remoto já possui uma versão remota. Pode ser que, no
   processo de enviar o código-fonte para o repositório remoto, apareçam conflitos no código. Isto ocorre porque as
   versões local e remota estão **desincronizadas**. Em outras palavras, existem modificações em uma das duas versões que
   não estão presentes na outra versão. Contudo, o git consegue identificar exatamente onde estes conflitos estão, e
   oferece ferramentas para conciliar as versões diferentes. Um guia de como resolver estes conflitos é apresentado na
   Seção :ref:`resolvendo-conflitos`.


.. |image0| image:: ../imagens/git_fluxo_compartilhamento.png
   :scale: 100 %

.. [#] Disponível em `<https://github.com/fabriciofx/gitflowchart>`__. Acesso em 30/11/2022.