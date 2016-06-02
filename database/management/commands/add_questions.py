from django.core.management.base import BaseCommand
from database.models import Question, Choice, Answer, SubTopic
import re
# lines = open('/home/anjaneyulu/Documents/raw_ppp/reasoning/analogy.txt', 'r').readlines()
# db = []
# while 1:
#     d = {"question": "", "options": [], "ans": "", "explanation": ""}
#     missing = {}
#     q = False
#     a = False
#     e = False
#     for line_num, line in enumerate(lines, len(lines)):
#         l = []
#         for i in line.split():
#             if i:
#                 l.append(i)
#         line = " ".join(l)
#         if line:
#             if line[0].isdigit():
#                 if d["question"]:
#                     db.append(d)
#                 # raw_input()
#                 d = {"question": "", "options": [], "ans": "", "explanation": ""}
#                 rpl = re.findall("[0-9]+", line)
#                 # print(rpl)
#                 if rpl:
#                     rpl = rpl[0]
#                 else:
#                     rpl = ""
#
#                 line = line.replace(rpl + ".", "").strip()
#                 line = line.replace(rpl + " .", "").strip()
#                 d["question"] = line
#                 q = True
#                 a = False
#                 e = False
#                 continue
#             elif line.startswith("("):
#                 options = re.findall("\)[a-zA-Z\ )\-]+\(", line + "(")
#                 options = map(lambda x: x.replace(")", "").replace("(", "").strip(), options)
#                 d["options"] = options
#             elif line.startswith("Ans") or line.startswith("ans"):
#                 # print "ans:", line
#                 options = re.findall("\([a-zA-Z\ )]+\)", line)
#                 options = map(lambda x: x.replace(")", "").replace("(", "").strip(), options)
#                 # print(options[0])
#                 d["ans"] = d["options"][ord(options[0].lower()) - 97]
#                 q = False
#                 a = True
#                 e = False
#             elif line.startswith("exp") or line.startswith("Exp"):
#                 # print "explanation:", line
#                 d["explanation"] = "Ans: " + d["ans"] + "<br>" + d["ans"] + line
#                 q = False
#                 a = False
#                 e = True
#             else:
#                 if q:
#                     d["question"] += line
#                 elif e:
#                     d["explanation"] += line
#                 else:
#                     missing[line_num] = line
#     # print("*"*100)
#     # print d["question"]
#     # print d["options"]
#     # print d["ans"]
#     # print d["explanation"]
#     # print("*"*100)
#     db.append(d)
#     print "missed"
#     print missing
#     break

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        # for q_data in db:
        #     data = q_data["question"]
        #     choices = q_data["options"]
        #     ans = q_data['ans']
        #     explanation = q_data['explanation']
        #     sub_topic = SubTopic.objects.get(slug='analogy')
        #     question, create = Question.objects.get_or_create(data=data,
        #                                                       sub_topic=sub_topic)
        #     for choice in choices:
        #         is_ans = ans == choice
        #         Choice.objects.create(description=choice,
        #                               question=question,
        #                               is_answer=is_ans)
        #     Answer.objects.create(explination=explanation,
        #                           question=question)
        #     print (sub_topic)
        #     print (data)
        #     print (choices)
        #     print (ans)
        #     print (explanation)
        import re
        f = open("/home/anjaneyulu/Documents/raw_ppp/databases/dbms.txt", 'r').read()
        num = re.compile('Q.[\d]+')
        indexes = [m.start() for m in re.finditer(num, f)]
        for i in range(len(indexes) - 1):
            start = indexes[i]
            end = indexes[i + 1]
            q = f[start:end]
            # print q
            idx = q.index("(A")
            qs = q[:idx]
            qs = qs.strip()
            chs = q[idx:]
            chs = chs.strip()
            rpl = re.findall("Q.[0-9]+", qs)
            count = qs.count("\n")
            if count > 1:
                qs = qs.replace("\n", "\n<br>\n")
            qno = rpl[0].split(".")[1]
            qs = qs.replace("Q." + qno, '', 1)
            # print(chs)
            # raw_input()
            options = chs.split("(")
            ans = chs.split("Ans:")[1]
            chs = chs.split("Ans:")[0]
            options = re.compile("\([A-Da-d]\)").split(chs)
            ac = re.compile("\([A-Da-d]\)")
            ac = ans.replace("(", "").replace(")", "").strip()
            print(ac)
            is_ans = options[ord(ac.lower()) - 96]
            print "*" * 100
            print "question:", qs
            print"question no: ", qno
            print"options:", options
            print"ans:", is_ans
            # db entry
            sub_topic = SubTopic.objects.get(slug='database-management-systems')
            question, create = Question.objects.get_or_create(data=qs,
                                                              sub_topic=sub_topic)


            for option in options:
                if option:
                    t = is_ans == option
                    count = option.count("\n")
                    option = option.strip()
                    if count > 1:
                        option = option.replace("\n", "\n<br>\n")
                    Choice.objects.create(description=option,
                                          question=question,
                                          is_answer=t)
                    print option

            ans = is_ans.strip().replace("\n", "\n<br>\n")
            print"answer:", ans
            explanation = "<p>" + ans + "</p>"
            Answer.objects.create(explination=explanation,
                                  question=question)
