import unittest
from src.synapse_transform import Sale,aggregate
class SynapseTest(unittest.TestCase):
 def test_region_revenue(self):self.assertEqual(aggregate([Sale("NSW",2,10),Sale("NSW",1,5)]),{"NSW":25})
 def test_rejects_negative(self):
  with self.assertRaises(ValueError):aggregate([Sale("NSW",-1,5)])
if __name__=="__main__":unittest.main()