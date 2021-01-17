# Related Work

This lists other alternatives.


## [md-to-json](https://www.npmjs.com/package/md-2-json)

> https://github.com/ajithr/md-2-json

### Example

#### Simple content

```js

var md2json = require('md-2-json');

md2json.parse('This is a markdown content');

/* output
{
    raw: "This is a markdown content\n"
}
*/

```

#### Multiline Content

```js

var md2json = require('md-2-json');
var mdContent = `
# Heading 1

This is a para

- This is a list

## Heading 2

This is a para
`

md2json.parse(mdContent);

/* output
{
    "Heading 1": {
        raw: "This is a para\n - This is a list\n",
        "Heading 2": {
            raw: "This is a para\n"
        }
    }
}
*/

```

## [md2json](https://www.npmjs.com/package/@jackens/md2json)

Code repository is 404

## [md-to-json](https://github.com/PatternPedia/md-to-json)

Input: test.md

```markdown
# Name
My name

# Attributes
- Color Vision
- Hair on Head

# MDCode
      My name __is__ md:
      - A
      - B
      - C

# End Tag
Text

# Empty
```

Output: `test.json`

```json
{
  "Name": "My name",
  "Attributes": [
    "Color Vision",
    "Hair on Head"
  ],
  "MDCode": "My name __is__ md:\n- A\n - B\n- C",
  "End_Tag": "Text",
  "Empty": ""
}
```
