import pickle

examInfo_dict = {
"IELTS (International English Language Testing System)": 
'''Writing section consists of two tasks: Task 1 (minimum 150 words) and Task 2 (minimum 250 words).
Task 1 requires the test taker to describe, summarize or explain information presented in a graph, table, chart, or diagram, while Task 2 requires the test taker to write an essay in response to a prompt.
Scores range from 0-9 in half-point increments, with a separate band score for each section and an overall band score.
''',

"TOEFL (Test of English as a Foreign Language)": 
'''Writing section consists of two tasks: Integrated Writing Task (150-225 words) and Independent Writing Task (300-350 words).
Integrated Writing Task requires the test taker to read a passage, listen to a lecture and write a response, while Independent Writing Task requires the test taker to write an essay in response to a prompt.
Scores range from 0-30 in one-point increments, with a separate score for each section and a total score.
''',

"CAE (Cambridge English: Advanced)": 
'''Writing section consists of two tasks: Task 1 (220-260 words) and Task 2 (220-260 words).
Task 1 requires the test taker to write an essay, article, letter, or report, while Task 2 requires the test taker to select and complete one of four writing tasks.
Scores range from 0-210 in five-point increments, with a separate score for each section and a total score.
''',

"CPE (Cambridge English: Proficiency)": 
'''Writing section consists of two tasks: Task 1 (240-280 words) and Task 2 (240-280 words).
Task 1 requires the test taker to write an essay, article, letter, or report, while Task 2 requires the test taker to select and complete one of four writing tasks.
Scores range from A to C, with C being the highest level of achievement.
''',

"PTE Academic (Pearson Test of English Academic)":
'''Writing section consists of two tasks: Task 1 (20 minutes, 200-300 words) and Task 2 (40 minutes, 300-450 words).
Task 1 requires the test taker to write an essay based on a given prompt, while Task 2 requires the test taker to analyze a graph, chart, or diagram and write a short essay explaining the information presented.
Scores range from 10-90, with each section (reading, writing, speaking, and listening) scored separately and an overall band score.
''',

"GRE (Graduate Record Examination)":
'''The Analytical Writing section consists of two tasks: Task 1 (30 minutes) and Task 2 (30 minutes).
Task 1 requires the test taker to analyze an issue and present their perspective on the issue, while Task 2 requires the test taker to analyze an argument presented in a given passage.
Scores range from 0-6, in half-point increments, with the two tasks combined to give an overall score.
''',

"GMAT (Graduate Management Admission Test)":
'''The Analytical Writing Assessment consists of one task (30 minutes) requiring the test taker to analyze an argument presented in a given passage and write an essay presenting their analysis and critique.
Scores range from 0-6, in half-point increments, with an overall score for the section and an overall score for the exam.
''',

"SAT (Scholastic Assessment Test)":
'''The Writing and Language section consists of four passages with accompanying multiple-choice questions (35 minutes).
The essay portion is optional, and requires the test taker to analyze an argument presented in a given passage and write an essay presenting their analysis and critique (50 minutes).
Scores for the multiple-choice questions range from 200-800, with a separate score for the essay portion ranging from 2-8.
''',

"ESOL (English for Speakers of Other Languages)": 
'''Writing section consists of two tasks: Task 1 (100-140 words) and Task 2 (140-190 words). Task 1 requires the test taker to write a short message, note or letter. Task 2 requires the test taker to write an essay in response to a prompt.
Scores range from Entry Level 1 (A1) to Level 2 (B2) on the Common European Framework of Reference for Languages (CEFR).
''',

"CELPIP (Canadian English Language Proficiency Index Program)":
'''Writing section consists of two tasks: Task 1 (150-200 words) and Task 2 (300-400 words).
Task 1 requires the test taker to write an email, while Task 2 requires the test taker to respond to a prompt by either writing an email, making notes, or writing a letter.
Scores range from 0-12 in one-point increments, with a separate score for each section and an overall score.
''',

"ACT (American College Testing)":
'''Writing section consists of one task: an optional essay (40 minutes).
The essay requires the test taker to analyze a complex issue and develop an argument, with supporting examples.
Scores range from 2-12 in one-point increments.
''',

"OET (Occupational English Test)":
'''Writing section consists of one task: a referral letter (180-200 words) based on a patient case note or letter.
The letter must demonstrate the test taker's ability to organize and present information clearly and coherently, as well as their ability to use appropriate language in a professional setting.
Scores range from A to E, with A being the highest level of achievement.
''',

"BEC (Business English Certificate)": 
'''Writing section consists of two parts. Part 1 (100 words) requires the test taker to write an email, memo, report or proposal. Part 2 (250 words) requires the test taker to write an essay in response to a prompt related to business or work.
Scores range from Pass with Merit, Pass or Fail.
''',

"ILEC (International Legal English Certificate)": 
'''ILEC assesses the language skills needed in the legal profession, with a focus on international law. The exam is divided into four sections: Reading, Writing, Listening, and Speaking.
Scores range from A to C, with C being the highest score. Each section is worth 25% of the overall grade.
''',

"TOEIC (Test of English for International Communication)": 
'''TOEIC assesses proficiency in English for business settings, with a focus on listening and reading comprehension. The exam consists of two sections: Listening and Reading.
Scores range from 10-990, with separate scores for each section. The higher the score, the greater the level of proficiency in English for international communication.
''',

"Trinity ISE (Trinity College London: Integrated Skills in English)":
'''Writing section consists of two tasks: Task 1 (140-190 words) and Task 2 (250-280 words).
Task 1 requires the test taker to write a letter, email, note, or short message, while Task 2 requires the test taker to write an essay in response to a prompt.
Scores range from Pass with Distinction, Pass with Merit, Pass, and Fail.
''',

"FCE (FCE (First Certificate in English))":
'''Writing section consists of two tasks: Task 1 (140-190 words) and Task 2 (250 words).
Task 1 requires the test taker to write an email, letter, report, or review, while Task 2 requires the test taker to select and complete one of three writing tasks.
Scores range from A to C, with C being the minimum passing grade.
''',

"PET (Preliminary English Test)":
'''Writing section consists of two tasks: Task 1 (100 words) and Task 2 (140 words).
Task 1 requires the test taker to write an email, letter, or note, while Task 2 requires the test taker to write an essay in response to a prompt.
Scores range from A to C, with C being the minimum passing grade.
''',

"KET (Key English Test)":
'''Writing section consists of two tasks: Task 1 (25 words) and Task 2 (35-45 words).
Task 1 requires the test taker to write a short message, while Task 2 requires the test taker to complete a form or write a short message.
Scores range from A to C, with C being the minimum passing grade.
''',

"BULATS (Business Language Testing Service)":
'''Writing section consists of two tasks: Task 1 (50-60 words) and Task 2 (180-200 words).
Task 1 requires the test taker to write an email or short memo, while Task 2 requires the test taker to write a report or letter.
Scores range from 0-100 in five-point increments, with separate scores for each section and an overall score.
'''
}


# Open the file for writing
with open('exam_info.pkl', 'wb') as f:
    # Use pickle to dump the dictionary into the file
    pickle.dump(examInfo_dict, f)