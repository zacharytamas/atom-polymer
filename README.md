# atom-polymer

[![Greenkeeper badge](https://badges.greenkeeper.io/zacharytamas/atom-polymer.svg)](https://greenkeeper.io/)

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
<link rel="import" href="${1:../bower_components}/polymer/polymer.html">

<dom-module id="$2">
  <template>
    <style>
      :host {
        $5
      }
    </style>
    $4
  </template>
  <script>
    Polymer({
      is: '$2',
      $3
    });
  </script>
</dom-module>
```

#### [pen] Polymer element without template

```html
<link rel="import" href="${1:../bower_components}/polymer/polymer.html">

<script>
  Polymer({
    is: '$2',
    $3
  });
</script>
```
#### [pes] Polymer element with an external script source

```html
<link rel="import" href="${1:../bower_components}/polymer/polymer.html">

<dom-module id="$2">
  <template>
    <style>
      :host {
        $5
      }
    </style>
    $4
  </template>
  <script src="$3">
  </script>
</dom-module>
```

#### [pet] Polymer element with a template only
This snippet also provides a wrapper div for `<content>` and a style declaration.

```html
<link rel="import" href="${1:../bower_components}/polymer/polymer.html">

<dom-module id="$2">
  <template>
    <style>
      :host {
        $4
      }
      .content-wrapper > ::content {
        $5
      }
    </style>
    $3
    <div class="content-wrapper">
      <content></content>
    </div>
  </template>
</dom-module>
```

### [dom-module] A blank `dom-module` element

This is handy if you need to add a visual presence to a Polymer element that did not necessarily need it before.

```html
<dom-module id="$1">
  <style>
    :host {
      display: block;
    }
  </style>
  <template>
    $2
  </template>
</dom-module>
```

### <template> shortcuts

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
* `paper-checkbox`
* `paper-dialog`
* `paper-drawer-panel`
* `paper-fab`
* `paper-header-panel`
* `paper-icon-button`
* `paper-menu`
* `paper-progress`
* `paper-radio-button`
* `paper-radio-group`
* `paper-ripple`
* `paper-scroll-header-panel`
* `paper-slider`
* `paper-spinner`
* `paper-tabs`
* `paper-toolbar`

### Iron elements

We include snippets of these Iron elements with sensible defaults:

* `iron-ajax`
* `iron-collapse`
* `iron-form`
* `iron-icon`
* `iron-iconset`
* `iron-image`
* `iron-input`
* `iron-localstorage`
* `iron-media-query`
* `iron-pages`

### Gold elements

* `gold-cc-cvc-input`
* `gold-cc-expiration-input`
* `gold-cc-input`
* `gold-email-input`
* `gold-phone-input`
* `gold-zip-input`
