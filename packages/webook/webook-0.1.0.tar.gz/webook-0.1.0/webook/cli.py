
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-H", "--headless", action="store_true", dest="headless", help="Use headless mode of the browser", default=False)
parser.add_option("-u", "--url-file", dest="url_file", help="A markdown file containing URLs to download", metavar="URL_MARKDOWN_FILE")
parser.add_option("-d", "--delete-element-file", dest="delete_element_file", help="A JSON file contains CSS selectors of which elements to delete", metavar="DELETE_ELEMENT_JSON_FILE")
parser.add_option("-c", "--cover", dest="cover", help="Cover page, local image file or an URL of an image", metavar="COVER_IMAGE", default=None)
parser.add_option("-o", "--output", dest="output_file", help="The output file", metavar="OUTPUT_FILE")

(options, args) = parser.parse_args()

if not options.url_file:
    print("URL_MARKDOWN_FILE is required\n")
    parser.print_help()
    exit(1)


if not options.output_file:
    print("OUTPUT_FILE is required\n")
    parser.print_help()
    exit(1)


if not options.delete_element_file:
    print("DELETE_ELEMENT_JSON_FILE is required\n")
    parser.print_help()
    exit(1)