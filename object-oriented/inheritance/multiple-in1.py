

# this file will explain , multiple inheritance in python
# multiple inheritance is not supported in java and c# 
# but in python it is supported


# consider a scenario

# class parent1{
#     void m1(){
#         System.out.println(" parent1 method m1");
#     }
# }


# class parent2{
#     void m1(){
#         System.out.println(" parent2 method m1");
#     }
# }


# class child extends parent1 , parent2{

# }

# note , here confusion is there that in child which m1() method gets inherited
# is it comes from parent1
# or from parent2
# java and c# cant resolve this confusion
# but python resolves this confusion by giving order wise priority to parents
# if in list of parents , parent1 comes before parent2 , then m1() of parent1 will get executed
# below code will demonstrate the scene

class parent1:

    def m1(self):
        print('parent1 m1() method')


class parent2:

    def m1(self):
        print('parent2 m1() method')


class child(parent1,parent2): # note that parent1 is having higher priority than parent2
    pass

class child1(parent2,parent1): # note that parent2 is having higher priority than parent1
    pass


c = child()
c.m1()      # first python will search in class child
            # if not found then it will search in parent1 (if found there , it will get executed)
            # if not found then it will search in parent2

# observe the changes in order of parents in child and child1
c1 = child1()
c1.m1()