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
        answers = {
            '1': 'A',
            '10': 'A',
            '100': 'C',
            '101': 'B',
            '102': 'A',
            '103': 'C',
            '104': 'A',
            '105': 'A',
            '106': 'C',
            '107': 'D',
            '108': 'D',
            '109': 'B',
            '11': 'C',
            '110': 'C',
            '111': 'B',
            '112': 'A',
            '113': 'A',
            '114': 'A',
            '115': 'A',
            '116': 'A',
            '117': 'B',
            '118': 'A',
            '119': 'A',
            '12': 'B',
            '120': 'A',
            '121': 'A',
            '122': 'A',
            '123': 'A',
            '124': 'A',
            '13': 'A',
            '14': 'D',
            '15': 'D',
            '16': 'A',
            '17': 'B',
            '18': 'B',
            '19': 'A',
            '2': 'D',
            '20': 'D',
            '21': 'B',
            '22': 'B',
            '23': 'A',
            '24': 'D',
            '25': 'C',
            '26': 'A',
            '27': 'C',
            '28': 'A',
            '29': 'A',
            '3': 'C',
            '30': 'C',
            '31': 'B',
            '32': 'B',
            '33': 'C',
            '34': 'A',
            '35': 'B',
            '36': 'C',
            '37': 'D',
            '38': 'C',
            '39': 'D',
            '4': 'B',
            '40': 'C',
            '41': 'A',
            '42': 'A',
            '43': 'B',
            '44': 'B',
            '45': 'C',
            '46': 'D',
            '47': 'B',
            '48': 'A',
            '49': 'C',
            '5': 'A',
            '50': 'C',
            '51': 'A',
            '52': 'B',
            '53': 'D',
            '54': 'B',
            '55': 'C',
            '56': 'A',
            '57': 'D',
            '58': 'A',
            '59': 'B',
            '6': 'C',
            '60': 'B',
            '61': 'C',
            '62': 'B',
            '63': 'A',
            '64': 'D',
            '65': 'D',
            '66': 'C',
            '67': 'C',
            '68': 'A',
            '69': 'B',
            '7': 'A',
            '70': 'B',
            '71': 'B',
            '72': 'B',
            '73': 'B',
            '74': 'C',
            '75': 'C',
            '76': 'B',
            '77': 'A',
            '78': 'B',
            '79': 'B',
            '8': 'A',
            '80': 'D',
            '81': 'D',
            '82': 'B',
            '83': 'D',
            '84': 'A',
            '85': 'B',
            '86': 'D',
            '87': 'B',
            '88': 'D',
            '89': 'C',
            '9': 'C',
            '90': 'C',
            '91': 'D',
            '92': 'C',
            '93': 'D',
            '94': 'A',
            '95': 'B',
            '96': 'D',
            '97': 'B',
            '98': 'C',
            '99': 'C'}
        f = open("/home/anjaneyulu/Documents/raw_ppp/c-mcqs/cprograms.txt", 'r').read()
        indexes = [m.start() for m in re.finditer('Q.', f)]
        for i in range(len(indexes) - 1):
            start = indexes[i]
            end = indexes[i + 1]
            q = f[start:end]
            # print q
            idx = q.index("(a)")
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
            # options = chs.split("(")
            options = re.compile("\([A-Da-d]\)").split(chs)
            is_ans = options[ord(answers[qno].lower()) - 96]
            print "*" * 100
            print "question:", qs
            print"question no: ", qno
            print"options:", options
            sub_topic = SubTopic.objects.get(slug='c-language')
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
                    # print option
                    # if t:
                    #     print ">>yes"
            ans = is_ans.strip().replace("\n", "\n<br>\n")
            # print"answer:", ans
            explanation = "<p>" + ans + "</p>"
            Answer.objects.create(explination=explanation,
                                  question=question)
            # raw_input()



