from app.questions.pool import question_pool

from app.questions.amec import question_methods
pool_amec = question_pool(question_methods, "AMec")

from app.questions.chemistry import chemistry_question
pool_chemistry = question_pool(chemistry_question, "Chemie")