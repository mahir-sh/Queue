import math
import matplotlib.pyplot as plt
import numpy as np
import random

class_time=[800, 1000, 1100, 1300, 1400, 1500]  #using 24hr format
student=[]

#GENERATE STUDENT NUMBER

np.random.seed(1)

for i in range(0, len(class_time)):
  num = np.random.normal(loc=100.0, scale=5.0, size=None) #generate student number at each class time.
  student.append(int(num))
print("Different time Student Arrival number : ", student)

#Assume there is only for 1 shuttle
Shuttle_capacity = 30 
Service_Time = 15

individual_arrival_time=[] #In Each Class time individual arrival time
A_T=[]                 # list For each class arrival student

individual_minute=[] #arrival minute before class
Minute=[]   # list For each arrival minute before class

#GENERATE ARRIVAL TIME 


np.random.seed(1)
for i in range(0, len(class_time)):
  for j in range(0, student[i]):
    
    t= random.expovariate(0.15) #randomly generate minute before class
    t=int(t)
    individual_minute.append(t)

    if class_time[i]==800:
      if t == 0:
        individual_arrival_time.append(800)
      else:
        arrival_time = 760-t
        individual_arrival_time.append(arrival_time)
    
    elif class_time[i]==1000:
      if t == 0:
        individual_arrival_time.append(1000)
      else:
        arrival_time = 960-t
        individual_arrival_time.append(arrival_time)

    elif class_time[i]==1100:
      if t == 0:
        individual_arrival_time.append(1100)
      else:
        arrival_time = 1060-t
        individual_arrival_time.append(arrival_time)
    
    elif class_time[i]==1300:
      if t == 0:
        individual_arrival_time.append(1300)
      else:
        arrival_time = 1260-t
        individual_arrival_time.append(arrival_time)

    elif class_time[i]==1400:
      if t == 0:
        individual_arrival_time.append(1400)
      else:
        arrival_time = 1360-t
        individual_arrival_time.append(arrival_time)

    elif class_time[i]==1500:
      if t == 0:
        individual_arrival_time.append(1500)
      else:
        arrival_time = 1460-t
        individual_arrival_time.append(arrival_time)

  individual_minute.sort(reverse = True) #sorted individual minute on a fixed class time
  Minute.append(individual_minute)
  individual_minute=[]

  individual_arrival_time.sort() #sorted individual arrival time from its waiting time on a fixed class time
  A_T.append(individual_arrival_time)
  individual_arrival_time=[]
  #print(len(A_T))

print("Each Student arrive before class in mins : ", Minute)
print("Each Student Arrival Time: ", A_T)

#GENERATE NUMBER OF TRIP FOR CLASS TIME


student_in_trip=[]
trip_no=[]
Trip=[]
Each_Class_Student_Trip=[]


