fs = require 'fs'
hyd = require 'hydrolysis'
path = require 'path'

tags = {}

hyd.Analyzer.analyze('../../github/finance-core/fin-fv.html')
    .then (analyzer) ->

      for tagName, value of analyzer.elementsByTagName
        tags[tagName] =
          attributes: value.properties
            .map (prop) -> prop.name if not prop.private
            .filter (name) -> name is not null

      completions =
        tags: tags

      fs.writeFileSync(path.join(__dirname, 'completions.json'),
        "#{JSON.stringify(completions, null, 2)}\n")
