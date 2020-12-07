import HyCarSim as hcs
import math

# fluid = hcs.Properties(viscosity = 4.4e-4 ,density = 700, compressibility = 1e-10 , heat_capacity = 1097, thermal_cond = 0.6)
# gas = hcs.Properties(viscosity = 3.2e-5, density = 0.815157, compressibility = 9e-5, heat_capacity = 3190, thermal_cond = 0.3)
# water = hcs.Properties(viscosity = 3.2e-9, density = 1040, compressibility = 9e-5, heat_capacity = 4200, thermal_cond = 0.6)

# numerical_parameters = hcs.NumericalParameters(model = 'BeggsBrill', wall_friction_factor = 0, heat_transfer_factor = 0							  
# solver = hcs.UpwindSolver(fluid, gas,water,numerical_parameters)


components = [

    hcs.PureComponentProperties(name="C1",
                                carbon_number=1, molar_mass=0.0160429, pres_critical=4.60015e6, temp_critical=190.6,
                                vol_critical=0.1e-4, acentric_factor=0.008, heat_capacity_gas=90.0,
                                heat_capacity_liq=100.0, evaporation_heat=5.11e5, viscosity_gas=1.5e-5,
                                viscosity_liq=4e-7),

    hcs.PureComponentProperties(name="C2",
                                carbon_number=2, molar_mass=0.03007, pres_critical=4871800, temp_critical=305.33,
                                vol_critical=0.00014319, acentric_factor=0.0991, heat_capacity_gas=1745.59,
                                heat_capacity_liq=2278.02, evaporation_heat=487000, viscosity_gas=9.30e-6,
                                viscosity_liq=1.67e-4),

    hcs.PureComponentProperties(name="C3",
                                carbon_number=3, molar_mass=0.044096, pres_critical=4247660, temp_critical=369.85,
                                vol_critical=2e-4, acentric_factor=0.152, heat_capacity_gas=1669.09,
                                heat_capacity_liq=2230.59, evaporation_heat=428000, viscosity_gas=8.1e-6,
                                viscosity_liq=1.98e-4),

    hcs.PureComponentProperties(name="C4",
                                carbon_number=4, molar_mass=0.05812, pres_critical=3796000, temp_critical=425.16,
                                vol_critical=2.55e-4, acentric_factor=0.1985, heat_capacity_gas=1694.60,
                                heat_capacity_liq=2278.39, evaporation_heat=386098, viscosity_gas=7.35e-6,
                                viscosity_liq=2.04e-4),

    hcs.PureComponentProperties(name="iC4",
                                carbon_number=4, molar_mass=0.05812, pres_critical=3640000, temp_critical=407.85,
                                vol_critical=0.000256, acentric_factor=0.1844, heat_capacity_gas=1638.16,
                                heat_capacity_liq=2231.59, evaporation_heat=366483, viscosity_gas=7.44e-6,
                                viscosity_liq=2.14e-4),

    hcs.PureComponentProperties(name="C5",
                                carbon_number=5, molar_mass=0.07215, pres_critical=3366500, temp_critical=469.7,
                                vol_critical=0.000310991, acentric_factor=0.2513, heat_capacity_gas=1664.17,
                                heat_capacity_liq=2317.26, evaporation_heat=357450, viscosity_gas=7.37e-6,
                                viscosity_liq=2.20e-4),

    hcs.PureComponentProperties(name="iC5",
                                carbon_number=5, molar_mass=0.07215, pres_critical=3377000, temp_critical=460.45,
                                vol_critical=0.000306, acentric_factor=0.227, heat_capacity_gas=1664.17,
                                heat_capacity_liq=2284.82, evaporation_heat=342204, viscosity_gas=7.5e-6,
                                viscosity_liq=2.14e-4),

    hcs.PureComponentProperties(name="C6",
                                carbon_number=6, molar_mass=0.08618, pres_critical=3018100, temp_critical=507.82,
                                vol_critical=0.00037, acentric_factor=0.2979, heat_capacity_gas=1692,
                                heat_capacity_liq=2293.57, evaporation_heat=334764, viscosity_gas=6.44e-6,
                                viscosity_liq=3.07e-4),

    hcs.PureComponentProperties(name="C7",
                                carbon_number=7, molar_mass=0.10021, pres_critical=2727000, temp_critical=540.13,
                                vol_critical=0.00043, acentric_factor=0.3498, heat_capacity_gas=1688,
                                heat_capacity_liq=2241.69, evaporation_heat=317034, viscosity_gas=7.16e-6,
                                viscosity_liq=4.14e-4),

    hcs.PureComponentProperties(name="C8",
                                carbon_number=8, molar_mass=0.11423, pres_critical=2497000, temp_critical=569.32,
                                vol_critical=0.000487, acentric_factor=0.396, heat_capacity_gas=1685.86,
                                heat_capacity_liq=2238.29, evaporation_heat=301234, viscosity_gas=7.55e-6,
                                viscosity_liq=5.46e-4)
]