for i in range(0, len(class_time)):
  count_student_num =0  #each time no of student counter that use shuttle
  shuttle_used=0        #total of count_student_num 
  count_trip=0
  
  for j in range(0, len(A_T[i])):
    if class_time[i]==800:
      # check if total arriving student is les than capacity
      if len(A_T[i]) <= Shuttle_capacity :
        student_in_trip.append(len(A_T[i]))
        count_trip += 1
        trip_no.append(count_trip)
      else:
        count_student_num += 1
        if count_student_num >= Shuttle_capacity:
          #for first trip we assume shuttle is alwyas be there until its capacity full
          
          count_trip += 1
          trip_no.append(count_trip)
          student_in_trip.append(count_student_num)
          shuttle_used += count_student_num
          remaining_student = len(A_T[i])-shuttle_used
          if remaining_student < Shuttle_capacity:
            student_in_trip.append(remaining_student)
            count_trip += 1
            trip_no.append(count_trip)
          
          count_student_num=0
      
    elif class_time[i]==1000:

      # check if total arriving student is les than capacity
      if len(A_T[i]) <= Shuttle_capacity :
        student_in_trip.append(len(A_T[i]))
        trip_no.append(count_trip)
        break
      
      # if total arriving student is greater than shuttle capacity
      else:
        count_student_num += 1
        if count_student_num >= Shuttle_capacity:
          #for first trip we assume shuttle is alwyas be there until its capacity full
          
          count_trip += 1
          trip_no.append(count_trip)
          student_in_trip.append(count_student_num)
          shuttle_used += count_student_num
          remaining_student = len(A_T[i])-shuttle_used
          if remaining_student < Shuttle_capacity:
            student_in_trip.append(remaining_student)
            count_trip += 1
            trip_no.append(count_trip)
          
          count_student_num=0
    elif class_time[i]==1100:
      # check if total arriving student is les than capacity
      if len(A_T[i]) <= Shuttle_capacity :
        student_in_trip.append(len(A_T[i]))
        trip_no.append(count_trip)
        break
      
      # if total arriving student is greater than shuttle capacity
      else:
        count_student_num += 1
        if count_student_num >= Shuttle_capacity:
          #for first trip we assume shuttle is alwyas be there until its capacity full
          
          count_trip += 1
          trip_no.append(count_trip)
          student_in_trip.append(count_student_num)
          shuttle_used += count_student_num
          remaining_student = len(A_T[i])-shuttle_used
          if remaining_student < Shuttle_capacity:
            student_in_trip.append(remaining_student)
            count_trip += 1
            trip_no.append(count_trip)

          count_student_num=0

    elif class_time[i]==1300:
      # check if total arriving student is les than capacity
      if len(A_T[i]) <= Shuttle_capacity :
        student_in_trip.append(len(A_T[i]))
        trip_no.append(count_trip)
        break
      
      # if total arriving student is greater than shuttle capacity
      else:
        count_student_num += 1
        if count_student_num >= Shuttle_capacity:
          #for first trip we assume shuttle is alwyas be there until its capacity full
          
          count_trip += 1
          trip_no.append(count_trip)
          student_in_trip.append(count_student_num)
          shuttle_used += count_student_num
          remaining_student = len(A_T[i])-shuttle_used
          if remaining_student < Shuttle_capacity:
            student_in_trip.append(remaining_student)
            count_trip += 1
            trip_no.append(count_trip)
          
          count_student_num=0

    elif class_time[i]==1400:
      # check if total arriving student is les than capacity
      if len(A_T[i]) <= Shuttle_capacity :
        student_in_trip.append(len(A_T[i]))
        trip_no.append(count_trip)
        break
      
      # if total arriving student is greater than shuttle capacity
      else:
        count_student_num += 1
        if count_student_num >= Shuttle_capacity:
          #for first trip we assume shuttle is alwyas be there until its capacity full
          
          count_trip += 1
          trip_no.append(count_trip)
          student_in_trip.append(count_student_num)
          shuttle_used += count_student_num
          remaining_student = len(A_T[i])-shuttle_used
          if remaining_student < Shuttle_capacity:
            student_in_trip.append(remaining_student)
            count_trip += 1
            trip_no.append(count_trip)
          
          count_student_num=0

    elif class_time[i]==1500:
      # check if total arriving student is les than capacity
      if len(A_T[i]) <= Shuttle_capacity :
        student_in_trip.append(len(A_T[i]))
        trip_no.append(count_trip)
        break
      
      # if total arriving student is greater than shuttle capacity
      else:
        count_student_num += 1
        if count_student_num >= Shuttle_capacity:
          #for first trip we assume shuttle is alwyas be there until its capacity full
          
          count_trip += 1
          trip_no.append(count_trip)
          student_in_trip.append(count_student_num)
          shuttle_used += count_student_num
          remaining_student = len(A_T[i])-shuttle_used
          if remaining_student < Shuttle_capacity:
            student_in_trip.append(remaining_student)
            count_trip += 1
            trip_no.append(count_trip)
          
          count_student_num=0

      
          
  Each_Class_Student_Trip.append(student_in_trip)
  student_in_trip=[]
  Trip.append(trip_no)
  trip_no=[]

print("NUMBER_OF_TRIP_EACH_CLASS_TIME:\n",Trip)
print("NUMBER_OF_STUDENT_EACH_TRIP:\n", Each_Class_Student_Trip)

