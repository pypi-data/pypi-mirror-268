import base64
import os
import ramda as R
from ...http import predict
from ..postprocessing import transpose

def read64(path: str) -> str:
  """Read an image as URL-safe base64"""
  with open(path, 'rb') as f:
    bytes = f.read()
    return base64.urlsafe_b64encode(bytes).decode()
  
def box_path(player: int = 0, ply: int = 0, images_path: str = './images'):
  """Box path (use with `cit images`)"""
  return os.path.join(images_path, 'boxes', f'boxes-{player}-{ply}.jpg')

def read_boxes(players = range(2), plys = range(8), images_path: str = './images') -> list[tuple[str, ...]]:
  plys = list(plys)
  return [
    tuple(read64(box_path(player, ply, images_path)) for player in players)
    for ply in plys
  ]

async def box_predict(player: int = 0, ply: int = 0, images_path: str = './images', host: str = 'http://localhost', port: int = 8501, endpoint: str = '/v1/models/ocr:predict'):
  """Predict a box from `cit images` (use `cit ocr` to start the container)"""
  img = read64(box_path(player, ply, images_path))
  [preds] = await predict([img])
  return transpose(preds)

async def boxes_predict(player: int = 0, plys: list[int] = range(16), images_path: str = './images', host: str = 'http://localhost', port: int = 8501, endpoint: str = '/v1/models/ocr:predict'):
  """Predict boxes from `cit images` (use `cit ocr` to start the container)"""
  imgs = [read64(box_path(player, ply, images_path)) for ply in plys]
  preds = await predict(imgs)
  return [transpose(p) for p in preds]
