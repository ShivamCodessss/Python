class Employee:
    a = 2

    @classmethod  # class method is used the in class value and the outer value will not be overwritten.
    def show(self):
        print(f"The class attribute of a is {self.a}")


e = Employee()
e.a = 45
e.show()

# if we remove the classmethod then it will print 45.