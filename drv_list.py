import sys
sys.path.insert(0, "drivers/")

def gotodrv(model, method, text):
    if model == 'model1':
        model1(method, text)
    elif model == 'model0':
        model0(method, text)
    else:
        print 'no drv cfg'
def model1(method, text):
    from model1 import printme
    printme (method, text)
def model0(method, text):
    from model0 import printme
    printme (method, text)
