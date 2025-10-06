from datetime import datetime

class LibraryDigitalSystem:
    def library_digital_system(self, logs):
       # Format for parsing times
       fmt = "%H:%M"

       # We need to parse the string into multiple parts
       # Track borrowing and return times for each book
       # calculate the total borrowed time for each book
       # Find the maximum duration
       # if 2 books share the smae max duration, return them in ascending order by ID
       # Dictionaries to store borrow times and total durations
       borrow_times = {}
       total_durations = {}

       entries = logs.split(',' )

       # for each entry split into parts
       for entry in entries:
          book_id_str, action, time_str =  entry.split()
          book_id = int(book_id_str)

          if action == "borrow":
              borrow_times[book_id] = time_str
          elif action == "return":
             # Get and remove the borrow time for this book
              borrow_time_str = borrow_times.pop(book_id)
              borrow_time = datetime.strptime(borrow_time_str, fmt)
              return_time = datetime.strptime(time_str, fmt)
              delta = return_time - borrow_time
              minutes = int(delta.total_seconds() // 60)

             # Add to total duration
              if book_id in total_durations:
                 total_durations[book_id] += minutes
              else:
                 total_durations[book_id] = minutes

       print(total_durations.items())
       max_duration = max(total_durations.values())
            
       print(max_duration)

       # Convert minutes to "HH:MM" format
       def minutes_to_hhmm(minutes):
          hours = minutes // 60
          mins = minutes % 60
          print(f"{hours:02}:{mins:02}")
          return f"{hours:02}:{mins:02}"
       
       # Collect all books with the  max duration
       result = []
       for book_id, duration in total_durations.items():
          if duration == max_duration:
             result.append((book_id, minutes_to_hhmm(duration)))

       result.sort()
       return result

logs = "1 borrow 09:00, 1 return 11:00, 1 borrow 12:00, 1 return 13:00, 2 borrow 12:00, 2 return 13:00"
lib_digital_system = LibraryDigitalSystem()
print(lib_digital_system.library_digital_system(logs))



          
       
