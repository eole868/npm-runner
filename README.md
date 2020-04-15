# flowci-plugin-npm

## Description

Run npm (cnpm) command, and upload html output report

## Inputs

- `FLOWCI_GIT_REPO`: git repo name
- `NPM_CMD`: npm command to run, for example: npm install, cnpm run test
- `NPM_REPORT_PATH` (optional): the relative path in project, for example `./coverage` if upload `coverage` directory

## How to use it

```yml
envs:
  FLOWCI_GIT_URL: "https://github.com/hexojs/hexo.git"
  FLOWCI_GIT_BRANCH: "master"
  FLOWCI_GIT_REPO: "hexo"

steps:
  - name: clone
    plugin: "gitclone"
    allow_failure: false

  - name: npm install
    docker: # optional, can be run from node:12 image
      image: node:12
    envs:
      NPM_CMD: "npm install"
    plugin: "npm-runner"
```

## Screenshot

### nyc test coverage report

![](https://raw.githubusercontent.com/gy2006/flowci-plugin-npm/master/screenshot/report.png)