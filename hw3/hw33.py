from turtle import Screen, Turtle 

def lev(n): 
    if n == 0: 
     # Base case 
     return 'F' 
    else: 
     # Recursive case 
     # Calculate the smaller curve 
     smaller = lev(n-1) 
     # Add in the turning in between the smaller curves 
     final = smaller  # First curve 
     if n%2 == 0:   # Even depths require right turns 
      final += 'RR'  # Rotate 90 degrees 
      final += smaller  # Second curve 
      final += 'RRRR'  # Rotate 180 degrees 
      final += smaller  # Third curve 
      final += 'RR'  # Rotate 90 degrees 
      final += smaller  # Final curve 
     else:     # Odd depths require left turns 
      final += 'LL'  # Rotate 90 degrees 
      final += smaller  # Second curve 
           # (No full rotation in odd depths) 
      final += smaller  # Third curve 
      final += 'LL'  # Rotate 90 degrees 
      final += smaller  # Final curve 
     return final   # Done! 

for i in range(4): 
    print(lev(i))