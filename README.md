# `pygithub-playground`

## About
A playground, demonstrating how to use [PyGithub](https://github.com/PyGithub/PyGithub) with [GitHub Apps](https://docs.github.com/en/developers/apps/creating-a-github-app).

## Setup
**Install dependencies**

On macOS:

```shell
brew bundle
```

:warning: If this is the first time using `direnv`, be sure to [hook `direnv` into your shell](https://direnv.net/docs/hook.html).

**Setup environment**

Create a `.envrc` file from [the example provided](.envrc.example) and follow [the included directions](.envrc.example) to populate the required environment variables.

```shell
# populate .envrc
cp .envrc.example .envrc
```

## Run the demo
```shell
pipenv run python demo.py
```
