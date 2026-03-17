import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# ============================================================
# GEBENES STRÖMUNGSFELD
# v(x, y) = 2xy² î - x³y ĵ
# ============================================================

def v_x(x, y):
    """x-Komponente des Geschwindigkeitsfeldes"""
    return 2 * x * y**2

def v_y(x, y):
    """y-Komponente des Geschwindigkeitsfeldes"""
    return -x**3 * y

# ============================================================
# (a) BERECHNUNG DER BESCHEUNIGUNG IM PUNKT (2; 1)
# ============================================================

def acceleration(x, y):
    """
    Beschleunigung im stationären Strömungsfeld: a = (v·∇)v
    
    ax = vx * ∂vx/∂x + vy * ∂vx/∂y
    ay = vx * ∂vy/∂x + vy * ∂vy/∂y
    """
    
    # Ableitungen berechnen
    d_vx_dx = 2 * y**2              # ∂(2xy²)/∂x = 2y²
    d_vx_dy = 4 * x * y             # ∂(2xy²)/∂y = 4xy
    d_vy_dx = -3 * x**2 * y         # ∂(-x³y)/∂x = -3x²y
    d_vy_dy = -x**3                 # ∂(-x³y)/∂y = -x³
    
    vx, vy = v_x(x, y), v_y(x, y)
    
    ax = vx * d_vx_dx + vy * d_vx_dy
    ay = vx * d_vy_dx + vy * d_vy_dy
    
    return ax, ay

# Berechnung im Punkt (2; 1)
x_point_a = 2.0
y_point_a = 1.0
ax_point, ay_point = acceleration(x_point_a, y_point_a)
magnitude_a = np.sqrt(ax_point**2 + ay_point**2)

print("=" * 60)
print("PART (a): BESCHLEUNIGUNG IM PUNKT (2; 1)")
print("=" * 60)
print(f"Position: ({x_point_a}; {y_point_a})")
print(f"Vₓ = {v_x(x_point_a, y_point_a):.2f}")
print(f"Vᵧ = {v_y(x_point_a, y_point_a):.2f}")
print("-" * 60)
print(f"Ableitungen:")
print(f"∂Vₓ/∂x = {d_vx_dx:.2f}")
print(f"∂Vₓ/∂y = {d_vx_dy:.2f}")
print(f"∂Vᵧ/∂x = {d_vy_dx:.2f}")
print(f"∂Vᵧ/∂y = {d_vy_dy:.2f}")
print("-" * 60)
print(f"Beschleunigungskomponenten:")
print(f"aₓ = Vₓ·(∂Vₓ/∂x) + Vᵧ·(∂Vₓ/∂y)")
print(f"aₓ = {v_x(x_point_a, y_point_a)} · {d_vx_dx} + {v_y(x_point_a, y_point_a)} · {d_vx_dy}")
print(f"    = {v_x(x_point_a, y_point_a) * d_vx_dx + v_y(x_point_a, y_point_a) * d_vx_dy:.2f}")
print(f"aᵧ = Vₓ·(∂Vᵧ/∂x) + Vᵧ·(∂Vᵧ/∂y)")
print(f"aᵧ = {v_x(x_point_a, y_point_a)} · {d_vy_dx} + {v_y(x_point_a, y_point_a)} · {d_vy_dy}")
print(f"    = {v_x(x_point_a, y_point_a) * d_vy_dx + v_y(x_point_a, y_point_a) * d_vy_dy:.2f}")
print("-" * 60)
print(f"\nERGEBNIS (a): aₓ = {ax_point:.2f}, aᵧ = {ay_point:.2f}")
print(f"           |a| = {magnitude_a:.2f}")
print("=" * 60)

# ============================================================
# (b) BAHNLINIE DURCH DEN PUNKT (1; 1)
# ============================================================

# Differentialgleichung für die Bahn: dy/dx = Vᵧ/Vₓ
def trajectory_ode(x, y):
    """Ordinäre DGL für die Trajektorie"""
    # Vermeide Division durch Null
    if abs(y) < 1e-9 or abs(2*y**3) < 1e-9:
        return 0.0
    return v_y(x, y) / v_x(x, x, y)

# Analytische Lösung: ∫y dy = -∫(x²/2) dx  →  y²/2 = -x³/6 + C
# Mit (1;1): C = 4/6 = 2/3  →  y(x) = √((4-x³)/3)

def analytic_trajectory(x):
    """Analytische Bahnkurve y(x) = √((4 - x³)/3)"""
    if x**3 > 4:
        return np.nan
    return np.sqrt((4 - x**3) / 3)

print("\n" + "=" * 60)
print("PART (b): BAHNLINIE DURCH DEN PUNKT (1; 1)")
print("=" * 60)

x_point_b = 1.0
y_point_b = 1.0

# Bestimmung der Konstanten C
C = (y_point_b**2 / 2) + (x_point_b**3 / 6)
print(f"Konstante C aus Punkt ({x_point_b}; {y_point_b}):")
print(f"C = y²/2 + x³/6 = {y_point_b}²/2 + {x_point_b}³/6 = {y_point_b**2}/2 + {x_point_b**3}/6")
print(f"  C = {y_point_b**2 / 2:.4f} + {x_point_b**3 / 6:.4f} = {C:.4f}")

print("-" * 60)
print("Bahnkurve: y(x) = √((4 - x³)/3)")

# Diskrete Punkte für die Darstellung der Bahnkurve
x_range = np.linspace(0.5, np.power(4, 1/3), 20)
y_analytic = analytic_trajectory(x_range)

print("-" * 60)
print(f"Bahnpunkte (analytisch):")
for i in range(len(x_range)):
    print(f"x={x_range[i]:.2f} → y={y_analytic[i]:.4f}")

# Visualisierung der Ergebnisse
plt.figure(figsize=(12, 5))

# Teil (a): Beschleunigungsfeld-Funktion an Punkt
plt.subplot(1, 2, 1)
plt.axhline(y=0, color='k', linestyle='--', alpha=0.3)
plt.axvline(x=0, color='k', linestyle='--', alpha=0.3)
# Beschleunigungsvektor an Punkt (2; 1)
ax_vec_x = ax_point * np.cos(np.radians(0))
ax_vec_y = ay_point * np.sin(np.radians(0))

plt.plot([x_point_a, x_point_a + ax_vec_x], 
         [y_point_a, y_point_a + ay_vec_y], 'r->', linewidth=3, label='Beschleunigung a')
plt.scatter([x_point_a], [y_point_a], c='red', s=100, zorder=5)
plt.text(x_point_a+0.3, y_point_a+0.2, f'P({x_point_a};{y_point_a})\na={ax_vec_x:.1f}i + {ay_vec_y:.1f}j', 
         fontsize=10, fontweight='bold')

plt.title('Beschleunigung im Punkt (2; 1)', fontsize=14)
plt.xlabel('x-Ebene')
plt.ylabel('y-Ebene')
plt.grid(True, alpha=0.3)
plt.legend()

# Teil (b): Bahnkurve
plt.subplot(1, 2, 2)
x_b_start, x_b_end = 0.5, np.power(4, 1/3) - 0.1
y_b_start, y_b_end = analytic_trajectory([x_b_start]), analytic_trajectory([x_b_end])
