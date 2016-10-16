from django.core.management.base import BaseCommand
from database.models import Question, Choice, Answer, SubTopic
import re
class Command(BaseCommand):

    def handle(self, *args, **options):
        import re
        answers = {'1': 'c',
                   '2': 'd',
                   '3': 'a',
                   '4': 'd',
                   '5': 'b',
                   '6': 'b',
                   '7': 'a',
                   '8': 'b',
                   '9': 'a',
                   '10': 'b',
                   '11': 'c',
                   '12': 'c',
                   '13': 'b',
                   '14': 'e',
                   '15': 'a',
                   '16': 'c',
                   '17': 'a',
                   '18': 'b',
                   '19': 'c',
                   '20': 'a',
                   '21': 'e',
                   }
        f = open("/home/anjaneyulu/Documents/raw_ppp/letter-series/letter-series.txt", 'r').read()
        indexes = [m.start() for m in re.finditer('Q\.', f)]
        for i in range(len(indexes) - 1):
            start = indexes[i]
            end = indexes[i + 1]
            q = f[start:end]
            print q
            idx = q.index("(a)")
            qs = q[:idx]
            qs = qs.strip()
            chs = q[idx:]
            chs = chs.strip()
            rpl = re.findall("Q\.[0-9]+", qs)
            count = qs.count("\n")
            if count > 1:
                qs = qs.replace("\n", "\n<br>\n")
            qno = rpl[0].split(".")[1]
            qs = qs.replace("Q." + qno, '', 1)
            # options = chs.split("(")
            options = re.compile("\([A-Ea-e]\)").split(chs)
            print"raw data:", options
            # print q
            is_ans = (answers[qno].lower())
            print is_ans
            is_ans = options[ord(answers[qno].lower()) - 96]
            print "*" * 100
            print "question:", qs
            print"question no: ", qno
            print"options:", options
            print"ans:", is_ans
            # db entry
            sub_topic = SubTopic.objects.get(slug='letter-series')
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
            explanation = "<p>Answer: " + ans + "</p>"
            Answer.objects.create(explination=explanation,
                                  question=question)

        print "::: database updated :::"
