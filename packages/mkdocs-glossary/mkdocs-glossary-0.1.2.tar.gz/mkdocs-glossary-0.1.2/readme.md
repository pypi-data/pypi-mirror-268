# mkdocs-glossary

A MkDocs plugin that automatically creates references to glossary terms within italicized text from a specified glossary list file.

## Setup

### Installing using pip:

`pip install mkdocs-glossary`

## Config

You need to activate the plugin in `mkdocs.yml`:

``` yaml
plugins:
  - glossary:
      file: "file_name" # Optional --> Default : glossary.md
      exclude: # Optional --> Default : None
        - 'excluded term A'
        - 'excluded term B'
        - '...'
      unknown_warning: true # Optional --> Default : false
```

- `file` - The filename, from docs root folder, of the `Markdown` file containing the glossary list.
- `exclude` - This is a list of all the terms, case insensitive, that you want the plugin to ignore.
- `unknown_warning` - This option allow the plugin to create warning on founded term that are not in glossary list or exclude list.

## Usage

### How it work

The plugin will look for `Markdown` *italic* text. It will ignore italic placed in headers, links text, images alt text, code and code blocks. It will then check if the text is part of the glossary list from the glossary file and create a reference next to the text.

To create that reference to the definition it will use a superscript number inside a `Markdown` link element. To correctly render superscript this plugin require a way to render them. I recommend using `pymdownx.caret` markdown extension via `mkdocs-material`.

You can set the `pymdownx.caret` markdown extension like this in your `mkdocs.yml`.

``` yaml
markdown_extensions:
  - pymdownx.caret
```

Using the command `mkdocs build` or `mkdocs serve` will trigger the plugin.

### Glossary list

For the glossary list inside the glossary file you have to respect this format

First, create a `Markdown` ordered list like in the usual way.

``` markdown
1. Something
2. Something else
```

Secondly place each terms between `Markdown` bold characters. you can separate variantes that have the same description by using comma.

``` markdown
1. **Term A**
2. **Term B, Variant B1**
```

Finnaly you can add your description the same way you would write any text just after a space, a colon and another space

``` markdown
1. **Term A** : Term A Description
2. **Term B, Variant B1** : *Term B* **Important Descripiton** See : [link](.)
```

### About `Extended Markdown Definition List`

I'm aware of the `Extended Markdown Definition List` element but it's supposed to generate a definition at the end of a page/document and since i don't want to interfere with any plugins that would use it the proper way i had to come up with another way to write and read the glossary list.

### Notes

Note that most `Markdown` interpreter will automaticaly manage numbers or ordered list so it have no importance if you use accurate number on the glossary list. The plugin just do a simple increment at each new entry.

Be aware that multiple ordered list that follow the glossary list rules would work but would create confusion with user since the numbers shown on the glossary lists would not correspond to the ones used by the plugin to reference terms in the documentation.

By the way any italic words contained in the glossary file will be ignored by the plugin.

## License

This project is under MIT license. See the `license` file for more details.

## See Also

- [GitLab Repo](http://www.gitlab.org/cfpt-mkdocs-plugins/mkdocs-glossary/)
- [MkDocs Website](http://www.mkdocs.org/)
- [MkDocs-Material Documentation](https://squidfunk.github.io/mkdocs-material/)