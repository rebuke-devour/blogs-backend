# """ A blogsController Module """

from masonite.controllers import Controller
from masonite.request import Request
from app.blogs import blogs

def __init__(self,request: Request):
    self.request = request



class blogsController(Controller):
    """Class Docstring Description
    """

 

    # def show(self):
    #     """Show a single resource listing
    #     ex. Model.find('id')
    #         Get().route("/show", blogsController)
    #     """
    #     id = self.request.param("id")
    #     return blogs.where("id",id).get()
    

    # def index(self):
    #     return blogs.all()

    def show(self):
        """Show a single resource listing
        ex. Model.find('id')
            Get().route("/show", blogsController)
        """
        id = self.request.param("id")
        return blogs.find(id)

    def index(self):
        """Show several resource listings
        ex. Model.all()
            Get().route("/index", blogsController)
        """
        return blogs.all()





    def create(self):
        subject = self.request.input("subject")
        details = self.request.input("details")
        blogs = blogs.create({"subject": subject, "details": details})
        return blogs


    def update(self):
        """Edit an existing resource listing
        ex. Post target to update new Model
            Post().route("/update", blogsController)
        """

        pass

    def destroy(self):
        """Delete an existing resource listing
        ex. Delete().route("/destroy", blogsController)
        """

        pass