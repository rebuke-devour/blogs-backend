"""Web Routes."""

from masonite.routes import Get, Post, Put,  Delete, RouteGroup

ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),

     RouteGroup([
        Get("/", "blogsController@index").name("index"),
        Get("/@id", "blogsController@show").name("show"),
        Post("/", "blogsController@create").name("create"),
        Put("/@id", "blogsController@update").name("update"),
        Delete("/@id", "blogsController@destroy").name("destroy")
    ],prefix="/blogs",name= "blogs")
]
