![gimme meme](./gimme.png){width=200px}

<em>"Forsooth, we must rebase. Pray thee, direct me to thy spaghet"</em>

<em>- ye olde fullstack dev, circ. 2005</em>


# Gimme: The Multi-Repo Manager

This is a utility designed to help developers quickly hop between and manage multiple local repositories. The main utility of this CLI is jumping between repos with the base command, `gimme [repo]`, but it also provides a few other simple quality of life features.

Check out `gimme -h` for more info.

## Table of Contents
- [Setup](#Setup)
  - [Prerequisites](#Prerequisites)
  - [Installation](#Installation)
  - [Basic Usage](#Basic Usage)

## Setup

### Prerequisites
Make sure you have `pipx` and `python ^3.8` installed. If you don't you can install them with your favorite package mananger (brew, apt, pip+pyenv, etc).

```
~$ sudo brew install pipx python3
```

### Installation

Install `gimmetool` using `pipx`:
```
~$ pipx install gimmetool
```

Then run first-time setup:
```
~$ sudo gimme init
where do all of your repositories live (default: ~/)? ~/code
shell config file [~/.zshrc]:
Initialization successful. Restart your shell to begin.
~$
```

After gimme is initialized, you will need to restart your terminal or re-`source` your shell configs:

```
~$ source ~/.zshrc
```

### Basic Usage.

Now, you should be ready to go:
```
~$ gimme --version
output: <version number>
```

Try jumping from any directory to your favorite local repository.

```shell
# jumps from ~/ directly to your repo!
~$ gimme frontend
~/code/frontend$ 

# also supports partial matching
~$ gimme back 
~/code/backend$
```

## Other Tools
There are a few other tricks `gimme` has up its sleeve. Some help streamline jumps between your most common repos. Others help manage and prune large sets of repositories.

### Favorites

Let's say you have the following repos:
```shell
/Users/bob/code/
- lib-login/
- lib-log/
- logger/
```

But you spend most of your time in `logger.`
Jumping with `gimme log` might result in a jump to a repo you don't actually want to be in: 

```shell
~$ gimme log
~/code/lib-login$ # really? >:(
```

But, by adding the repo you want as a favorite, `gimme` will prioritize it.

```
gimme config add favorite /User/bob/code/logger
```

Now, the jump is unambiguous:

```shell
~$ gimme log
~/code/logger$ # :D
```

### Aliases

Sometimes, there are repos with longer names that you'd rather not change, but that you'd also rather not type out.

```shell
/User/bob/code/legacy-backend-2013
```

You can create an alias that maps a shortcut to a more specific search.

```shell
~$ gimme config add alias back2018 legacy-backend-2018
```

Now, you don't have to be as specific with your jumps to get to the repo you want, and you don't have to change the name of the directory and inevitably forget the name of the remote origin it actually belongs to.

```shell
~$ gimme back13
~/code/legacy-backend-2013$ 
```

### Listing Repositories

Gimme also lets you list all repositories and reports on what branches exist in them locally.

```
~$ gimme list (or gimme ls)
/Users/bob/code:
    my-backend
      * master
      - dev
      - working-branch
    my-frontend
      - new-homepage
      * main
      - temp-wip-changes
    my-database
      * main
```

### Mass Updates

A little tired of having to pull multiple times on a bunch of separate repos? `gimme` will update the default branch of every repo in your groups!

```
~$ gimme updates
- Updating 'my-backend'...done
- Updating 'my-frontend'...done
- Updating 'my-database'...done
...
```