binary_coefficients = [

    hcs.InteractionBinaryCoefficient(name1="C1", name2="C2", k=0),
    hcs.InteractionBinaryCoefficient(name1="C1", name2="C3", k=0),
    hcs.InteractionBinaryCoefficient(name1="C1", name2="C4", k=0),
    hcs.InteractionBinaryCoefficient(name1="C1", name2="iC4", k=0),
    hcs.InteractionBinaryCoefficient(name1="C1", name2="C5", k=0),
    hcs.InteractionBinaryCoefficient(name1="C1", name2="iC5", k=0),
    hcs.InteractionBinaryCoefficient(name1="C1", name2="C6", k=0),
    hcs.InteractionBinaryCoefficient(name1="C1", name2="C7", k=0),
    hcs.InteractionBinaryCoefficient(name1="C1", name2="C8", k=0),

    hcs.InteractionBinaryCoefficient(name1="C2", name2="C3", k=0),
    hcs.InteractionBinaryCoefficient(name1="C2", name2="C4", k=0),
    hcs.InteractionBinaryCoefficient(name1="C2", name2="iC4", k=0),
    hcs.InteractionBinaryCoefficient(name1="C2", name2="C5", k=0),
    hcs.InteractionBinaryCoefficient(name1="C2", name2="iC5", k=0),
    hcs.InteractionBinaryCoefficient(name1="C2", name2="C6", k=0),
    hcs.InteractionBinaryCoefficient(name1="C2", name2="C7", k=0),
    hcs.InteractionBinaryCoefficient(name1="C2", name2="C8", k=0),

    hcs.InteractionBinaryCoefficient(name1="C3", name2="C4", k=0),
    hcs.InteractionBinaryCoefficient(name1="C3", name2="iC4", k=0),
    hcs.InteractionBinaryCoefficient(name1="C3", name2="C5", k=0),
    hcs.InteractionBinaryCoefficient(name1="C3", name2="iC5", k=0),
    hcs.InteractionBinaryCoefficient(name1="C3", name2="C6", k=0),
    hcs.InteractionBinaryCoefficient(name1="C3", name2="C7", k=0),
    hcs.InteractionBinaryCoefficient(name1="C3", name2="C8", k=0),

    hcs.InteractionBinaryCoefficient(name1="C4", name2="iC4", k=0),
    hcs.InteractionBinaryCoefficient(name1="C4", name2="C5", k=0),
    hcs.InteractionBinaryCoefficient(name1="C4", name2="iC5", k=0),
    hcs.InteractionBinaryCoefficient(name1="C4", name2="C6", k=0),
    hcs.InteractionBinaryCoefficient(name1="C4", name2="C7", k=0),
    hcs.InteractionBinaryCoefficient(name1="C4", name2="C8", k=0),

    hcs.InteractionBinaryCoefficient(name1="iC4", name2="C5", k=0),
    hcs.InteractionBinaryCoefficient(name1="iC4", name2="iC5", k=0),
    hcs.InteractionBinaryCoefficient(name1="iC4", name2="C6", k=0),
    hcs.InteractionBinaryCoefficient(name1="iC4", name2="C7", k=0),
    hcs.InteractionBinaryCoefficient(name1="iC4", name2="C8", k=0),

    hcs.InteractionBinaryCoefficient(name1="C5", name2="iC5", k=0),
    hcs.InteractionBinaryCoefficient(name1="C5", name2="C6", k=0),
    hcs.InteractionBinaryCoefficient(name1="C5", name2="C7", k=0),
    hcs.InteractionBinaryCoefficient(name1="C5", name2="C8", k=0),

    hcs.InteractionBinaryCoefficient(name1="iC5", name2="C6", k=0),
    hcs.InteractionBinaryCoefficient(name1="iC5", name2="C7", k=0),
    hcs.InteractionBinaryCoefficient(name1="iC5", name2="C8", k=0),

    hcs.InteractionBinaryCoefficient(name1="C6", name2="C7", k=0),
    hcs.InteractionBinaryCoefficient(name1="C6", name2="C8", k=0),

    hcs.InteractionBinaryCoefficient(name1="C7", name2="C8", k=0)
]
water = hcs.Properties(viscosity=5.5e-4, density=1040, compressibility=4.4e-10, heat_capacity=4200, thermal_cond=0.6)
numerical_parameters = hcs.NumericalParameters(model='BeggsBrill', wall_friction_factor=1, heat_transfer_factor=1)
solver = hcs.UpwindSolver(components, water, binary_coefficients, numerical_parameters)

