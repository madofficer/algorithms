def calculate_shock_relations(P1, v1, rho1, T1, P2, v2, rho2, T2, gamma=1.4, R=287.0):

    E1 = R * T1 / (gamma - 1)
    E2 = R * T2 / (gamma - 1)

    # 1. Сохранение импульса (P + ρv²)
    momentum1 = P1 + rho1 * v1**2
    momentum2 = P2 + rho2 * v2**2
    momentum_diff = abs(momentum1 - momentum2)

    # 2. Сохранение массы (ρvS)
    mass_flow1 = rho1 * v1 
    mass_flow2 = rho2 * v2 
    mass_flow_diff = abs(mass_flow1 - mass_flow2)

    # 3. Сохранение энергии (ρvS(v²/2 + E))
    energy_flow1 = mass_flow1 * (v1**2 / 2 + E1)
    energy_flow2 = mass_flow2 * (v2**2 / 2 + E2)
    energy_diff = abs(energy_flow1 - energy_flow2)

    # Вывод результатов

    print(f"1. impulse:")
    print(f"   Before: {momentum1:.4e}")
    print(f"   After:   {momentum2:.4e}")

    print(f"\n2. Diss:")
    print(f"   Before: {mass_flow1:.4e}")
    print(f"   After:   {mass_flow2:.4e}")

    print(f"\n3. Energy:")
    print(f"   Before: {energy_flow1:.4e}")
    print(f"   After:   {energy_flow2:.4e}")

    return {
        'momentum': {'before': momentum1, 'after': momentum2, 'diff': momentum_diff},
        'mass_flow': {'before': mass_flow1, 'after': mass_flow2, 'diff': mass_flow_diff},
        'energy_flow': {'before': energy_flow1, 'after': energy_flow2, 'diff': energy_diff}
    }

# Пример использования с вашими данными
results = calculate_shock_relations(
    P1=77039.4, v1=1038.92, rho1=2.05147, T1=302.673,
    P2=698465, v2=700.139, rho2=4.28627, T2=571.2   # T2 подобрана для примера
)