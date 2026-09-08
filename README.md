# MatCalc Documentation

## Install prerequisites

`pip install -r requirements.txt`

## Serve locally for development

`mkdocs serve`

To develop the documentation locally using the built-in HTTP server of `mkdocs` is recommended.
Just start it with `mkdocs serve`, visit the `localhost` website it tells you and watch it
reload automatically on changes to source files. Source files are located in the `src` folder.

## Build static website (for publishing)

`mkdocs build`

When you are finished you need to create the files you want to host. Just issue a `mkdocs build`
and the output folder `docs` will be updated. `docs` is the folder which gets hosted via GitHub
Pages.

After that you can commit and push, it will take some minutes until your changes will be public.