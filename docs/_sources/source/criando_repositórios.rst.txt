.. _criando-repositorios:

Criando repositórios
====================

No decorrer do curso, pode ser que você queira organizar os arquivos de
uma disciplina em um repositório do Github. Você pode fazer isso
acessando o link https://github.com/new.

Você se deparará com uma tela parecida com esta:

|image0|

Você precisará configurar todos os 8 itens. A seguir está a descrição do
que cada um deles faz:

1. **Template:** Se você está copiando a *estrutura* de outro
   repositório, ou não. Deixe este campo inalterado para este tutorial.
2. **Proprietário:** Se você tiver mais de uma conta no Github (por
   exemplo, se você fizer parte de uma organização na condição de
   administrador, como a
   `CTISM-Prof-Henry <https://github.com/CTISM-Prof-Henry>`__), você
   pode escolher qual conta será a proprietária do repositório. Deixe a
   sua conta pessoal neste tutorial.
3. **Nome do repositório:** Escolha um nome que faça sentido para o que
   você estiver armazenando (por exemplo, *codigos_algoritmos*, ou
   *codigos_frontend*)
4. **Descrição:** uma pequena descrição textual para dizer do que se
   trata o repositório. É opcional, mas sempre é bom preenchê-la.
5. **Público ou privado:** um repositório *público* está acessível para
   qualquer pessoa na internet; todo mundo pode vê-lo (inclusive seus
   colegas!). Já um repositório privado é acessível apenas para você e
   quem você incluí-lo ( através das configurações do repositório).
   Prefira sempre fazer repositórios privados.
6. **Adicionar arquivo README:** É um arquivo Markdown com uma descrição
   mais detalhada sobre as coisas que estão contidas no repositório.
   Apesar de opcional, é recomendável sempre incluir um arquivo README.
7. **.gitignore:** um arquivo do git usado para ignorar certos arquivos
   (em outras palavras, evitar que envie-mos estes arquivos para o
   repositório remoto, e também que o git mantenha um controle sobre as
   versões destes arquivos). É dependente da linguagem de programação
   que você está utilizando. Se não houver nada que você queira ignorar
   no momento, você pode sempre criar o arquivo .gitignore
   posteriormente.
8. **Licença:** como você quer que as pessoas usem seu código-fonte, uma
   vez que ele vier a público? Pode deixar este campo inalterado para
   este tutorial.

Clique no botão após realizar a configuração.

Feito isso, você pode seguir o :ref:`fluxo normal <resolvendo-conflitos>` de
trabalho do git.

.. |image0| image:: ../imagens/create_1.png
