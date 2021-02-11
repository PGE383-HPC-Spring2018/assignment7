#/usr/bin/env python
#
# Copyright 2020-2021 John T. Foster
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import unittest
import nbconvert
import os

import numpy as np

with open("assignment7.ipynb") as f:
    exporter = nbconvert.PythonExporter()
    python_file, _ = exporter.from_file(f)


with open("assignment7.py", "w") as f:
    f.write(python_file)


from assignment7 import convert_to_true_stress_and_strain


class TestSolution(unittest.TestCase):
    
    def test_convert_to_true_stress_and_strain(self):

        strain, stress = convert_to_true_stress_and_strain('data.dat') 

        np.testing.assert_allclose(strain[:10], np.array([ 1.76974413e-06,  2.19162248e-05, -3.19850395e-05, -2.99607468e-05,
            2.42023361e-05, -1.02986180e-05,  1.80243056e-05,  2.69191677e-05,
            7.80963814e-05,  4.51086396e-05]), atol=1e-6)
        np.testing.assert_allclose(strain[-10:], np.array([0.59983723, 0.59999834, 0.60013837, 0.60030186, 0.60047056,
           0.6006305 , 0.60080112, 0.60096908, 0.60115796, 0.60148428]), atol=1e-6)
        np.testing.assert_allclose(stress[:10], np.array([ 310.00135992,  570.65679508,  817.77043635,  945.39539323,
           1192.34923999, 1423.21648246, 1605.57296261, 1851.96319545,
           2099.05379863, 2286.42636236]), atol=1e-6)
        np.testing.assert_allclose(stress[-10:], np.array([112492.77647224, 112254.75315531, 112024.73779468, 111711.26437979,
           111496.03728211, 111091.35149831, 110849.85117293, 110550.18990996,
           110154.87432769, 108773.98868365]), atol=1e-6)


if __name__ == '__main__':
    unittest.main()


