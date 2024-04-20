from edapi import EdAPIWL
from colorama import Fore
from datetime import datetime
import time

# Print iterations progress
def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=50, fill='█', printEnd='\r'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()

# initialize Ed API
ed = EdAPIWL()
# authenticate user through the ED_API_TOKEN environment variable
ed.login()

# retrieve user information; authentication is persisted to next API calls
user_info = ed.get_user_info()

user = user_info['user']
print(f"Hello {user['name']}!")

# retrieve the list of courses
courses = user_info['courses']

# number of courses 
num_courses = len(courses)


# A List of Items
items = list(range(0, 57))
l = len(items)


# implement color later

# holds the course id
courses_with_lessons = []


# we will print the title and challenge id of all lessons with type cpp
with open("edstem/integration/edstem-data/data.txt", "w") as f:

  # we need to put the course data in then the lesson data
  # iterate through courses
  for i in range(num_courses):
    course = courses[i]
    # when there is a course with no lessons we will label it as such
    if 'lessons' not in course['course']['features']:
      f.write(f"st_course_id: '{course['course']['id']}'\n")
      f.write(f"st_code: '{course['course']['code']}'\n")
      f.write(f"st_name: '{course['course']['name']}'\n")
      f.write(f"st_lessons: 'False'\n")
    else:
      courses_with_lessons.append(course['course']['id'])
      f.write(f"st_course_id: '{course['course']['id']}'\n")
      f.write(f"st_code: '{course['course']['code']}'\n")
      f.write(f"st_name: '{course['course']['name']}'\n")
      f.write(f"st_lessons: 'True'\n")
  # we iterate through the lessons in the courses with lessons
  total_lessons = sum([len(ed.list_lessons(course_id)['lessons']) for course_id in courses_with_lessons])
  processed_lessons = 0
  printProgressBar(0, total_lessons, prefix = 'Progress:', suffix = 'Complete', length = 50)
  for k in range(len(courses_with_lessons)):

    ed_lesson = ed.list_lessons(courses_with_lessons[k])

    # we get the length of the lessons in the course k
    num_lessons = len(ed_lesson['lessons'])
    
    for i in range(num_lessons):
      # Update Progress Bar
      processed_lessons += 1
      printProgressBar(processed_lessons, total_lessons, prefix='Progress:', suffix='Complete', length=50)
      if ed_lesson['lessons'][i]['type'] != 'general':
        

        if ed_lesson['lessons'][i]['openable'] == True:

          f.write(f"bhavl_course_id: '{courses_with_lessons[k]}'\n")
          f.write(f"bhavl_lesson_id: '{str(ed_lesson['lessons'][i]['id'])}'\n")
          try:
            f.write(f"bhavl_due_at: '{datetime.fromisoformat(ed_lesson['lessons'][i]['due_at']).strftime('%Y-%m-%d %H:%M:%S')}'\n")
          except:
            f.write(f"bhavl_due_at: 'Unavailable'\n")
          f.write(f"bhavl_type: '{ed_lesson['lessons'][i]['type']}'\n")
          f.write(f"bhavl_openable: '{ed_lesson['lessons'][i]['openable']}'\n")
          f.write(f"bhavl_title: '{ed_lesson['lessons'][i]['title']}'\n")
          f.write(f"bhavl_status: '{ed_lesson['lessons'][i]['status']}'\n")

          
          lesson_content = ed.get_lesson_content(ed_lesson['lessons'][i]['id'])

          # Try to get the attempt id
          try:
          
            attempt_id = lesson_content['lesson']['attempt_id'] # note the attempt id is the most recent attempt for the user. NOT THE BEST ATTEMPT.
            
            if attempt_id != 'null':
              try:
                marking_info = ed.get_marking_status(ed_lesson['lessons'][i]['id'], attempt_id)
              except:  
                continue
              else:
                possible_score = 0
                user_score = 0
                for j in range(len(marking_info['lesson_markable_marking_status'])):
                  possible_score += marking_info['lesson_markable_marking_status'][j]['total_points']
                user_score = marking_info['attempt_result']['mark']
                # print(marking_info['attempt_result']['completed_at'])
                f.write(f"bhavl_user_score: '{user_score}'\n")
                f.write(f"bhavl_potential_score: '{possible_score}'\n")
            else:
              continue
          except:
            continue

        # if the lesson is not openable we can't get the challenge id so we get the marking info
        else:
          f.write(f"bhavl_course_id: '{courses_with_lessons[k]}'\n")
          f.write(f"bhavl_lesson_id: '{str(ed_lesson['lessons'][i]['id'])}'\n")
          try:
            f.write(f"bhavl_due_at: '{datetime.fromisoformat(ed_lesson['lessons'][i]['due_at']).strftime('%Y-%m-%d %H:%M:%S')}'\n")
          except:
            f.write(f"bhavl_due_at: 'Unavailable'\n")
          f.write(f"bhavl_type: '{ed_lesson['lessons'][i]['type']}'\n")
          f.write(f"bhavl_openable: '{ed_lesson['lessons'][i]['openable']}'\n")
          f.write(f"bhavl_title: '{ed_lesson['lessons'][i]['title']}'\n")
          f.write(f"bhavl_status: '{ed_lesson['lessons'][i]['status']}'\n")


          
          lesson_content = ed.get_lesson_content(ed_lesson['lessons'][i]['id']) # get lesson content
          
          # get attempt id
          attempt_id = lesson_content['lesson']['attempt_id']

          # if trying to get marking info raises an error then we will not be able to get the user's score
          # we won't print anything about the user's score (for now)

          # try to get marking info
          try:
            marking_info = ed.get_marking_status(ed_lesson['lessons'][i]['id'], attempt_id)
          except:
            continue
          else:
            possible_score = 0
            user_score = 0
            for j in range(len(marking_info['lesson_markable_marking_status'])):
              possible_score += marking_info['lesson_markable_marking_status'][j]['total_points']
              user_score += marking_info['lesson_markable_marking_status'][j]['count_marked']
          # print the user's score and the total possible score
            f.write(f"bhavl_user_score: '{user_score}'\n")
            f.write(f"bhavl_potential_score: '{possible_score}'\n")

      # FOR GENERAL LESSONS
      else:

        f.write(f"bhavl_course_id: '{courses_with_lessons[k]}'\n")
        f.write(f"bhavl_lesson_id: '{str(ed_lesson['lessons'][i]['id'])}'\n")
        try:
          f.write(f"bhavl_due_at: '{datetime.fromisoformat(ed_lesson['lessons'][i]['due_at']).strftime('%Y-%m-%d %H:%M:%S')}'\n")
        except:
          f.write(f"bhavl_due_at: 'Unavailable'\n")
        
        # Print out the rest of the information
        f.write(f"bhavl_type: '{ed_lesson['lessons'][i]['type']}'\n")
        f.write(f"bhavl_openable: '{ed_lesson['lessons'][i]['openable']}'\n")
        f.write(f"bhavl_title: '{ed_lesson['lessons'][i]['title']}'\n")

        # get the lesson content
        lesson_content = ed.get_lesson_content(ed_lesson['lessons'][i]['id'])

        # get attempt id
        attempt_id = lesson_content['lesson']['attempt_id']
        
        # try to get the attempt id
        try:
          marking_info = ed.get_marking_status(ed_lesson['lessons'][i]['id'], attempt_id)
        except:
          continue
        else:
          possible_score = 0
          user_score = 0
          for j in range(len(marking_info['lesson_markable_marking_status'])):
            possible_score += marking_info['lesson_markable_marking_status'][j]['total_points']
            user_score += marking_info['lesson_markable_marking_status'][j]['count_marked'] # kinda weird but we can keep this here for now

        # print the user's score and the total possible score
          f.write(f"bhavl_user_score: '{user_score}'\n")
          f.write(f"bhavl_potential_score: '{possible_score}'\n")

# tell user the data is now being stored and sorted
print(Fore.GREEN + "Data has been stored and sorted" + Fore.RESET)