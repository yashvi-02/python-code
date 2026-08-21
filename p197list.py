procedural = ["c", "fortran", "pascal"]
object_oriented = ["java", "c++", "python"]
functional = ["haskell", "scala", "lisp"]
language = str(input("enter a programming language: "))
if language == "c" or language == "fortran" or language == "pascal":
    print("procedural")
elif language == "java"or language == "c++" or language == "python":
    print("object_oriented")
elif language == "haskell"or language == "scala" or language == "lisp":
    print("functional")
