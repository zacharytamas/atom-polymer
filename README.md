# atom-polymer

Develop for Polymer 1.0+ faster with Atom.

## Snippets

**Note:** The majority of the initial snippets are borrowed from [Rob Dodson's excellent `polymer-snippets` package](https://github.com/robdodson/Atom-PolymerSnippets) and adapted for a Polymer 1.0+ world.

### HTML imports

#### [hii] Import Iron element

```html
<link rel="import" href="${1:bower_components}/iron-$2/iron-$2.html">
```

#### [hip] Import Paper element

```html
<link rel="import" href="${1:bower_components}/paper-$2/paper-$2.html">
```

#### [hi] Import generic element

```html
<link rel="import" href="${1:bower_components}/${0}/${0}.html">
```

### New element boilerplates

#### [pe] Polymer element with template and style

```html
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
```

#### [pen] Polymer element without template

```html
<script>
  Polymer({
    is: '$1',
    $2
  });
</script>
```

### `<template>`

#### [tm] Template tag

```html
<template>
  $1
</template>
```

#### [tm-repeat] Repeating template

```html
<template is="dom-repeat" items="{{$1}}">
  $2
</template>
```

#### [tm-if] Conditional template

```html
<template is="dom-if" if="$1">
  $2
</template>
```

### Paper elements

We include snippets of these Paper elements with sensible defaults:

* `paper-button`
* `paper-drawer-panel`
* `paper-tabs`
* `paper-toolbar`

### Iron elements

We include snippets of these Iron elements with sensible defaults:

* `iron-ajax`
* `iron-icon`
