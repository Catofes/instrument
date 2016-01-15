import falcon
from falcon import HTTPError

Error_text = {
    0: ['Unknown Error.',
        falcon.HTTP_500],
    1: ['SQL Error.',
        falcon.HTTP_500],
    2: ['Token Required.',
        falcon.HTTP_400],
    3: ['Login Required',
        falcon.HTTP_403],
    4: ['Login Failed',
        falcon.HTTP_403],
    5: ['Only Json Is Accepted or Sent',
        falcon.HTTP_400],
    6: ['Empty Request Body',
        falcon.HTTP_400],
    7: ['Malformed JSON',
        falcon.HTTP_400],
    8: ['Illegal Username',
        falcon.HTTP_409],
    9: ['Username Existed',
        falcon.HTTP_409],
    10: ['Illegal Email',
         falcon.HTTP_409],
    11: ['Email Existed',
         falcon.HTTP_409],
    12: ['User Name and Password Mismatch.',
         falcon.HTTP_403],
    13: ['Parameters Missing',
         falcon.HTTP_400],
    14: ['Email Not Match.',
         falcon.HTTP_403],
    15: ['Code Error',
         falcon.HTTP_403],
    16: ['Error Status',
         falcon.HTTP_403],
    17: ['Error Password',
         falcon.HTTP_403],
    18: ['Error Zone',
         falcon.HTTP_403],
    19: ['Parameters Error',
         falcon.HTTP_403],
    20: ['Balance not enough.',
         falcon.HTTP_403],
    21: ['Payment Expired.',
         falcon.HTTP_403],
    22: ['Code Could not Used',
         falcon.HTTP_403],
    403: ['',
          falcon.HTTP_403],
    404: ['',
          falcon.HTTP_404]
}


class RError(HTTPError):
    def __init__(self, code=0):
        global Error_text
        self.code = code
        if self.code not in Error_text.keys():
            self.code = 0
        self.text = Error_text[self.code][0]
        self.http_code = Error_text[self.code][1]
        HTTPError.__init__(self, self.http_code, self.text, code=self.code)
