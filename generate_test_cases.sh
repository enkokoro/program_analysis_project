# Make directories

# pynguin
pynguin --project-path triangle --output-path triangle/tests/pynguin --module-name triangle 

# deal -> write deal file

# tstl
tstl tests/tstl/triangle.tstl
tstl_rt --timeout 30 

# crosshair

# klara
klara triangle_types.py

# auger -> write auger file