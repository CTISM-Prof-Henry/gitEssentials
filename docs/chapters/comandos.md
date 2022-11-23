# Comandos

## Sumário

* [Comandos do sistema operacional](#comandos-do-sistema-operacional)
    * [Acessar um novo diretório](
    #acessar-um-novo-diretório)
    * [Listar arquivos em um diretório](
    listar-arquivos-em-um-diretório)
    * [Limpar tela](#limpar-tela)
    * [Abrir uma janela do navegador de arquivos](#abrir-uma-janela-do-navegador-de-arquivos)
* [Comandos do git](#comandos-do-git)
    * [git clone](#git-clone)
    * [git status](#git-status)
    * [git add](#git-add)
    * [git restore](#git-restore)
    * [git commit](#git-commit)
    * [git push](#git-push)
    * [git pull](#git-pull)
    * [git branch](#git-branch)
    * [git checkout](#git-checkout)

### Comandos do sistema operacional

#### Acessar um novo diretório

Windows, Linux:

```bash
cd <diretório> 
```

Exemplo:

```bash
cd Downloads
```

#### Listar arquivos em um diretório

Windows:

```bash
dir <diretório>
```

Linux:

```bash
ls <diretório>
```

Exemplo:

Windows: 

```bash
dir
dir Downloads
```

Linux:

```bash
ls 
ls Downloads
```

#### Limpar tela

Exemplo:

Windows:

```bash
cls
```

Linux:

```bash
clear
```

#### Abrir uma janela do navegador de arquivos

Windows:

```bash
explorer <parâmetro>
```

Linux:

```bash
nautilus <parâmetro>
```

Exemplo:

Windows: 

```bash
explorer .
explorer Downloads
```

Linux:

```bash
nautilus .
nautilus Downloads
```

#### Comandos do git

Esta seção apresenta apenas um **resumo** sobre os comandos do git.
Cada um destes comandos possui muito mais parâmetros e funções do que as listadas
aqui, porém espera-se que este resumo seja suficiente para o andamento do curso.

**Nota 1:** é preciso estar dentro de uma pasta que é um repositório git para 
estes comandos funcionarem.

**Nota 2:** Alguns destes comandos (marcados com o símbolo 🟦) dependem do 
**estado atual** do repositório, que pode ser consultado com um 
[git status](#git-status). Em outras palavras, se você der este comando fora da 
sequência correta, ele não terá o efeito desejado. Por outro lado, os comandos
que **não dependem de estado** são relativamente inofensivos caso foram usados
fora da ordem correta.

#### git clone

**Copia** um repositório remoto para a máquina local, **se o repositório não 
existir na máquina local.** Não confundir com a funcionalidade do 
[git pull](#git-pull).

Sintaxe: 

```bash
git clone <url do repositório>
```

Exemplo:

```bash
git clone https://github.com/CTISM-Prof-Henry/gitEssentials
```

#### git status

Mostra o status do repositório na máquina local.

Sintaxe e exemplo:

```bash
git status
```

#### git add

🟦 Adiciona arquivos à lista de modificações-candidatas a serem salvas. Não 
confundir com a funcionalidade do [git commit](#git-commit).

Sintaxe:

```bash
git add <parâmetro>
```

Exemplo: 

```bash
git add .  # adiciona todos os arquivos da pasta atual
git add *  # adiciona todos os arquivos da pasta atual
git add README.md  # adiciona apenas o arquivo README.md
git add README.md main.py estilo.css  # adiciona uma lista de arquivos
```

#### git restore

Descarta modificações que foram feitas em um arquivo.

Sintaxe:

```bash
git restore <parâmetro>
```

Exemplo:

```bash
git restore README.md  # descarta modificações que foram feitas no README.md
git restore .  # descarta modificações que foram feitas nos arquivos da pasta atual
```

#### git commit

🟦 **Salva** as modificações feitas no repositório local, em um checkpoint (também
chamado de commit).

**Nota:** só pode ser utilizado após um [git add](#git-add).

Sintaxe e exemplo: 

```bash
git commit -m "mensagem explicando o que foi feito neste commit"
```

#### git push 

🟦 **Uso 1:** Envia modificações da atual branch local para uma branch do repositório 
remoto, dado que as modificações já foram salvas.

**Nota 1:** só pode ser utilizado após um [git commit](#git-commit).

**Nota 2:** é uma boa prática ser precedido por um [git pull](#git-pull).

**Nota 3:** caso você esteja trabalhando em um repositório que é uma cópia de
outro repositório (vide [Fazendo fork e pull requests](
chapters/fork_pull_request.md)), você deve adicionar a flag `-u` ao comando.

Sintaxe: 

```bash
git push origin <nome da branch remota>
```

Exemplo:

```bash
git push origin main  # envia para a branch remota main
git push origin top  # envia para a branch remota top
git push origin -u top  # envia para a branch remota top que referencia outro repo
```

**Uso 2:** deleta uma branch remota. Veja [git branch](#git-branch) para ver
como deletar uma branch local.

Sintaxe:

```bash
git push origin --delete <nome da branch remota>
```

Exemplo:

```bash
git push origin --delete top  # deleta a branch remota top
```

#### git pull

🟦 **Baixa** as modificações da branch de um repositório remoto para a atual branch
da máquina local, **se o repositório já existir na máquina local.** Não confundir 
com a funcionalidade do [git clone](#git-clone).

Sintaxe:

```bash
git pull origin <nome da branch remota>
```

Exemplo:

```bash
git pull origin main  # baixa da branch remota main
git pull origin top  # baixa da branch remota top
```

#### git checkout

🟦 Muda de uma branch local para outra.

Sintaxe:

```bash
git checkout <nome da branch local>
```

Exemplo:

```bash
git checkout top  # troca da branch atual para a branch top
git checkout main  # troca da branch atual para a branch main
```

#### git branch 

🟦 **Uso 1:** lista as branches locais.

Sintaxe e exemplo:

```bash
git branch
```

**Uso 2:** deleta uma branch local. Veja [git push](#git-push) para deletar
uma branch remota.

**Nota:** tenha certeza que você **não está dentro da branch que será deletada.**
Veja [git checkout](#git-checkout) para ver como trocar de uma branch para 
outra.

Sintaxe:

```bash
git branch -d <nome da branch local>
```

Exemplo:

```bash
git branch -d top  # deleta a branch local top
```