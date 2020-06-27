#!/usr/local/bin/python3



class XMLParser:

    def __init__(self,xml):
        self.xml = xml
        self.index = 0
        self.map = {}
        self.tokens = []

    def raiseException(self, message):
        print(self.tokens)
        raise Exception(message)

    def getTokenForString(self, string):
        if not string in self.map:
            self.map[string] = len(self.map)+1
        return self.map[string]

    def currenChar(self):
        return self.xml[self.index]

    def nextChar(self):
        if self.index + 1 < len(self.xml):
            return self.xml[self.index + 1]
        return None

    def isParsing(self):
        return self.index < len(self.xml)

    def moveIndex(self):
        self.index += 1
        return self.isParsing()

    def isCurrentWhiteSpace(self):
        return self.currenChar().isspace()

    def parseWhiteSpace(self):
        while self.isParsing() and self.currenChar().isspace():
            self.moveIndex()
        return self.isParsing()

    def parseString(self):
        string = ''
        while self.isParsing() and self.currenChar().isalpha():
            string += self.currenChar()
            self.moveIndex()
        return string


    def parseAttribute(self):

        string = self.parseString()
        token = self.getTokenForString(string)
        self.tokens.append(token)

        if self.currenChar() != '=':
            self.raiseException('')
        self.moveIndex()
        if self.currenChar() != '"':
            self.raiseException('')
        self.moveIndex()

        string = ''
        while self.isParsing() and self.currenChar() != '"':
            string += self.currenChar()
            self.moveIndex()
        self.moveIndex()
        self.tokens.append(string)

        return self.isParsing()

    def parseTagStart(self):
        if self.currenChar() != '<':
            return

        self.moveIndex()

        tagName = self.parseString()
        token = self.getTokenForString(tagName)
        self.tokens.append(token)

        self.parseWhiteSpace()

        while self.currenChar() != '>':
            self.parseAttribute()
            self.parseWhiteSpace()

        self.moveIndex()
        self.tokens.append(0)

        return tagName

    def parseTagEnd(self, tagName):
        if self.currenChar() != '<':
            self.raiseException('1')
        self.moveIndex()
        if self.currenChar() != '/':
            self.raiseException('2')
        self.moveIndex()

        string = self.parseString()

        if string != tagName:
            self.raiseException('Invalid tag name. Expected "%s" and received "%s"' % (tagName, string))

        self.parseWhiteSpace()
        if self.currenChar() != '>':
            self.raiseException('3')
        self.moveIndex()
        self.tokens.append(0)
        return self.isParsing()

    def parseElement(self):
        tagName = self.parseTagStart()
        self.parseXML()
        self.parseTagEnd(tagName)

    def parseXML(self):
        while self.isParsing():
            self.parseWhiteSpace()
            if self.currenChar() == '<':
                if self.nextChar() == '/':
                    return self.isParsing()
                else:
                    self.parseElement()
            else:
                string = ''
                while self.isParsing() and self.currenChar() != '<':
                    string += self.currenChar()
                    self.moveIndex()
                self.tokens.append(string)

    def parse(self):
        self.parseXML()
        return self.tokens





# <family lastName="McDowell" state="CA">
#     <person firstName="Gayle">Some Message</person>
# </family>

testcases = [
    'Some Message',
    '<family lastName="McDowell" state="CA">Some Message</family>',
    '<family lastName="McDowell" state="CA"></family>',
    '<family lastName="McDowell" state="CA"></family><family lastName="McDowell" state="CA"></family>',
    '<family lastName="McDowell" state="CA"><person firstName="Gayle">Some Message</person></family>',
    '<family lastName="McDowell" state="CA"><person firstName="Gayle"><span>Some Message</span></person></family>',
]

for testcase in testcases:
    print('====================')
    print(testcase)
    print()
    xmlParser = XMLParser(testcase)
    print(xmlParser.parse())