#GENERATE INDIVIDUAL WAITING TIME FOR USEING SHUTTLE 



Each_Trip_Wait=[]
Each_Trip_Arrive=[]


individual_wait=[]
arriving_time=[]

WAIT = []
ARRIVE =[]

Each_Trip_Departure =[]

for i in range(0, len(class_time)):
  total_number_student=0
  if class_time[i]==800:
    for j in range(0, len(Each_Class_Student_Trip[i])):

      total_number_student += Each_Class_Student_Trip[i][j]
      prev_number_student = total_number_student - Each_Class_Student_Trip[i][j]
      #print("total_number_student", total_number_student)
      if j == 0:
        for m in range(0, total_number_student):
          wait = 0
          individual_wait.append(wait)
          arriving_time.append(A_T[i][m])
      else:
        shuttle_departure = A_T[i][total_number_student-1] + (Service_Time *(j-1))
        #print(shuttle_departure)
        arrive = shuttle_departure + Service_Time
        arrive_mod = arrive % 100
        if arrive_mod >= 60:
          shuttle_arrive = (arrive - arrive_mod)+ 100 + (arrive_mod - 60) #to make time format
        else:
          shuttle_arrive = arrive
        #print(shuttle_arrive)

        for m in range(prev_number_student, total_number_student):
          wait = (shuttle_arrive - A_T[i][m])-40 #to adjust time value
          if wait <= 0 or wait < Service_Time:
            wait = wait + 40 #to adjust time
            individual_wait.append(wait)
            arriving_time.append(A_T[i][m])
          else:
            individual_wait.append(wait)
            arriving_time.append(A_T[i][m])

      Each_Trip_Wait.append(individual_wait)
      individual_wait=[]
      Each_Trip_Arrive.append(arriving_time)
      arriving_time=[]
   

  elif class_time[i]==1000:
    for j in range(0, len(Each_Class_Student_Trip[i])):

      total_number_student += Each_Class_Student_Trip[i][j]
      prev_number_student = total_number_student - Each_Class_Student_Trip[i][j]
      #print("total_number_student", total_number_student)
      if j == 0:
        for m in range(0, total_number_student):
          wait = 0
          individual_wait.append(wait)
          arriving_time.append(A_T[i][m])
      else:
        shuttle_departure = A_T[i][total_number_student-1] + (Service_Time *(j-1))
        #print(shuttle_departure)
        arrive = shuttle_departure + Service_Time
        arrive_mod = arrive % 100
        if arrive_mod >= 60:
          shuttle_arrive = (arrive - arrive_mod)+ 100 + (arrive_mod - 60) #to make time format
        else:
          shuttle_arrive = arrive
        #print(shuttle_arrive)

        for m in range(prev_number_student, total_number_student):
          wait = (shuttle_arrive - A_T[i][m])-40 #to adjust time value
          if wait <= 0 or wait < Service_Time:
            wait = wait + 40 #to adjust time
            individual_wait.append(wait)
            arriving_time.append(A_T[i][m])
          else:
            individual_wait.append(wait)
            arriving_time.append(A_T[i][m])

      Each_Trip_Wait.append(individual_wait)
      individual_wait=[]
      Each_Trip_Arrive.append(arriving_time)
      arriving_time=[]

  elif class_time[i]==1100:
    for j in range(0, len(Each_Class_Student_Trip[i])):

      total_number_student += Each_Class_Student_Trip[i][j]
      prev_number_student = total_number_student - Each_Class_Student_Trip[i][j]
      #print("total_number_student", total_number_student)
      if j == 0:
        for m in range(0, total_number_student):
          wait = 0
          individual_wait.append(wait)
          arriving_time.append(A_T[i][m])
      else:
        shuttle_departure = A_T[i][total_number_student-1] + (Service_Time *(j-1))
        #print(shuttle_departure)
        arrive = shuttle_departure + Service_Time
        arrive_mod = arrive % 100
        if arrive_mod >= 60:
          shuttle_arrive = (arrive - arrive_mod)+ 100 + (arrive_mod - 60) #to make time format
        else:
          shuttle_arrive = arrive
        #print(shuttle_arrive)

        for m in range(prev_number_student, total_number_student):
          wait = (shuttle_arrive - A_T[i][m])-40 #to adjust time value
          if wait <= 0 or wait < Service_Time:
            wait = wait + 40 #to adjust time
            individual_wait.append(wait)
            arriving_time.append(A_T[i][m])
          else:
            individual_wait.append(wait)
            arriving_time.append(A_T[i][m])

      Each_Trip_Wait.append(individual_wait)
      individual_wait=[]
      Each_Trip_Arrive.append(arriving_time)
      arriving_time=[]

  elif class_time[i]==1300:
    for j in range(0, len(Each_Class_Student_Trip[i])):

      total_number_student += Each_Class_Student_Trip[i][j]
      prev_number_student = total_number_student - Each_Class_Student_Trip[i][j]
      #print("total_number_student", total_number_student)
      if j == 0:
        for m in range(0, total_number_student):
          wait = 0
          individual_wait.append(wait)
          arriving_time.append(A_T[i][m])
      else:
        shuttle_departure = A_T[i][total_number_student-1] + (Service_Time *(j-1))
        #print(shuttle_departure)
        arrive = shuttle_departure + Service_Time
        arrive_mod = arrive % 100
        if arrive_mod >= 60:
          shuttle_arrive = (arrive - arrive_mod)+ 100 + (arrive_mod - 60) #to make time format
        else:
          shuttle_arrive = arrive
        #print(shuttle_arrive)

        for m in range(prev_number_student, total_number_student):
          wait = (shuttle_arrive - A_T[i][m])-40 #to adjust time value
          if wait <= 0 or wait < Service_Time:
            wait = wait + 40 #to adjust time
            individual_wait.append(wait)
            arriving_time.append(A_T[i][m])
          else:
            individual_wait.append(wait)
            arriving_time.append(A_T[i][m])

      Each_Trip_Wait.append(individual_wait)
      individual_wait=[]
      Each_Trip_Arrive.append(arriving_time)
      arriving_time=[]

  elif class_time[i]==1400:
    for j in range(0, len(Each_Class_Student_Trip[i])):

      total_number_student += Each_Class_Student_Trip[i][j]
      prev_number_student = total_number_student - Each_Class_Student_Trip[i][j]
      #print("total_number_student", total_number_student)
      if j == 0:
        for m in range(0, total_number_student):
          wait = 0
          individual_wait.append(wait)
          arriving_time.append(A_T[i][m])
      else:
        shuttle_departure = A_T[i][total_number_student-1] + (Service_Time *(j-1))
        #print(shuttle_departure)
        arrive = shuttle_departure + Service_Time
        arrive_mod = arrive % 100
        if arrive_mod >= 60:
          shuttle_arrive = (arrive - arrive_mod)+ 100 + (arrive_mod - 60) #to make time format
        else:
          shuttle_arrive = arrive
        #print(shuttle_arrive)

        for m in range(prev_number_student, total_number_student):
          wait = (shuttle_arrive - A_T[i][m])-40 #to adjust time value
          if wait <= 0 or wait < Service_Time:
            wait = wait + 40 #to adjust time
            individual_wait.append(wait)
            arriving_time.append(A_T[i][m])
          else:
            individual_wait.append(wait)
            arriving_time.append(A_T[i][m])

      Each_Trip_Wait.append(individual_wait)
      individual_wait=[]
      Each_Trip_Arrive.append(arriving_time)
      arriving_time=[]

  elif class_time[i]==1500:
    for j in range(0, len(Each_Class_Student_Trip[i])):

      total_number_student += Each_Class_Student_Trip[i][j]
      prev_number_student = total_number_student - Each_Class_Student_Trip[i][j]
      #print("total_number_student", total_number_student)
      if j == 0:
        for m in range(0, total_number_student):
          wait = 0
          individual_wait.append(wait)
          arriving_time.append(A_T[i][m])
      else:
        shuttle_departure = A_T[i][total_number_student-1] + (Service_Time *(j-1))
        #print(shuttle_departure)
        arrive = shuttle_departure + Service_Time
        arrive_mod = arrive % 100
        if arrive_mod >= 60:
          shuttle_arrive = (arrive - arrive_mod)+ 100 + (arrive_mod - 60) #to make time format
        else:
          shuttle_arrive = arrive
        #print(shuttle_arrive)

        for m in range(prev_number_student, total_number_student):
          wait = (shuttle_arrive - A_T[i][m])-40 #to adjust time value
          if wait <= 0 or wait < Service_Time:
            wait = wait + 40 #to adjust time
            individual_wait.append(wait)
            arriving_time.append(A_T[i][m])
          else:
            individual_wait.append(wait)
            arriving_time.append(A_T[i][m])

      Each_Trip_Wait.append(individual_wait)
      individual_wait=[]
      Each_Trip_Arrive.append(arriving_time)
      arriving_time=[]



  WAIT.append(Each_Trip_Wait)
  Each_Trip_Wait=[]
  ARRIVE.append(Each_Trip_Arrive)
  Each_Trip_Arrive=[]


