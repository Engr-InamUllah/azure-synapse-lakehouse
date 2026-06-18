from dataclasses import dataclass
@dataclass(frozen=True)
class Sale: region:str; quantity:int; unit_price:float
def aggregate(rows:list[Sale])->dict[str,float]:
 out={}
 for r in rows:
  if r.quantity<0 or r.unit_price<0: raise ValueError("negative sales values")
  out[r.region]=round(out.get(r.region,0)+r.quantity*r.unit_price,2)
 return out