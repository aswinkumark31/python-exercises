class book:
    def setd(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
    def getd(self):
        print('title is ',self.title)
        print('author is ',self.author)
        print('page number ',self.pages)
ob=book()
ob.setd(input('enter a title:'),input('enter a author:'),int(input('enter a number')))

ob.getd()