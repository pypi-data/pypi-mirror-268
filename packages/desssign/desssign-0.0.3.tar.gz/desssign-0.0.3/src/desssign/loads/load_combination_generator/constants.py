from desssign.loads.enums import LoadBehavior
from desssign.loads.enums import LoadType
from desssign.loads.enums import VariableCategory

PSI_FACTORS = {
    VariableCategory.A: {
        "psi_0": 0.7,
        "psi_1": 0.5,
        "psi_2": 0.3,
    },
    VariableCategory.B: {
        "psi_0": 0.7,
        "psi_1": 0.5,
        "psi_2": 0.3,
    },
    VariableCategory.C: {
        "psi_0": 0.7,
        "psi_1": 0.7,
        "psi_2": 0.6,
    },
    VariableCategory.D: {
        "psi_0": 0.7,
        "psi_1": 0.7,
        "psi_2": 0.6,
    },
    VariableCategory.E: {
        "psi_0": 1.0,
        "psi_1": 0.9,
        "psi_2": 0.8,
    },
    VariableCategory.F: {
        "psi_0": 0.7,
        "psi_1": 0.7,
        "psi_2": 0.6,
    },
    VariableCategory.G: {
        "psi_0": 0.7,
        "psi_1": 0.5,
        "psi_2": 0.3,
    },
    VariableCategory.H: {
        "psi_0": 0.0,
        "psi_1": 0.0,
        "psi_2": 0.0,
    },
    VariableCategory.SNOW_ABOVE_1000_M: {
        "psi_0": 0.7,
        "psi_1": 0.5,
        "psi_2": 0.2,
    },
    VariableCategory.SNOW_BELLOW_1000_M: {
        "psi_0": 0.5,
        "psi_1": 0.2,
        "psi_2": 0.0,
    },
    VariableCategory.WIND: {
        "psi_0": 0.6,
        "psi_1": 0.2,
        "psi_2": 0.0,
    },
    VariableCategory.TEMPERATURE: {
        "psi_0": 0.6,
        "psi_1": 0.5,
        "psi_2": 0.0,
    },
}


GAMMA_VALUES = {
    "Set B": {
        LoadType.PERMANENT: {
            LoadBehavior.FAVOURABLE: 1.0,
            LoadBehavior.UNFAVOURABLE: 1.35,
        },
        LoadType.VARIABLE: {
            LoadBehavior.FAVOURABLE: 0.0,
            LoadBehavior.UNFAVOURABLE: 1.5,
        },
    },
    "Set C": {
        LoadType.PERMANENT: {
            LoadBehavior.FAVOURABLE: 1.0,
            LoadBehavior.UNFAVOURABLE: 1.0,
        },
        LoadType.VARIABLE: {
            LoadBehavior.FAVOURABLE: 0.0,
            LoadBehavior.UNFAVOURABLE: 1.3,
        },
    },
}

XI = 0.85
