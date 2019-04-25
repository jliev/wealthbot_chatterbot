# chat/consumers.py
from channels.generic.websocket import WebsocketConsumer
from .wealthbot_function.client import registration0
from .wealthbot_function.profile import registration1,registration2,registration3,registration4,registration5,registration6
import json

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
#       1.the connection has been built: Xinyu (finished)
#       2.get response from message to the user interface : Niu Hongqian and Liu xian
#       response = chatterbot.get_response(message)
#       3.update the user profile by the message: Li Jiahao
        self.wealthbot.recv_msg(self.scope,message)

        response = message + " " + "(chatterbot not implement yet)"
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

        self.step = 0

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


    def recv_msg(self, request, message):
        # initial registration step
        print(message)
        if self.registration_step == 0:
            field = self.field0[self.step]
            self.post0[field] = message
            self.step += 1
            print('--------post0-------:', self.post0)
            if set(self.post0.keys()) == set(self.field0): #初始表填完了
                request.POST = self.post0
                # post form0
                print("function0")
                self.function0(request, 5)
                # intialize form1
                self.step = 2
                self.registration_step = 1
                self.post1['client-first_name'] = self.post0['first_name']
                self.post1['client-last_name']  = self.post0['last_name']
                return

        #first registration step
        if self.registration_step == 1:
            field = self.field1[self.step]
            self.post1[field] = message
            self.step += 1
            print('--------post1-------:', self.post1)
            if set(self.post1.keys()) == set(self.field1):  # 第一张表填完了
                request.POST = self.post1
                # post form1
                print("function1")
                self.function1(request)
                self.step = 0
                self.registration_step = 2
                return

        #second registration step
        if self.registration_step == 2:
            field = self.field2[self.step]
            self.post2[field] = message
            self.step += 1
            print('--------post2-------:', self.post2)
            if set(self.post2.keys()) == set(self.field2):  # 第二张表填完了
                request.POST = self.post2
                # post form2
                print("function2")
                self.function2(request)
                self.step = 0
                self.registration_step = 3
                return

        #third registration step
        if self.registration_step == 3:
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
            return


