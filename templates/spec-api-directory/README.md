<!-- start header -->
To run this locally, [install Ploomber](https://docs.ploomber.io/en/latest/get-started/quick-start.html) and execute: `ploomber examples -n templates/spec-api-directory`

[![binder-logo](https://raw.githubusercontent.com/ploomber/projects/master/_static/open-in-jupyterlab.svg)](https://binder.ploomber.io/v2/gh/ploomber/binder-env/main?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fploomber%252Fprojects%26urlpath%3Dlab%252Ftree%252Fprojects%252Ftemplates/spec-api-directory%252FREADME.ipynb%26branch%3Dmaster)

Questions? [Ask us on Slack.](https://ploomber.io/community/)

For a notebook version (with outputs) of this file, [click here](https://github.com/ploomber/projects/blob/master/templates/spec-api-directory/README.ipynb)
<!-- end header -->



# Pipeline from a directory

<!-- start description -->
Create a pipeline from a directory with scripts (without a pipeline.yaml file).
<!-- end description -->

## Build

```bash
mkdir output
ploomber build --entry-point '*.py'
```

Output stored in the `output/` directory.


## Describe

This pipeline contains five steps. The last task trains a model and outputs a
report and a model file. To get the pipeline description:

```bash
ploomber status --entry-point '*.py'
```

`--entry-point '*.py'` means "all files with py extension are tasks in the
pipeline". If all the files in the current directory are tasks, you can also
use the shortcut `--entry-point .`.
