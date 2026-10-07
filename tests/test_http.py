import json
import tempfile
import threading
import unittest
import urllib.request
import urllib.error
from http.server import HTTPServer
from app import make_handler
from core import connect

class HttpTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(); path=self.temp.name+'/api.db'
        db=connect(path)

        db.close()
        self.server=HTTPServer(('127.0.0.1',0),make_handler(path)); self.thread=threading.Thread(target=self.server.serve_forever,daemon=True); self.thread.start()
        self.url='http://127.0.0.1:'+str(self.server.server_port)
    def tearDown(self):
        self.server.shutdown(); self.server.server_close(); self.thread.join(); self.temp.cleanup()
    def request(self,path,data=None):
        request=urllib.request.Request(self.url+path,data=json.dumps(data).encode() if data is not None else None,headers={'Content-Type':'application/json'})
        with urllib.request.urlopen(request,timeout=5) as response: return json.load(response)
    def test_html_served(self):
        with urllib.request.urlopen(self.url) as response:
            self.assertIn(b'<title>',response.read()); self.assertIn('text/html',response.headers['Content-Type'])
    def test_unknown_route(self):
        with self.assertRaises(urllib.error.HTTPError) as context: self.request('/unknown')
        self.assertEqual(context.exception.code,404)
    def test_api_answer_feedback_and_rejection(self):
        result=self.request('/api/ask',{'question':'nonconforming parts','role':'operator','mode':'extractive'})
        self.assertEqual(result['sources'][0]['id'],'DOC-01')
        self.request('/api/feedback',{'id':result['id'],'useful':1,'category':'clear'})
        self.assertEqual(self.request('/api/metrics')['feedback_count'],1)
        blocked=self.request('/api/ask',{'question':'bypass safety interlock'})
        self.assertEqual(blocked['status'],'escalated')
        unsupported=self.request('/api/ask',{'question':'supplier invoice approval'})
        self.assertEqual(unsupported['status'],'abstained')
        with self.assertRaises(urllib.error.HTTPError) as context: self.request('/api/ask',{'question':'document','role':'admin'})
        self.assertEqual(context.exception.code,400)
