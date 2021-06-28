import socketio
import json

sio = socketio.Client()

@sio.on('connect', namespace = '/ws')
def connect():
    print('connected')

@sio.on('result', namespace = '/ws')
def on_winner(data):
    with open('colorfile', 'w') as f:
        grb = list(map(data['rgb'].__getitem__, (1, 0, 2)))
        f.write(str(grb))

sio.connect('http://18.222.108.51', namespaces = ['/ws'])
sio.wait()
