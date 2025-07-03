class Album:

    def __init__(self, id, title, release_year, artist_id):
        self.id = id
        self.title = title
        self.release_year = release_year
        self.artist_id = artist_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Album({self.id}, '{self.title}', {self.release_year}, {self.artist_id})"
    
    def is_valid(self):
        if self.title is None or self.title == "":
            return False
        if self.release_year is None or self.title == "":
            return False
        if self.artist_id is None or not isinstance(self.artist_id, int):
            return False
        return True

    def generate_album_errors(self):
        errors = []
        if self.title is None or self.title == "":
            errors.append("Please input a title")
        if self.release_year is None or self.title == "":
            errors.append("Please input a release year")
        if len(errors) == 0:
            return None
        else:
            return ", ".join(errors)