print("WAITING_TIME_TO_EACH_TO_USE_SHUTTLE:\n ",WAIT)
print("ARRIVING_TIME_OF_EACH_TO_USE_SHUTTLE:\n ",ARRIVE)

#GENERATE AVERAGE WAITING TIME TO USE SHUTTLE


Average=[]
AVERAGE_WATING=[]
AVERAGE_WATING_IN_CLASS=[]
AVERAGE_SHUTTLE_UTILIZE=[]

for i in range(0, len(class_time)):
  utilize=0
  for j in range(0, len(WAIT[i])):
    average=sum(WAIT[i][j])/Each_Class_Student_Trip[i][j]
    #print(average)
    Average.append(average)
    if len(WAIT[i][j]) == Shuttle_capacity:
      utilize +=1

  AVERAGE_WATING.append(Average)
  Average=[]
  AVERAGE_SHUTTLE_UTILIZE.append(utilize)

print("AVERAGE_WAITING_TIME_TO_USE_EACH_TRIP_OF_SHUTTLE:\n",AVERAGE_WATING)
print("FULL_CAPACITY_OF_SHUTTLE_USE_EACH_CLASS_TIME:\n",AVERAGE_SHUTTLE_UTILIZE)

#GENERATE AVERAGE WAITING TIME OF ALL STUDENTS IN CLASS TIME 

