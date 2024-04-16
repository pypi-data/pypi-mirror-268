from typing import TypedDict
from pydantic import BaseModel
import aiohttp

class SamplePreds(BaseModel):
  preds: list[str]
  logprobs: list[float]

class TFSResponse(BaseModel):
  predictions: list[SamplePreds]
  
class Params(TypedDict):
  host: str
  port: int
  endpoint: str
  
async def predict(b64imgs: list[str], host: str = 'http://localhost', port: int = 8501, endpoint: str = '/v1/models/ocr:predict') -> list[SamplePreds]:
  base = f'{host.strip("/")}:{port}'
  async with aiohttp.ClientSession(base) as session:
    req = session.post(endpoint, json={
      "signature_name": "serving_default",
      "instances": b64imgs
    })
    async with req as res:
      x = await res.text()
      return TFSResponse.model_validate_json(x).predictions
    