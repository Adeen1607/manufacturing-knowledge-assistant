import argparse
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from core import ROOT, answer_question, connect, log_answer, feedback, metrics

def make_handler(db_path):
    class Handler(BaseHTTPRequestHandler):
        def send(self,obj,status=200):
            self.send_response(status); self.send_header('Content-Type','application/json'); self.end_headers(); self.wfile.write(json.dumps(obj,allow_nan=False).encode())
        def do_GET(self):
            if self.path == '/':
                self.send_response(200); self.send_header('Content-Type','text/html; charset=utf-8'); self.end_headers(); self.wfile.write((ROOT/'index.html').read_bytes()); return
            db=connect(db_path)
            try:
                if self.path == '/api/metrics': self.send(metrics(db))
                else: self.send({'error':'Not found'},404)
            finally: db.close()
        def do_POST(self):
            db=connect(db_path)
            try:
                length=int(self.headers.get('Content-Length',0))
                if not 0 < length <= 16384: raise ValueError('Invalid body size')
                data=json.loads(self.rfile.read(length))
                if self.path == '/api/ask':
                    result=answer_question(data['question'],data.get('role','operator'),data.get('mode','extractive'))
                    self.send(log_answer(db,data.get('role','operator'),result))
                elif self.path == '/api/feedback':
                    feedback(db,data['id'],data['useful'],data['category']); self.send({'saved':True})
                else: self.send({'error':'Not found'},404)
            except (ValueError,KeyError,TypeError) as e: self.send({'error':str(e)},400)
            finally: db.close()
    return Handler

if __name__=='__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('--port',type=int,default=8052); parser.add_argument('--db',default=str(ROOT/'local.db')); args=parser.parse_args()
    print(f'Open http://127.0.0.1:{args.port}',flush=True)
    HTTPServer(('127.0.0.1',args.port),make_handler(args.db)).serve_forever()
