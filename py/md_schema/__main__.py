import sys

import markdown2
import lxml.etree
from lxml.etree import fromstring
import cssselect



class Parser:
    def __init__(self, schema_dict):
        self.schema_dict = schema_dict

    def parse(self, markdown):
        res = {}

        html = markdown2.markdown(markdown).rstrip()
        html_parsable = '<div>'+html+'</div>'
        document = lxml.etree.fromstring(html_parsable)
        for schema_elem in self.schema_dict:
            if schema_elem['type'] == 'titlearea':
                elem_xpath = cssselect.GenericTranslator().css_to_xpath(schema_elem['selector'])
                text_xpath = elem_xpath + '/following::p[1]'
                found_elems = [e for e in document.xpath(elem_xpath)]
                found_texts = [e.text for e in document.xpath(text_xpath)]

                res_key = schema_elem['name']
                title = found_elems[0].text
                res[res_key] = {
                    'title': title,
                    'description': found_texts[0]
                }
            elif schema_elem['type'] == 'list':
                elem_xpath = cssselect.GenericTranslator().css_to_xpath(schema_elem['selector'])
                text_xpath = elem_xpath + '/following::p[1]'
                found_elems = [e for e in document.xpath(elem_xpath)]
                found_texts = [e.text for e in document.xpath(text_xpath)]

                res_key = schema_elem['name']
                title = found_elems[0].text
                res[res_key] = {
                    'title': title,
                    'description': found_texts[0]
                }
        return res

def main():
    print(sys.argv)

if __name__ == "__main__":
    main()
