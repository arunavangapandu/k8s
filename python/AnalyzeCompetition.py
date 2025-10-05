class AnalyzeCompetition:
  def analyze_competition(self, logs):
   students = {}
   entries =  logs.strip().split(', ')
   print("printing logs:", entries)
   for entry in entries:
    parts = entry.split()
    print(parts)
    student_id = int(parts[0])
    action = parts[1]
    time_stamp = parts[2]
    
    if student_id not in students:
      students[student_id] = {"score": 0, "solves": 0, "fails": 0}
      
    if action == 'solve':
      difficulty = int(parts[3])
      students[student_id]["score"] += difficulty
      students[student_id]["solves"] += 1
      
    elif action == 'fail':
      students[student_id]["fails"] += 1
    print(students)
   result = []     
   for sid, data in students.items():
    if data["solves"] > 0:
      result.append((sid, data["score"], data["solves"], data["fails"]))
    result.sort(key=lambda x: x[1], reverse=True)
    return result
          
instance = AnalyzeCompetition()   
logs = "1 solve 09:00 50, 2 fail 10:00, 1 solve 11:00 30"
result = instance.analyze_competition(logs)
print(result)      
          
       
      
      
     
