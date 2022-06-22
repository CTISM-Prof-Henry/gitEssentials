## Fazendo fork e pull requests

Essa página é um **esboço.** Ela será aprimorada depois.

Por hora, as instruções necessárias são:

1. Entrar na página do repositório que deseja-se fazer o fork, no github. Vamos 
   chamá-lo de `https://github.com/CTISM-Prof-Henry/gitEssentials`
2. Clicar no botão "fork", no canto superior direito:

![](../imagens/fork_1.png)

3. Confirmar que deseja-se fazer fork na tela que aparecer:

![](../imagens/fork_2.png)

4. Clonar o repositório que foi recém criado (a cópia, não o original) com 
   `git clone`. Por exemplo, se eu, henryzord, fizer um fork do repositório 
   **gitEssentials** (que pertence à conta CTISM-Prof-Henry), a URL do meu 
   repositório copiado será `https://github.com/henryzord/gitEssentials`, e o 
   comando a ser dado é

```bash
git clone https://github.com/henryzord/gitEssentials
```

5. Criar uma nova **branch local**, e mudar para ela: 
   `git checkout -b <nome da branch>`. Supondo que eu queira criar uma nova branch
    de nome **top**, o comando a ser dado é

```bash
git checkout -b top
```

6. Notificar o git de que este repositório relaciona-se com o repositório original:
`git remote add upstream <url do repo original>`. No exemplo, ficaria

```bash
git remote add upstream https://github.com/CTISM-Prof-Henry/gitEssentials
```

7. Fazer as modificações necessárias no código-fonte (editar, deletar ou criar 
   arquivos)
8. Adicionar arquivos com `git add`: `git add .`, por exemplo
9. Salvar modificações com `git commit -m "mensagem"`
10. Dar um `git pull` para atualizar o repositório local com as modificações do 
    repositório remoto original
11. Enviar modificações para o repositório copiado, em uma **branch remota** 
    que será criada, chamada **top**: `git push -u origin top`