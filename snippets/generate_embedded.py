"""This little tool just iterates over all the snippets and generates a file
called "_embedded_exclusions.cson" which effectively cancels all these
snippets when in embedded contexts such as inside <script> and <style> blocks"""

import os
import cson

HTML_SCOPE = ".text.html"
OUTPUT_FILENAME = "_embedded_exclusions.json"


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
  return cson.dumps({
    ".text.html .embedded": dict(
      (s["prefix"], {
        "prefix": s["prefix"]
      }) for s in snippets)
  }, indent=2)


if __name__ == '__main__':
  snippets = []
  for snippet_file in allSnippetsFiles():
    snippets.extend(snippetsInFileForScope(snippet_file).values())

  with open(OUTPUT_FILENAME, "w") as f:
    f.write(renderExceptions(snippets))
