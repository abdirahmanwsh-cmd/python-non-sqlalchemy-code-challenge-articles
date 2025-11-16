class Article:
    all = []

    def __init__(self, author, magazine, title):
      
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("title must be a string length 5..50")
        self._title = title

        
        self._author = None
        self._magazine = None
        self.author = author
        self.magazine = magazine

        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        
        return

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
       
        from classes.many_to_many import Author  
        if isinstance(value, Author):
            self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        from classes.many_to_many import Magazine
        if isinstance(value, Magazine):
            self._magazine = value


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("name must be a non-empty string")
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        
        return

    def articles(self):
        
        return [a for a in Article.all if a.author == self]

    def magazines(self):
        
        mags = [a.magazine for a in self.articles() if a.magazine is not None]
        
        seen = set()
        unique = []
        for m in mags:
            if m not in seen:
                seen.add(m)
                unique.append(m)
        return unique

    def add_article(self, magazine, title):
        
        return Article(self, magazine, title)

    def topic_areas(self):
        mags = self.magazines()
        if not mags:
            return None
        cats = [m.category for m in mags]
        
        seen = set()
        unique = []
        for c in cats:
            if c not in seen:
                seen.add(c)
                unique.append(c)
        return unique


class Magazine:
    all = []

    def __init__(self, name, category):
        
        self._name = None
        self._category = None
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    def articles(self):
        return [a for a in Article.all if a.magazine == self]

    def contributors(self):
        authors = [a.author for a in self.articles() if a.author is not None]
        seen = set()
        unique = []
        for au in authors:
            if au not in seen:
                seen.add(au)
                unique.append(au)
        return unique

    def article_titles(self):
        arts = self.articles()
        if not arts:
            return None
        return [a.title for a in arts]

    def contributing_authors(self):
        authors = self.contributors()
        if not authors:
            return None
        result = []
        for au in authors:
            count = sum(1 for a in Article.all if a.author == au and a.magazine == self)
            if count > 2:
                result.append(au)
        return result if result else None

pass