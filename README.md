# omop-cdm

LinkML version of OMOP CDM including OMOP-tuned convention enforcement

![Automated documentation build](https://github.com/SPHERE-Cancer-CAG/omop-link/actions/workflows/deploy-docs.yml/badge.svg)

## Website

[https://sphere-cancer-cag.github.io/omop-link/](https://sphere-cancer-cag.github.io/omop-link/)



## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
  * [omop_cdm](src/omop_cdm)
    * [schema](src/omop_cdm/schema) -- LinkML schema
      (edit this)
    * [datamodel](src/omop_cdm/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests

## Developer Documentation

<details>
To run commands you may use good old make or the command runner [just](https://github.com/casey/just/) which is a better choice on Windows.
Use the `make` command or `duty` commands to generate project artefacts:
* `make help` or `just --list`: list all pre-defined tasks
* `make all` or `just all`: make everything
* `make deploy` or `just deploy`: deploys site
</details>

## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
