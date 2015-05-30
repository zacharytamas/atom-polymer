# atom-polymer

Develop for Polymer 1.0+ faster with Atom.

## Snippets

**Note:** The majority of the initial snippets are borrowed from [Rob Dodson's excellent `polymer-snippets` package](https://github.com/robdodson/Atom-PolymerSnippets) and adapted for a Polymer 1.0+ world.

### HTML imports

#### [hii] Import Iron element

    <link rel="import" href="${1:bower_components}/iron-$2/iron-$2.html">

#### [hip] Import Paper element

    <link rel="import" href="${1:bower_components}/paper-$2/paper-$2.html">

#### [hi] Import generic element

    <link rel="import" href="${1:bower_components}/${0}/${0}.html">

### New element boilerplates

#### [pe] Polymer element with template and style

    ${1:<link rel="import" href="../polymer/polymer.html">}

    <dom-module id="$2">
      <style>
        :host {
          display: block;
        }
      </style>
      <template>
        $4
      </template>
    </dom-module>

    <script>
      Polymer({
        is: '$2',
        $3
      });
    </script>

#### [pen] Polymer element without template

    <script>
      Polymer({
        is: '$1',
        $2
      });
    </script>
