# Created by Tyler Gearing

from scipy.optimize import fmin_cobyla as max

def farm_optimize(acres, hours, p1, p2, h1, h2): 
    #objective
    def objective(X, p1, p2):
        x,y = X
        return -(p1*x + p2*y)
    #constraint 1
    def c1(X, acres, hours, h1, h2):
        x,y = X
        return hours - h1*x - h2*y
    #constraint 2
    def c2(X, acres, hours, h1, h2):
        x,y = X
        return acres - x - y
    #constraint 3
    def c3(X, acres, hours, h1, h2):
        return X[0]
    #constraint 4
    def c4(X, acres, hours, h1, h2):
        return X[1]
    
    X = max(objective, x0=[acres, 0], cons=[c1,c2,c3,c4],
            args=(p1,p2), consargs=(acres, hours, h1, h2))
    
    print ('With input:')
    print (acres,'total acres',hours,'total labor-hours')
    print ('${}'.format(p1),'corn profit-per-acre',
           '${}'.format(p2),'oat profit-per-acre')
    print (h1,'corn labor-hours',h2,'oat labor-hours')
    print (' We should plant {0:.1f} acres of corn.'.format(X[0]))
    print (' We should plant {0:.1f} acres of oats.'.format(X[1]))
    print (' The maximum profit we can earn is ${0:.2f}.'
           .format(-objective(X, p1, p2)))
    print ()

farm_optimize(240, 320, 40, 30, 2, 1)
farm_optimize(300, 380, 70, 45, 3, 1)
farm_optimize(180, 420, 65, 55, 3, 1)
