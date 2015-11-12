## 0.12.0 - Add auto-completion to embedded contexts.
* This makes `atom-polymer` smart enough to not auto-complete whole HTML structures in `<style>` tags, which it did before.
* Now will just auto-complete the *name* of the element, which is really handy when writing selectors for long element names.

## 0.11.0 - Add Gold snippets
* Added snippets for all `gold` elements from Polymer.

## 0.10.0 - Format tweaks
* Updates to documentation. Thanks @jreut!
* Fix problem with `paper-icon-button` snippet. (There was an extra quotation mark.)
* Move `<style>` tag inside `<template>` in all snippets. (@jreut)
* Optionally add `bower_components` to default path when Polymer is imported in the Polymer Element snippets. (@jreut)
* Add a snippet for Polymer Elements with only style and template. (@jreut)

## 0.9.0 - Whoops
* A glitch in `apm` caused me to accidentally skip this version.
* I tried to publish a new minor version without a token and it incremented the version number before it realized the problem. When I added the token and tried to publish again it bumped the version AGAIN, skipping this one.

## 0.8.1 - CSON escaping issue
* Fixed silly but tragic CSON escaping issue. Thanks to @clintwood !

## 0.8.0 - Add more snippets.
* Added `iron-collapse`, `iron-iconset`, `iron-input`, `iron-localstorage`, and `iron-media-query`.
* Added `paper-menu`, `paper-progress`, `paper-radio-button`, `paper-radio-group`, `paper-ripple`, `paper-slider`, and `paper-spinner`.

## 0.7.1 - Add trailing commas to JS snippets.
* It is statistically much more likely you want a trailing comma than you don't.

## 0.7.0 - Adding more snippets.
* A first! Added JS snippets for: Polymer's DOM wrapper, Polymer element declaration, Polymer properties shortcut, and Polymer lifecycle hooks.
* Added `paper-input` and `paper-material` snippets.

## 0.6.0 - Adding more snippets.
* Added `paper-icon-button`, `paper-checkbox`, `paper-dialog`, `paper-textarea`, `paper-input-error`, and `paper-fab` snippets.
* Added `iron-image` and `iron-form` snippets.

## 0.5.0 - Adding more snippets.
* Added `paper-scroll-header-panel`, `paper-header-panel`, `paper-input-container`, and `paper-textarea` snippets.
* Added `iron-pages` snippet.

## 0.4.1 - Fix bug where sometimes snippets didn't register.

## 0.4.0 - Adding more snippets
* Added `paper-tabs`, `paper-toolbar`, `paper-button` snippets.
* Added `iron-ajax` and `iron-icon` snippets.
* Added `dom-module` snippet.
* Reorganized snippets files.
* Big thanks to @daiying-zhang for contributing snippets!

## 0.3.0 - Adding more Polymer elements as snippets
* Added `google-feeds` snippet.
* Added `tm`, `tm-repeat`, and `tm-if` snippets.
* Added `paper-drawer-panel` snippet.

## 0.2.0 - First Release
* Adding initial snippets, see `README.md` for descriptions.
