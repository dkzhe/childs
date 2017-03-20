import tornado.ioloop
import tornado.web

import interface

class Register(tornado.web.RequestHandler):
    def get(self):
        if not self.get_secure_cookie('zc0'):
            member_id = interface.RegMember()
            self.set_secure_cookie('zc0', str(member_id))
            self.write('Your cookie was not set yet!')
        else:
            pass

class Generate(tornado.web.RequestHandler):
    def get_user(self):
        return self.get_secure_cookie('zc0')

    def get(self):
        member_id = get_user()
        questions = interface.GenQuestions(member_id)
        self.write(questions)

class Submit(tornado.web.RequestHandler):
    def get_answers(self, json):
        return interface.GetAnswers(json)

    def post(self, *args, **kwargs):
        answers = get_answers(args)
        self.write(answers)

class Score(tornado.web.RequestHandler):
    def get_user(self):
        return self.get_secure_cookie('zc0')

    def get(self):
        member_id = get_user()
        score = interface.GetScore(member_id)
        self.write(score)

application = tornado.web.Application([
    (r'/register', Register),
    (r'/questions', Generate),
    (r'/answers', Submit),
    (r'/score', Score),
], cookie_secret='61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=')

if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()