WAITING_TIME=[]
for i in range(0, len(class_time)):
  avg =sum(AVERAGE_WATING[i])/len(Trip[i])
  WAITING_TIME.append(avg)
print("AVERAGE_OF_WAITING_IN_CLASS_TIME:", WAITING_TIME)

plt.scatter(class_time,student,s=250,c='GREEN')
plt.xlabel("CLASS TIME")
plt.ylabel("TOTAL NUMBER OF STUDENT")
plt.title("CLASS TIME VS STUDENT ")
plt.show()

total_trip=[]
for i in range(0, len(class_time)):
  total_trip.append(len(Trip[i]))

plt.scatter(class_time,total_trip,s=250,c='Coral')
plt.xlabel("CLASS TIME")
plt.ylabel("Total Number of trips")
plt.title("CLASS TIME VS No. OF TRIPS ")
plt.show()

plt.scatter(class_time,WAITING_TIME,s=250,c='Purple')
plt.xlabel("CLASS TIME")
plt.ylabel("Average Wating time")
plt.title("CLASS TIME VS WAITING TIME ")
plt.show()

plt.scatter(class_time,AVERAGE_SHUTTLE_UTILIZE,s=150,c='BlUE')
plt.xlabel("Class Time")
plt.ylabel("Number of shuttle full utilized")
plt.title("CLASS TIME VS SHUTTLE UTILIZATION ")
plt.show()

c=['brown','pink','yellow','red','green','orange','blue']

for i in range(0, len(Trip)):
  print("For Class Time of", class_time[i])
  plt.scatter(Trip[i],AVERAGE_WATING[i],s=200,c=c[i])
  plt.xlabel("Number of trips on Class Time")
  plt.ylabel("Average Waiting Time")
  plt.title("EACH TRIP VS AVERAGE WAITING ")
  plt.show()
