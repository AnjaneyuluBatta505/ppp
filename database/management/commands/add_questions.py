from django.core.management.base import BaseCommand
from database.models import Question, Choice, Answer, SubTopic
import re
lines = open('/home/anjaneyulu/Documents/raw_ppp/reasoning/analogy.txt', 'r').readlines()
db = []
while 1:
    d = {"question": "", "options": [], "ans": "", "explanation": ""}
    missing = {}
    q = False
    a = False
    e = False
    for line_num, line in enumerate(lines, len(lines)):
        l = []
        for i in line.split():
            if i:
                l.append(i)
        line = " ".join(l)
        if line:
            if line[0].isdigit():
                if d["question"]:
                    db.append(d)
                # raw_input()
                d = {"question": "", "options": [], "ans": "", "explanation": ""}
                rpl = re.findall("[0-9]+", line)
                # print(rpl)
                if rpl:
                    rpl = rpl[0]
                else:
                    rpl = ""

                line = line.replace(rpl + ".", "").strip()
                line = line.replace(rpl + " .", "").strip()
                d["question"] = line
                q = True
                a = False
                e = False
                continue
            elif line.startswith("("):
                options = re.findall("\)[a-zA-Z\ )\-]+\(", line + "(")
                options = map(lambda x: x.replace(")", "").replace("(", "").strip(), options)
                d["options"] = options
            elif line.startswith("Ans") or line.startswith("ans"):
                # print "ans:", line
                options = re.findall("\([a-zA-Z\ )]+\)", line)
                options = map(lambda x: x.replace(")", "").replace("(", "").strip(), options)
                # print(options[0])
                d["ans"] = d["options"][ord(options[0].lower()) - 97]
                q = False
                a = True
                e = False
            elif line.startswith("exp") or line.startswith("Exp"):
                # print "explanation:", line
                d["explanation"] = "Ans: " + d["ans"] + "<br>" + d["ans"] + line
                q = False
                a = False
                e = True
            else:
                if q:
                    d["question"] += line
                elif e:
                    d["explanation"] += line
                else:
                    missing[line_num] = line
    # print("*"*100)
    # print d["question"]
    # print d["options"]
    # print d["ans"]
    # print d["explanation"]
    # print("*"*100)
    db.append(d)
    print "missed"
    print missing
    break

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        for q_data in db:
            data = q_data["question"]
            choices = q_data["options"]
            ans = q_data['ans']
            explanation = q_data['explanation']
            sub_topic = SubTopic.objects.get(slug='analogy')
            question, create = Question.objects.get_or_create(data=data,
                                                              sub_topic=sub_topic)
            for choice in choices:
                is_ans = ans == choice
                Choice.objects.create(description=choice,
                                      question=question,
                                      is_answer=is_ans)
            Answer.objects.create(explination=explanation,
                                  question=question)
            print (sub_topic)
            print (data)
            print (choices)
            print (ans)
            print (explanation)


