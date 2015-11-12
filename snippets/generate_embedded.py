"""This little tool just iterates over all the snippets and generates a file
called "_embedded_exclusions.cson" which effectively cancels all these
snippets when in embedded contexts such as inside <script> and <style> blocks"""

import os
import cson

HTML_SCOPE = ".text.html"
OUTPUT_FILENAME = "_embedded_exclusions.json"
ELEMENT_FAMILIES = ["paper", "iron", "google", "gold"]


def allSnippetsFiles():
  "Yields paths to all snippet files in this directory except our exceptions."
  for subdir, dirs, files in os.walk("."):
    return (f for f in files if f.endswith("cson") and not f.startswith("_"))


def snippetsInFileForScope(file_name, scope=HTML_SCOPE):
  "Returns Snippets in the file which are in the specified scope."
  with open(file_name, "r") as f:
    data = cson.loads(f.read())
  return data.get(HTML_SCOPE, {})


def renderExceptions(snippets):

  for snip in snippets:
    # If the element snippet is for a family of Polymer elements,
    # replace its body with just the name of the snippet. This will
    # let you auto-complete long element names in CSS and JavaScript.
    if snip.get("prefix", "").split("-")[0] in ELEMENT_FAMILIES:
      snip["body"] = snip["prefix"]
    else:
      del snip["body"]

  return cson.dumps({
    ".text.html .embedded": dict((s["prefix"], s) for s in snippets)
  }, indent=2)


if __name__ == '__main__':
  snippets = []
  for snippet_file in allSnippetsFiles():
    snippets.extend(snippetsInFileForScope(snippet_file).values())

  with open(OUTPUT_FILENAME, "w") as f:
    f.write(renderExceptions(snippets))
