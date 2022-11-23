: _guia-rapido

Guia rápido
-----------

O fluxo de trabalho mais comum quando trabalhamos com git é o seguinte:

**Nota:** Para resolver conflitos, confira :ref:`este tutorial.<resolvendo-conflitos>`

.. mermaid::

   flowchart TD; 

   entrou[Entrou em\num repositório]
   clone[git clone]
   add[git add]
   commit[git commit]
   pull[git pull]
   push[git push]
   collab{colaborativo?}
   conflict{conflitos?}
   solve(resolver)
   branches_1{usando\nbranches?}
   branches_2{usando\nbranches?}
   work_on_code(desenvolve\ncódigo)
   merge_text(junta branches\ncom git merge)

   entrou --> clone --> 
   branches_1 -- sim --> branch_text(cria branch com\n git checkout) --> work_on_code
   branches_1 -- não --> main_text(continua na\nbranch main) --> work_on_code --> add

   branches_2 -- sim --> merge_text

   add --> commit  --> 
   collab -- não --> branches_2  
   collab -- sim --> pull --> 
   conflict -- sim --> solve --> add
   conflict -- não --> branches_2
   merge_text --> push 
   branches_2 -- não --> push
