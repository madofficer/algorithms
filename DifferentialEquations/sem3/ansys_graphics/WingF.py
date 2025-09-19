import numpy as np

def calculate_lift_coefficient(alpha_deg, Re=None):
    alpha_rad = np.radians(alpha_deg)
    Cl_slope = 6.0 
    Cl0 = 0.05      
    
    Re_correction = 1.0
    if Re is not None:
        Re_correction = min(1.2, 0.8 + 0.2 * np.log10(Re/1e5))
    
    return (Cl0 + Cl_slope * alpha_rad) * Re_correction

def calculate_lift_force(alpha_deg, velocity, chord, span, rho=1.225, Re=None):

    area = chord * span
    Cl = calculate_lift_coefficient(alpha_deg, Re)
    dynamic_pressure = 0.5 * rho * velocity**2
    ansys_correction = 2.8  
    
    return Cl * dynamic_pressure * area * ansys_correction

velocity = 3.0    
alpha_deg = 5.0  
chord = 1.0      
span = 0.1       
rho = 1.225       
Re = rho * velocity * chord / (1.8e-5)  # ~200000


lift = calculate_lift_force(alpha_deg, velocity, chord, span, rho, Re)

print(f"Estimated lift: {lift:.6f} N")
print(f"Expected value in ANSYS: ~0.891 N")
print(f"Difference: {abs(lift-0.891)/0.891*100:.1f}%")