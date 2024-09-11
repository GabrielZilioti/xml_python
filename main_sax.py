import xml.sax  # Used to load pieces of an XML file to the RAM, it's useful for big files or a limited resources env


class BooksHandler(xml.sax.ContentHandler):

    def startElement(self, name, attrs):
        self.current = name
        if name == "book":
            print(f"-- Book {attrs['id']} --")

    def characters(self, content):
        if self.current == "author":
            self.author = content
        elif self.current == "title":
            self.title = content
        elif self.current == "genre":
            self.genre = content
        elif self.current == "price":
            self.price = content
        elif self.current == "publish_date":
            self.publish_date = content
        elif self.current == "description":
            self.description = content

    def endElement(self, name):
        if self.current == "author":
            print(f"Author: {self.author}")
        elif self.current == 'title':
            print(f"Title: {self.title}")
        elif self.current == 'genre':
            print(f"Genre: {self.genre}")
        elif self.current == 'price':
            print(f"Price: {self.price}")
        elif self.current == 'publish_date':
            print(f"Publish Date: {self.publish_date}")
        elif self.current == 'description':
            print(f"Description: {self.description}")


handler = BooksHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse("xml_files/books.xml")
