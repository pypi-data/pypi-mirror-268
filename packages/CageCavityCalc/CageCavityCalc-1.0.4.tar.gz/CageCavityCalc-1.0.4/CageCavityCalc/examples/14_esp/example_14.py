from CageCavityCalc.CageCavityCalc import cavity

cav = cavity()
#cav.read_file("ncage.xyz")
#cav.read_file("vic_host.xyz")
#cav.read_file("gal2_cage.pdb")
cav.read_file("pd2_cage.pdb")
cav.grid_spacing = 0.5

cav.calculate_volume()
cav.calculate_esp(metal_name="Pd", metal_charge=2)
#cav.calculate_esp(metal_name="Ga", metal_charge=3)
#cav.calculate_esp()
cav.print_to_pymol("pd2_cage.pml", "esp")

