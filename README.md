# Python. Organize output. Groups and humans.

---

## 🏠 Homework

Homework related actions.

### ▶️ Run

Make all actions needed for run homework from zero. Including configuration.

```shell
just homework-i-docker-i-run
```

### 🚮 Purge

Make all actions needed for run homework from zero.

```shell
just homework-i-docker-i-purge
```

---

## 🛠️ Development

### Install just

You must have [just] installed on your system for run different commands.

If you don't have [just] installed, you can find commands for installation here:

- [just.just](just/dev/just.just)

After installing [just], you can see all available commands with:

```bash
just --list
```

[just]: https://github.com/casey/just

### Initialize dev

Install dependencies and register pre-commit.

```shell
just init-i-dev
```

### ⚙️ Configure

Configure homework.

```shell
just init-i-configs
```

---

## 🐳 Docker

Use services in dockers.

### ▶️ Run

Just up/run services

```shell
just d-up
```

### 🚮 Purge

Purge all data related to services

```shell
just d-purge
```
