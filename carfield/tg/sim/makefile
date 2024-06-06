# Makefile for Carfield simulation

CAR_VSIM_SIM_BUILD = car-vsim-sim-build
CAR_VSIM_SIM_RUN = car-vsim-sim-run

all: $(CAR_VSIM_SIM_BUILD)

$(CAR_VSIM_SIM_BUILD):
    make car-vsim-sim-build

$(CAR_VSIM_SIM_RUN):
    make car-vsim-sim-run CHS_BINARY=./sw/tests/bare-metal/hostd/helloworld.car.l2.elf

help:
    @echo "Make targets:"
    @echo "  all: Build and run Carfield simulation"
    @echo "  car-vsim-sim-build: Build Carfield simulation"
    @echo "  car-vsim-sim-run: Run Carfield simulation"
