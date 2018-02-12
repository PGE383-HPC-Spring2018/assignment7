#!/usr/bin/env python

import numpy as np

from assignment7 import convert_to_true_stress_and_strain

def test_convert_to_true_stress_and_strain_1():
    
    strain, stress = convert_to_true_stress_and_strain('data_1.dat') 
    
    np.testing.assert_allclose(strain[:10], np.array([ 1.76974413e-06,  2.19162248e-05, -3.19850395e-05, -2.99607468e-05,
        2.42023361e-05, -1.02986180e-05,  1.80243056e-05,  2.69191677e-05,
        7.80963814e-05,  4.51086396e-05]), atol=1e-6)
    np.testing.assert_allclose(strain[-10:], np.array([0.59983723, 0.59999834, 0.60013837, 0.60030186, 0.60047056,
       0.6006305 , 0.60080112, 0.60096908, 0.60115796, 0.60148428]), atol=1e-6)
    np.testing.assert_allclose(stress[:10], np.array([ 154.06881215,  283.61299635,  406.42699041,  469.85582669,
        592.59040384,  707.33003537,  797.96010967,  920.41457409,
       1043.21711836, 1136.34015604]), atol=1e-6)
    np.testing.assert_allclose(stress[-10:], np.array([55908.23359743, 55789.93743991, 55675.62118854, 55519.82678595,
       55412.86021235, 55211.73381078, 55091.70960098, 54942.77975485,
       54746.31028711, 54060.01842394]), atol=1e-6)
    
    
def test_convert_to_true_stress_and_strain_2():
    
    strain, stress = convert_to_true_stress_and_strain('data_2.dat') 
    
    np.testing.assert_allclose(strain[:10], np.array([ 1.76974413e-06,  2.19162248e-05, -3.19850395e-05, -2.99607468e-05,
        2.42023361e-05, -1.02986180e-05,  1.80243056e-05,  2.69191677e-05,
        7.80963814e-05,  4.51086396e-05]), atol=1e-6)
    np.testing.assert_allclose(strain[-10:], np.array([0.59983723, 0.59999834, 0.60013837, 0.60030186, 0.60047056,
       0.6006305 , 0.60080112, 0.60096908, 0.60115796, 0.60148428]), atol=1e-6)
    np.testing.assert_allclose(stress[:10], np.array([ 153.33046427,  282.2538306 ,  404.47926003,  467.60412469,
        589.75051781,  703.9402797 ,  794.13602519,  916.00364798,
       1038.21768249, 1130.89444428]), atol=1e-6)
    np.testing.assert_allclose(stress[-10:], np.array([55640.303151  , 55522.57390717, 55408.80549646, 55253.75771134,
       55147.30375637, 54947.14121796, 54827.69220322, 54679.47607737,
       54483.94815525, 53800.94522598]), atol=1e-6)

