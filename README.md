# GitHub Tutorial
Tutorial para os Alunos da UNINOVE

[Cheatsheet GitHub em Português](https://training.github.com/downloads/pt_BR/github-git-cheat-sheet/) - [PDF](https://training.github.com/downloads/pt_BR/github-git-cheat-sheet.pdf)

## Setup

Instalação:
 * MacOS: `brew install git`
 * Linux: `sudo apt-get install git`
 * Windows: `choco install git`

## Comandos

* Configuração
  * `git config --global user.name "[Nome Sobrenome]"`
  * `git config --global user.email "[email valido]"`
* Pulls/Forks
  * `git clone`
  * `git pull`
* Commits
  * `git add arquivos` ou `git add .`
  * `git commit -m "Mensagem do Commit"`
* Pushs
  * `git push -u origin main`
* Logs
  * `HEAD`, `HEAD~` e `HEAD~{n}`
  * `git diff`
  * `git status`
  * `git log` e `git log --graph`
* Branches
  * `git branch` e `git branch [nome-do-branch]`
  * `git checkout [nome-do-branch]`
* Reset
  * `git reset --soft` versus `git reset --hard`
* Pull Requests
  * `git push -u origin [nome-do-branch]`
* Merging no Master/Main
* GitHub Actions
