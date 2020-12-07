import HyCarSim as hcs
import math

fluid = hcs.Properties(viscosity=2e-3, density=760, compressibility=2.2e-9, heat_capacity=2000, thermal_cond=0.14)
gas = hcs.Properties(viscosity=1e-5, density=0.815, compressibility=1e-5, heat_capacity=2200, thermal_cond=0.03)
water = hcs.Properties(viscosity=5.5e-4, density=1040, compressibility=4.4e-10, heat_capacity=4200, thermal_cond=0.6)

numerical_parameters = hcs.NumericalParameters(model='BeggsBrill', wall_friction_factor=1, heat_transfer_factor=1)
solver = hcs.UpwindSolver(fluid, gas, water, numerical_parameters)

# T_joint=323.01
# P_joint=1.0251e7
FRAC_W = 0.0
FRAC_G = 1.0
FRAC_L = 0.0

P_wellhead = 74.85e5
T_wellhead = 288.7
P_bottom = 2.758e7
T_bottom = 394
roughness = 2.54e-5
ncells = 2

solver.traverse_simple_circuit(units=[

    hcs.PressureBoundaryCondition(
        "bc_left",
        pressure=P_wellhead,
        temperature=T_wellhead,
        frac_water=FRAC_W,
        frac_liquid=FRAC_L,
        frac_gas=FRAC_G,
        molar_fraction=[]
    ),
    hcs.Channel(
        name="channel",
        parts=[

            hcs.ChannelPart(
                PartName="Part_1",
                length=49,
                sine=math.sin(math.radians(-(90 - 0))),
                diameter=0.088,
                pressure=8.0e6,
                temperature=296.0,
                wall_temperature=296.0,
                ncells=2,
                roughness=roughness,
                frac_liquid=FRAC_L,
                frac_gas=FRAC_G,
                frac_water=FRAC_W,
                molar_fraction=[]
            ),

            hcs.ChannelPart(
                PartName="Part_2",
                length=1171,
                sine=math.sin(math.radians(-(90 - 0))),
                diameter=0.088,
                pressure=10.0e6,
                temperature=323,
                wall_temperature=323,
                ncells=2,
                roughness=roughness,
                frac_liquid=FRAC_L,
                frac_gas=FRAC_G,
                frac_water=FRAC_W,
                molar_fraction=[]
            ),

            hcs.ChannelPart(
                PartName="Part_3",
                length=2133,
                sine=math.sin(math.radians(-(90 - 51.32))),
                diameter=0.088,
                pressure=15.0e6,
                temperature=371,
                wall_temperature=371,
                ncells=2,
                roughness=roughness,
                frac_liquid=FRAC_L,
                frac_gas=FRAC_G,
                frac_water=FRAC_W,
                molar_fraction=[]
            ),

            hcs.ChannelPart(
                PartName="Part_4",
                length=306,
                sine=math.sin(math.radians(-(90 - 51.32))),
                diameter=0.147,
                pressure=22.0e6,
                temperature=317,
                wall_temperature=390,
                ncells=2,
                roughness=roughness,
                frac_liquid=FRAC_L,
                frac_gas=FRAC_G,
                frac_water=FRAC_W,
                molar_fraction=[]
            ),

        ]),

    hcs.PressureBoundaryCondition(
        "bc_right",
        pressure=P_bottom,
        temperature=T_bottom,
        frac_water=FRAC_W,
        frac_liquid=FRAC_L,
        frac_gas=FRAC_G,
        molar_fraction=[]
    )

])

solver.compute_all(time=2000, dt=5e-3, dtmax=1e-2, delta_seconds=50, path_text='output.tsv')
