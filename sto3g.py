"""
  STO-3G  EMSL  Basis Set Exchange Library   3/31/19 7:38 AM
 Elements                             References
 --------                             ----------
  H - Ne: W.J. Hehre, R.F. Stewart and J.A. Pople, J. Chem. Phys. 2657 (1969).
 Na - Ar: W.J. Hehre, R. Ditchfield, R.F. Stewart, J.A. Pople,
          J. Chem. Phys.  2769 (1970).
 K,Ca - : W.J. Pietro, B.A. Levy, W.J. Hehre and R.F. Stewart,
 Ga - Kr: J. Am. Chem. Soc. 19, 2225 (1980).
 Sc - Zn: W.J. Pietro and W.J. Hehre, J. Comp. Chem. 4, 241 (1983) + Gaussian.
  Y - Cd: W.J. Pietro and W.J. Hehre, J. Comp. Chem. 4, 241 (1983). + Gaussian
"""   



orbital_coeffs = {

        'H': {'S' : [  3.42525091,  0.62391373, 0.16885540]},
        'C': {'S' : [ 71.61683700, 13.04509600, 3.53051220],
              'SP': [  2.94124940,  0.68348310, 0.22228990]},
        'N': {'S' : [ 99.10616900, 18.05231200, 4.88566020],
              'SP': [  3.78045590,  0.87849660, 0.28571440]},
        'O': {'S' : [130.70932000, 23.80886100, 6.44360830],
              'SP': [  5.03315130,  1.16959610, 0.38038900]},
        'F': {'S' : [166.67913000, 30.36081200, 8.21682070],
              'SP': [  6.46480320,  1.50228120, 0.48858850]}
        }

primitive_coeffs = {

        'H': {'S' : [ 0.15432897, 0.53532814, 0.44463454]},
        'C': {'S' : [ 0.15432897, 0.53532814, 0.44463454],       
              'SP': [-0.09996723, 0.39951283, 0.70011547],
                    [ 0.15591627, 0.60768372, 0.39195739]},
        'N': {'S' : [ 0.15432897, 0.53532814, 0.44463454],
              'SP': [-0.09996723, 0.39951283, 0.70011547],
                    [ 0.15591627, 0.60768372, 0.39195739]},
        'O': {'S' : [ 0.15432897, 0.53532814, 0.44463454]},       
              'SP': [-0.09996723, 0.39951283, 0.70011547],
                    [ 0.15591627, 0.60768372, 0.39195739]},
        'F': {'S' : [ 0.15432897, 0.53532814, 0.44463454]},
             {'SP': [-0.09996723, 0.39951283, 0.70011547],
                    [ 0.15591627, 0.60768372, 0.39195739]}
        }
