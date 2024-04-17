"""The kardb class provides a file-based database management system for JSON data.
It handles document creation, deletion, renaming, and updating. With methods for loading, saving, and manipulating data, 
it offers a simple interface for managing database files within specified directories.
"""

import json
import os


# KARDB CLASS

class kardb:

    """The kardb class which contains all methods the data at (self.data). The default document is 'main.json' which is created
    when class is initialized. You can start storing data without creating a doc.

    Attributes:
        data (dict): The place where the data of the current document is held.
        dbname (TYPE): The name of the database.
        docname (str): The name of the current document.
    """
    
    def __init__(self,dbname):

        """The initialization of the class, the passed name is taken as database name and a folder with that name is created.
        The document is set to be main. Either the directory is created if it does not exists or the file is loaded up.
        
        Args:
            dbname (str): The name of the database.
        """
        self.dbname = dbname
        self.docname = 'main'
        self.data = {}
        self.createdirs()
        self.load()


    def load(self):
        """Loads the current document's data for usage. The data will be {} if the file does not exist.
        """
        filepath = f'{self.dbname}/{self.docname}.json'

        if os.path.exists(filepath):
            with open(filepath,'r') as f:
                data = json.load(f)

            self.data.clear()
            self.data.update(data)

        else:
            self.data.clear()


    def save(self,indent=3):
        """Saves the current data of the document as local JSON file.
        
        Args:
            indent (int, optional): The indentation for the JSON file.
        """
        filepath = f'{self.dbname}/{self.docname}.json'

        with open(filepath,'w') as f:
            json.dump(self.data,f,indent=indent)


    def createdirs(self):
        """This function is to create the directory so that the documents can be saved in there.
        """
        directory = os.path.dirname(f'./{self.dbname}/')

        if directory and not os.path.exists(directory):
            os.makedirs(directory)
            

    def getdirs(self):
        """This function can be used to get the current place where the database is located.
        
        Returns:
            TYPE: The directory of the database folder.
        """
        directory = os.path.dirname(f'./{self.dbname}/')

        return directory


    def createdoc(self,docname):
        """Creates a document with the passed arg as name. This will contain empty dictionary.
        
        Args:
            docname (str): Name of the document you want.
        """
        data = {}
        path = f'{self.dbname}/{docname}.json'

        with open(path,'w') as f:
            json.dump(data,f)


    def changedoc(self,docname,save=True):
        """Changes from current working document to specified document. Also loads up the data from that doc. The document is
        also saved before changing. If you want to disable this you can do so by passing 'save=False' in arg.
        
        Args:
            docname (str): Name of the doc you want to work on.
        """
        if save:
            self.save()

        self.docname = docname

        self.load()


    def cacdoc(self,docname):
        """Convenience method to create and change to a new document simultaneously.
        
        Args:
            docname (str): The name of the document you want to create and work on with.
        """
        self.createdoc(docname)
        self.changedoc(docname)


    def renamedoc(self,old_docname,new_docname):
        """Renames the specified document.
        
        Args:
            old_docname (str): The name of the document you want to change.
            new_docname (str): The new name for the document.
        """
        path = f'{self.dbname}/{old_docname}.json'
        new_path = f'{self.dbname}/{new_docname}.json'

        os.rename(path,new_path)

        if self.docname == old_docname:
            self.changedoc(new_docname)
            self.load()


    def deletedoc(self,docname):
        """Deletes the specified document.
        
        Args:
            docname (str): The name of the document you want to delete.
        """
        path = f'{self.dbname}/{docname}.json'

        os.remove(path)

        if self.docname == docname:
            path = f'{self.dbname}/main.json'

            if os.path.exists(path):
                self.changedoc('main')
            else:
                self.cacdoc('main')


    def updatedoc(self, branch, indent=3):
        """Updates the data in the working document with the provided data.
        
        Args:
            branch (dict): The branch dictionary which you want to add to the document.
            indent (int, optional): The indentation of the JSON file.
        """
        path = f'{self.dbname}/{self.docname}.json'

        with open(path,'r') as f:
            data = json.load(f)

        data.update(branch)

        with open(path,'w') as f:
            json.dump(data,f,indent=indent)


    def doctype(self):
        """This function is used to get the type of data.
        
        Returns:
            TYPE: The type of data stored in working document.
        """
        return type(self.data)