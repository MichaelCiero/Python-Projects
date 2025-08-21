print("Hello, the following quiz will require answers in letter form (a, b, c, etc), so please limit your answers to single letters and NO PERIODS. Enjoy!")
point_total = 0

q1 = input("What year did the First Crusade begin? A. 904, B. 1096, C. 1123, or D. 1209 ---> ")
if q1.lower() == "b":
    print("Correct! +100 pts")
    point_total = point_total + 100
else:
    print("Incorrect! +0 pts")

q2 = input("What was the main goal of the First Crusade? A. To conquer the Holy Roman Empire, B. To stop the Mongols from conquering Europe, C. To convince Japan to establish trade with various European countries, or D. To recapture Jerusalem from Muslim Control ---> ")
if q2.lower() == "d":
    print("Correct! +100pts")
    point_total = point_total + 100
else:
    print("Incorrect! +0 pts")

q3 = input("Which Crusade ended with the capture of Constantinople by Western Crusaders, and thus the abandonment of the task initially given to the Crusaders by the pope? A. The First Crusade, B. The Second Crusade, C. The Third Crusade, or D. The Fourth Crusade ---> ")
if q3.lower() == "d":
    print("Correct! +100pts")
    point_total = point_total + 150
else:
    print("Incorrect! +0 pts")

print("Your total score was...")
print(str(point_total) + " / 350")