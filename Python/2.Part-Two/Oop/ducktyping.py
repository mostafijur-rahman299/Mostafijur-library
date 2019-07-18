class Mycharm:
    def execute(self):
        print('running...')
        print('checking..')
        
        
class MyEditor:
    def execute(self):
        print('spilling...')
        print('colling...')

# There is method that is called no matter whatever class..This is ducktyping..
class Laptop:
    def code(self, ide):
        ide.execute() # execute is method
        
ide = MyEditor()
# ide = Mycharm()

lap1 = Laptop()
lap1.code(ide)
