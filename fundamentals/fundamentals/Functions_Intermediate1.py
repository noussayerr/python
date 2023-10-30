#1
x = [ [5,2,3], [10,8,9] ] 
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0]=15
print (x)
students[0]['last_name']="Bryant"
print(students)
sports_directory['soccer'][0]="Andres"
print(sports_directory)
z[0]['y']=30
print(z)
#
def iterateDictionary(list1):
    for i in range (len(list1)):
        print(list1[i])
iterateDictionary(students)
#3
def iterateDictionary2(key,list1):
    for i in range (len(list1)):
        print (list1[i][key])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)
#4
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(dojo):
    print (len(dojo['locations']))
    for i in range (len(dojo['locations'])):
        print (dojo['locations'][i])
    print (len(dojo['instructors']))
    for i in range (len(dojo['instructors'])):
        print (dojo['instructors'][i])
printInfo(dojo)
