class Ligne():
    def __init__(self):

        self.note_container = []

        for i in range(42):
            self.note_container.append('-')
        
    def addNote(self, note, position):
        print("note", note, "position", position)
        liste  = list(range(25))
        if note in liste:
            self.note_container[position] = str(note)
            print(self.note_container)
        else : 
            print("La note n'est pas valide")
        
    

    
    
   