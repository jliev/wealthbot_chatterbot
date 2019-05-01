# chat/consumers.py
from channels.generic.websocket import WebsocketConsumer
from .wealthbot_function.client import registration0
from .wealthbot_function.profile import registration1,registration2,registration3
from .wealthbot_function.profile import registration4,registration5,registration6,completeStepThree
import json
import re

class obj(object):
    def __init__(self, d):
        for a, b in d.items():
            if isinstance(b, (list, tuple)):
               setattr(self, a, [obj(x) if isinstance(x, dict) else x for x in b])
            else:
               setattr(self, a, obj(b) if isinstance(b, dict) else b)
        self.META ={}


# wealthbot interface

class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()
        self.wealthbot = wealthbot_chat()
        self.scope = obj(self.scope)

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        response, result = self.wealthbot.get_response(message)
#        print("yayayya_________________")
#        print(self.scope)
#        response, result = message,message
        self.wealthbot.recv_msg(self.scope,result)
        self.send(text_data=json.dumps({
            'message': response
        }))


class wealthbot_chat:

    def __init__(self):

        self.registration_step = 0
        self.field0 = ['first_name', 'last_name', 'email', 'password1', 'password2', 'is_accepted']
        self.field1 = ['client-first_name', 'client-last_name', 'client-birth_date',
                       'client-marital_status', 'client-phone_number', 'client-annual_income',
                       'client-estimated_income_tax', 'client-liquid_net_worth', 'client-employment_type']
        self.field2 = ['answer_11', 'answer_10', 'answer_9', 'answer_12']
        self.field3 = ['client_account_types-groups']
        self.field4 = ['client_account_types-groups','client_account_types-group_type']
        self.field5 = ['value', 'contribution_type']
        self.field6 = ['value', 'monthly_contributions', 'monthly_distributions', 'sas_cash']

        self.step = -1

        self.post0 = {}
        self.post1 = {}
        self.post2 = {}
        self.post3 = {}
        self.post4 = {}
        self.post5 = {}
        self.post6 = {}

        self.function0 = registration0
        self.function1 = registration1
        self.function2 = registration2
        self.function3 = registration3
        self.function4 = registration4
        self.function5 = registration5
        self.function6 = registration6
        self.function7 = completeStepThree
        self.name = ""

    def recv_msg(self, request, message):
        # initial registration step
        print(message)
        if self.registration_step == 0:
            if self.step <= -1:
                self.step += 1
                return
            if self.step == 0:
                field1 = self.field0[self.step]
                field2 = self.field0[self.step+1]
                self.post0[field1] = message.split(' ')[0]
                self.post0[field2] = message.split(' ')[1]
                self.step += 2
            else:
                field = self.field0[self.step]
                self.post0[field] = message
                self.step += 1
            print('--------post0-------:', self.post0)
            # for debug
            # self.post0[self.field0[0]] = 'Li'
            # self.post0[self.field0[1]] = 'Jiahao'
            # self.post0[self.field0[2]] = '115@qq.com'
            # self.post0[self.field0[3]] = 'Adgjmptw63318798'
            # self.post0[self.field0[4]] = 'Adgjmptw63318798'
            # self.post0[self.field0[5]] = 'True'
            if set(self.post0.keys()) == set(self.field0): #初始表填完了
                request.POST = self.post0
                # post form0
                print("function0")
                self.function0(request, 5)
                # intialize form1
                self.step = 1
                self.registration_step = 1
                self.post1['client-first_name'] = self.post0['first_name']
                self.post1['client-last_name']  = self.post0['last_name']
                return

        #first registration step
        if self.registration_step == 1:
            if self.step <= 1:
                self.step += 1
                return
            field = self.field1[self.step]
            self.post1[field] = message
            self.step += 1
            print('--------post1-------:', self.post1)
            if set(self.post1.keys()) == set(self.field1):  # 第一张表填完了
                request.POST = self.post1
                # post form1
                print("function1")
                self.function1(request)
                self.step = -1
                self.registration_step = 2
                return

        #second registration step
        if self.registration_step == 2:
            if self.step <= -1:
                self.step += 1
                return
            field = self.field2[self.step]
            self.post2[field] = message
            self.step += 1
            print('--------post2-------:', self.post2)
            if set(self.post2.keys()) == set(self.field2):  # 第二张表填完了
                request.POST = self.post2
                # post form2
                print("function2")
                self.function2(request)
                self.step = -1
                self.registration_step = 3
                return

        #third registration step
        if self.registration_step == 3:
            if self.step <= -1:
                self.step += 1
                return
            field = self.field3[self.step]
            self.post3[field] = message
            self.step += 1
            print('--------post3-------:', self.post3)
            if set(self.post3.keys()) == set(self.field3):  # 第三张表填完了
                request.POST = self.post3
                # post form3
                print("function3")
                self.function3(request)
                self.step = 1
                self.registration_step = 4
                self.post4['client_account_types-groups'] = self.post3['client_account_types-groups']
                return

        #forth registration step
        if self.registration_step == 4:
            field = self.field4[self.step]
            self.post4[field] = message
            self.step += 1
            print('--------post4-------:', self.post4)
            if set(self.post4.keys()) == set(self.field4):  # 第四张表填完了
                request.POST = self.post4
                # post form4
                print("function4")
                self.function4(request)
                self.step = 0
                self.registration_step = 5
                return

        #fifth registration step
        if self.registration_step == 5:
            field = self.field5[self.step]
            self.post5[field] = message
            self.step += 1
            print('--------post5-------:', self.post5)
            if set(self.post5.keys()) == set(self.field5):  # 第五张表填完了
                request.POST = self.post5
                # post form5
                print("function5")
                self.function5(request)
                self.step = 1
                self.registration_step = 6
                self.post6['value'] = self.post5['value']
                return

        #sixth registration step
        if self.registration_step == 6:

            for i in range(self.step,len(self.field6)):
                field = self.field6[i]
                self.post6[field] = 0
            request.POST = self.post6
            print("function6")
            self.function6(request)
            self.function7(request)
            return

    def get_response(self,message):

        result = message
        response = "Not inplement yet"

        if self.registration_step == 0:

            if self.step <= -1:
                if message == "login":
                    response = "What is your name"
                else:
                    response = "if you want to start, send login"
                    self.step -= 1

            elif self.step == 0:
                patterns, key = ["{M,m}y name is ","I am "], "\w+ \w+"
                result = extract_info(patterns, key, message)
                self.name = result.split(' ')[1]
                response = f"Dear {self.name},what's your email"

            elif self.step == 2:
                patterns, key = ["{M,m}y email is "], "\w+@\w+.com"
                result = extract_info(patterns, key, message)
                response = "Set your password please"

            elif self.step == 3:
                patterns, key = [], "\w+"
                result = extract_info(patterns, key, message)
                response = "Verify your password please"

            elif self.step == 4:
                patterns, key = [], "\w+"
                result = extract_info(patterns, key, message)
                response = "Do you accept the rules, True/False"

            elif self.step == 5:
                patterns, key = [], "\w+"
                result = extract_info(patterns, key, message)
                if result == 'True':
                    response = "\ncongratulation, you have finish the first step \n" \
                               "if you want to continue, send continue"


        elif self.registration_step == 1:

            if self.step <= 1:
                if message == "continue":
                    response = f"Dear {self.name}, When is your birthday"
                else:
                    response = "please send continue to next step"
                    self.step -= 1

            if self.step == 2:
                pattern = "\d+-\d+-\d+"
                result = re.findall(pattern , message)[0]
                response = f"Dear {self.name},what's your marital_status"

            if self.step == 3:
                response = f"what's your phone_number"

            if self.step == 4:
                response = f"what's your annual income"

            if self.step == 5:
                response = f"what's your income tax"

            if self.step == 6:
                response = f"what's your liquid_net_worth"

            if self.step == 7:
                response = f"what's your employment type"

            if self.step == 8:
                response = "\ncongratulation, you have finish the second step \n" \
                           "if you want to continue, send continue \n" \
                           "then I will ask you some question to give advice\n"

        elif self.registration_step == 2:
            if self.step <= -1:
                if message == "continue":
                    response = f"\nDear {self.name} , which one do you prefer:\n" \
                               f"a.steady but lower return \n"\
                               f"b.maximizing long term gains,even experience short term losses\n"
                else:
                    response = "please send continue to next step"
                    self.step -= 1

            if self.step == 0:
                if 'a' in message:
                    result = 30
                if 'b' in message:
                    result = 31
                response = f"\nDear {self.name} , which set of hypothetical portfolio returns in\n" \
                           f"one year is most acceptable to you: \n"\
                           f"a. +/- 15% \n"\
                           f"b. +/- 10% \n"\
                           f"c. +/-  5% \n"\

            if self.step == 1:
                if 'a' in message:
                    result = 27
                if 'b' in message:
                    result = 28
                if 'c' in message:
                    result = 29

                response = f"\nAs you know, the global stock market is often volatile. if your entire investment portfolio\n" \
                           f"lost 10% of its value in a month during a market decline, what would you do\n" \
                           f"a. sell all of your investments\n"\
                           f"b. sell some \n"\
                           f"c. keep all  \n"\
                           f"d. buy more  \n"

            if self.step == 2:
                if 'a' in message:
                    result = 23
                if 'b' in message:
                    result = 24
                if 'c' in message:
                    result = 25
                if 'd' in message:
                    result = 26

                response = f"\nwill you need up to 1/4 of your portfolio within the next 10 years for a \n" \
                           f"alrge expense(house, college, etc.)?\n" \
                           f"a. Yes\n"\
                           f"b. No \n"\

            if self.step == 3:
                if 'a' in message:
                    result = 32
                if 'b' in message:
                    result = 33
                response = "\ncongratulation, you have finish the third step \n" \
                           "if you want to continue, send continue \n" \

        elif self.registration_step == 3:
            if self.step <= -1:
                if message == "continue":
                    response = f"What types of accounts will we be managing for you\n" \
                               f"a.Open a new account\n" \
                               f"b.Transfer an account\n" \
                               f"c.Rollover a 401(k) plan\n"

                else:
                    response = "please send continue to next step"
                    self.step -= 1

            if self.step == 0:
                if 'a' in message:
                    result = 'deposit_money'
                response = f"What types of accounts will you opening\n" \
                           f"a.Personal Investment Account\n" \
                           f"b.Joint Investment Account\n" \
                           f"c.Roth IRA\n" \
                           f"d.Traditional IRA\n"

        elif self.registration_step == 4:
            if self.step == 1:
                if 'a' in message:
                    result = 'Personal Account'
                response = f"How much do you want to invest\n"

        elif self.registration_step == 5:
            if self.step == 0:
                response = f"Will you be making contributions or\n" \
                           f"withdrawing money from the account\n" \
                           f"a.Contributions\n" \
                           f"b.Distributions\n" \
                           f"c.Neither\n"
            if self.step == 1:
                response = "send anything,then you can see the portfolio from\n"\
                           "the see my portfolio button"

        elif self.registration_step == 6:
            pass

        return response,result



def extract_info(patterns,key,message):
    patterns.append("")
    for pattern in patterns:
        results = re.findall(pattern + key, message)
        if results:
            break
    result1 = results[0]
    result2 = re.findall(pattern, message)[0]
    result = result1.replace(result2, "")
    return result
