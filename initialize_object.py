# Initialize an object means to make this object ready for employment
# This portion of code means take the value of the parameter tasks and store for later use in the variable giraffe_task


class Giraffes:
    def __init__(self, task):
        self.giraffe_task = task


# oscar and gertrude are instance or object of class Giraffes with values 100 and 150
# this code has the effect to call function __init__ and use 100 and 150 for the value of the parameter task
# oscar.giraffe_task this . full stop means object of class like  oscar refers to variables and function of this class
oscar = Giraffes(100)
gertrude = Giraffes(150)

print(oscar.giraffe_task)
print(gertrude.giraffe_task)

