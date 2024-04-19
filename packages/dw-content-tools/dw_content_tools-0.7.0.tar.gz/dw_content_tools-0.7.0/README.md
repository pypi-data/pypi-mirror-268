# Content CLI Tools

## Installation

```
$ pip3 install dw-content-tools
```

## Module Repository Validator

```
Validates that a module repo structure and content is valid, based
on the following rules:

* metadata.yml exists
* metadata.yml is valid
    * validate JSON schema
* docker-compose.yml exists
* docker-compose.yml is valid
    * validate JSON schema
* english.md exists
* validating english.md:
    * pages:
        * unique IDs
        * all pages contain a valid ID
        * all pages have a name
    * all images referenced in md exist as static files
    * activities:
        * all activities have an unique `id`
        * all activities have `type` defined
        * input:
            * has required `correct-answer` tag
        * multiple-choice:
            * has required `answer` (many) tags
            * at least one answer is marked as `is-correct`
            * when more than one answer is correct, `widget` has to be `checkbox`
        * code:
            * `template` and `device` attrs are defined
            * has required `validation-code` tag
```
