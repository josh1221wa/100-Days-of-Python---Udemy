# What if we want to pass arguments to the decorator function? We use args and kwargs to do this.

# In the below program, a user can only post a blog if they are logged in. The is_authenticated_decorator function checks if the user is logged in. If they are, it runs the blog_post function. If they are not, it does not run the blog_post function.

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False
    
def is_authenticated_decorator(function):
    def wrapper(*args):
        # The args variable is a tuple of all the arguments passed to the function that the decorator is applied to. In this case, the function is blog_post, and the only argument is user. In this way the decorator can access the arguments of the function that it is applied to.
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@is_authenticated_decorator
def blog_post(user):
    print(f"This is {user.name}'s blog post.")

user = User("John")
user.is_logged_in = True
blog_post(user)