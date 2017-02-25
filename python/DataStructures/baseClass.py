#This will have implementation for a organism class

class livingOrg(object):
    count = 0
    def __init__(self, name):
        self.name = name
        livingOrg.count += 1
   
    def greet(self):
        print 'Hello I am %s pleased to meet you'%self.name
    
    @classmethod
    def getCount(self):
        '''
        returns the number of organisms created
        '''
        print 'there are currently %d organisms'%livingOrg.count

class python(livingOrg):
    def __init__(self, name):
        livingOrg.__init__(self, name)
        self.Type = 'Snake'

    def makeSound(self):
        print 'hissssss'


if __name__ == '__main__':
    boa = python('boa')
    boa.greet()
    livingOrg.getCount()
    boa.makeSound()