T_wellhead = 300  # real data
T_bottom_hole = 400  # syntetic
P_wellhead = 1e6  # real data
P_bottom_hole = 4.5e7  # syntetic
Molar_frac = [0.82532, 0.08204, 0.03846, 0.01147, 0.00961, 0.00413, 0.00439, 0.0087, 0.00931, 0.00657]

solver.traverse_simple_circuit(units=[

    hcs.PressureBoundaryCondition('bc_left', pressure=P_wellhead, temperature=T_wellhead, frac_water=0.0,
                                  frac_liquid=0.1, frac_gas=0.9, molar_fraction=Molar_frac),
    hcs.Channel(name="channel", parts=[

        hcs.ChannelPart(
            PartName="1",
            length=1000,
            ncells=1,
            roughness=2.54e-5,
            sine=math.sin(math.radians(-90)),
            diameter=0.0889,
            frac_liquid=0.1,
            frac_gas=0.9,
            frac_water=0.0,
            pressure=1.811e7,
            wall_temperature=331,
            temperature=331,
            molar_fraction=Molar_frac),

        hcs.ChannelPart(
            PartName="2",
            length=55,
            ncells=1,
            roughness=2.54e-5,
            sine=math.sin(math.radians(-83.3)),
            diameter=0.0889,
            frac_liquid=0.1,
            frac_gas=0.9,
            frac_water=0.0,
            pressure=2e7,
            wall_temperature=332,
            temperature=332,
            molar_fraction=Molar_frac),

        hcs.ChannelPart(
            PartName="3",
            length=45,
            ncells=1,
            roughness=2.54e-5,
            sine=math.sin(math.radians(-65.7)),
            diameter=0.0889,
            frac_liquid=0.1,
            frac_gas=0.9,
            frac_water=0.0,
            pressure=2.4e7,
            wall_temperature=333,
            temperature=333,
            molar_fraction=Molar_frac),

        hcs.ChannelPart(
            PartName="4",
            length=80,
            ncells=1,
            roughness=2.54e-5,
            sine=math.sin(math.radians(-69)),
            diameter=0.0889,
            frac_liquid=0.1,
            frac_gas=0.9,
            frac_water=0.0,
            pressure=2.88e7,
            wall_temperature=335,
            temperature=335,
            molar_fraction=Molar_frac),

        hcs.ChannelPart(
            PartName="5",
            length=80,
            ncells=1,
            roughness=2.54e-5,
            sine=math.sin(math.radians(-61)),
            diameter=0.0889,
            frac_liquid=0.1,
            frac_gas=0.9,
            frac_water=0.0,
            pressure=2.9e7,
            wall_temperature=336,
            temperature=336,
            molar_fraction=Molar_frac),

        hcs.ChannelPart(
            PartName="6",
            length=30,
            ncells=1,
            roughness=2.54e-5,
            sine=math.sin(math.radians(-58.3)),
            diameter=0.0889,
            frac_liquid=0.1,
            frac_gas=0.9,
            frac_water=0.0,
            pressure=2.93e7,
            wall_temperature=337,
            temperature=337,
            molar_fraction=Molar_frac),

        hcs.ChannelPart(
            PartName="7",
            length=30,
            ncells=1,
            roughness=2.54e-5,
            sine=math.sin(math.radians(-50)),
            diameter=0.0889,
            frac_liquid=0.1,
            frac_gas=0.9,
            frac_water=0.0,
            pressure=2.95e7,
            wall_temperature=338,
            temperature=338,
            molar_fraction=Molar_frac),

        hcs.ChannelPart(
            PartName="8",
            length=228,
            ncells=1,
            roughness=2.54e-5,
            sine=math.sin(math.radians(-53.1)),
            diameter=0.0889,
            frac_liquid=0.1,
            frac_gas=0.9,
            frac_water=0.0,
            pressure=2.98e7,
            wall_temperature=341,
            temperature=341,
            molar_fraction=Molar_frac),

        hcs.ChannelPart(
            PartName="9",
            length=76,
            ncells=1,
            roughness=2.54e-5,
            sine=math.sin(math.radians(-48.6)),
            diameter=0.0889,
            frac_liquid=0.1,
            frac_gas=0.9,
            frac_water=0.0,
            pressure=3e7,
            wall_temperature=342,
            temperature=342,
            molar_fraction=Molar_frac),

        hcs.ChannelPart(
            PartName="10",
            length=76,
            ncells=1,
            roughness=2.54e-5,
            sine=math.sin(math.radians(-49.6)),
            diameter=0.0889,
            frac_liquid=0.1,
            frac_gas=0.9,
            frac_water=0.0,
            pressure=3.2e7,
            wall_temperature=343,
            temperature=343,
            molar_fraction=Molar_frac),

        hcs.ChannelPart(
            PartName="11",
            length=759,
            ncells=1,
            roughness=2.54e-5,
            sine=math.sin(math.radians(-47.5)),
            diameter=0.0889,
            frac_liquid=0.1,
            frac_gas=0.9,
            frac_water=0.0,
            pressure=3.3e7,
            wall_temperature=351,
            temperature=351,
            molar_fraction=Molar_frac),

        hcs.ChannelPart(
            PartName="12",
            length=455,
            ncells=1,
            roughness=2.54e-5,
            sine=math.sin(math.radians(-47.5)),
            diameter=0.0889,
            frac_liquid=0.1,
            frac_gas=0.9,
            frac_water=0.0,
            pressure=3.4e7,
            wall_temperature=356,
            temperature=356,
            molar_fraction=Molar_frac),

        hcs.ChannelPart(
            PartName="13",
            length=456,
            ncells=1,
            roughness=2.54e-5,
            sine=math.sin(math.radians(-49.7)),
            diameter=0.0889,
            frac_liquid=0.1,
            frac_gas=0.9,
            frac_water=0.0,
            pressure=3.5e7,
            wall_temperature=362,
            temperature=362,
            molar_fraction=Molar_frac),

        hcs.ChannelPart(
            PartName="14",
            length=56,
            ncells=1,
            roughness=2.54e-5,
            sine=math.sin(math.radians(-49)),
            diameter=0.0889,
            frac_liquid=0.1,
            frac_gas=0.9,
            frac_water=0.0,
            pressure=3.6e7,
            wall_temperature=363,
            temperature=363,
            molar_fraction=Molar_frac),

        hcs.ChannelPart(
            PartName="15",
            length=279,
            ncells=1,
            roughness=2.54e-5,
            sine=math.sin(math.radians(-58)),
            diameter=0.0889,
            frac_liquid=0.1,
            frac_gas=0.9,
            frac_water=0.0,
            pressure=3.65e7,
            wall_temperature=368,
            temperature=368,
            molar_fraction=Molar_frac),

        hcs.ChannelPart(
            PartName="16",
            length=35,
            ncells=1,
            roughness=2.54e-5,
            sine=math.sin(math.radians(-60.1)),
            diameter=0.0889,
            frac_liquid=0.1,
            frac_gas=0.9,
            frac_water=0.0,
            pressure=3.7e7,
            wall_temperature=369,
            temperature=369,
            molar_fraction=Molar_frac),

        hcs.ChannelPart(
            PartName="17",
            length=35,
            ncells=1,
            roughness=2.54e-5,
            sine=math.sin(math.radians(-70.6)),
            diameter=0.0889,
            frac_liquid=0.1,
            frac_gas=0.9,
            frac_water=0.0,
            pressure=3.75e7,
            wall_temperature=370,
            temperature=370,
            molar_fraction=Molar_frac),

        hcs.ChannelPart(
            PartName="18",
            length=75,
            ncells=1,
            roughness=2.54e-5,
            sine=math.sin(math.radians(-70.6)),
            diameter=0.0889,
            frac_liquid=0.1,
            frac_gas=0.9,
            frac_water=0.0,
            pressure=3.8e7,
            wall_temperature=371,
            temperature=371,
            molar_fraction=Molar_frac),

        hcs.ChannelPart(
            PartName="19",
            length=150,
            ncells=1,
            roughness=2.54e-5,
            sine=math.sin(math.radians(-76.7)),
            diameter=0.0889,
            frac_liquid=0.1,
            frac_gas=0.9,
            frac_water=0.0,
            pressure=4e7,
            wall_temperature=374,
            temperature=374,
            molar_fraction=Molar_frac),

        hcs.ChannelPart(
            PartName="20",
            length=109,
            ncells=1,
            roughness=2.54e-5,
            sine=math.sin(math.radians(-80.6)),
            diameter=0.0889,
            frac_liquid=0.1,
            frac_gas=0.9,
            frac_water=0.0,
            pressure=4.3e7,
            wall_temperature=376,
            temperature=376,
            molar_fraction=Molar_frac),

        hcs.ChannelPart(
            PartName="21",
            length=121,
            ncells=1,
            roughness=2.54e-5,
            sine=math.sin(math.radians(-90)),
            diameter=0.0889,
            frac_liquid=0.1,
            frac_gas=0.9,
            frac_water=0.0,
            pressure=4.5e7,
            wall_temperature=378,
            temperature=378,
            molar_fraction=Molar_frac),
    ]),
    hcs.PressureBoundaryCondition('bc_rigth', pressure=P_bottom_hole, temperature=T_bottom_hole, frac_water=0.0,
                                  frac_liquid=0.1, frac_gas=0.9, molar_fraction=Molar_frac),

    # hcs.MassFlowBoundaryCondition('bc_rigth', flux=20, temperature=T_bottom_hole, frac_water=0.1, frac_liquid=0.1,
    #                               frac_gas=0.8, molar_fraction=Molar_frac)

])
# solver.compute_steady(MaxIterations=150000, dtmax=5e-2, error=1.9e-4, delta_iterations=25, path_text='output.tsv')

solver.compute_all(tmie=2500, dt=5e-3, dtmax=5e-2, delta_seconds=50, path_text='output.tsv')
