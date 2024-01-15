import bpy

# create objects
## white sphere
bpy.ops.mesh.primitive_uv_sphere_add(radius=1, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
## white planes
bpy.ops.mesh.primitive_plane_add(size=4, enter_editmode=False, align='WORLD', location=(0, 0, 3), rotation=(0, 0, 0), scale=(1, 1, 1))
bpy.ops.mesh.primitive_plane_add(size=4, enter_editmode=False, align='WORLD', location=(0, 0, -1), rotation=(0, 0, 0), scale=(1, 1, 1))
bpy.ops.mesh.primitive_plane_add(size=4, enter_editmode=False, align='WORLD', location=(0, 2, 1), rotation=(1.5708, 0, 0), scale=(1, 1, 1))
## red plane
bpy.ops.mesh.primitive_plane_add(size=4, enter_editmode=False, align='WORLD', location=(2, 0, 1), rotation=(0, 1.5708, 0), scale=(1, 1, 1))
## green plane
bpy.ops.mesh.primitive_plane_add(size=4, enter_editmode=False, align='WORLD', location=(-2, 0, 1), rotation=(0, 1.5708, 0), scale=(1, 1, 1))
## light plane
bpy.ops.mesh.primitive_plane_add(size=1, enter_editmode=False, align='WORLD', location=(0, 0, 3), rotation=(0, 0, 0), scale=(1, 1, 1))

# creating and assigning materials
## white
white_material = bpy.data.materials.new(name = "white")
ws = bpy.data.objects['Sphere']
ws.data.materials.append(white_material)
wp1 = bpy.data.objects['Plane']
wp1.data.materials.append(white_material)
wp2 = bpy.data.objects['Plane.001']
wp2.data.materials.append(white_material)
wp3 = bpy.data.objects['Plane.002']
wp3.data.materials.append(white_material)

white_material.use_nodes = True
wp_nodes = white_material.node_tree.nodes
wp_nodes["Principled BSDF"].inputs[0].default_value = (1, 1, 1, 1)

## red
red_material = bpy.data.materials.new(name = "red")
rp1 = bpy.data.objects['Plane.004']
rp1.data.materials.append(red_material)

red_material.use_nodes = True
rp_nodes = red_material.node_tree.nodes
rp_nodes["Principled BSDF"].inputs[0].default_value = (1, 0, 0, 1)

## green
green_material = bpy.data.materials.new(name = "green")
gp1 = bpy.data.objects['Plane.003']
gp1.data.materials.append(green_material)

green_material.use_nodes = True
gp_nodes = green_material.node_tree.nodes
gp_nodes["Principled BSDF"].inputs[0].default_value = (0, 1, 0, 1)

## light
light_source_material = bpy.data.materials.new(name = "light")
ls1 = bpy.data.objects['Plane.005']
ls1.data.materials.append(light_source_material)

light_source_material.use_nodes = True
ls_nodes = light_source_material.node_tree.nodes

ls_material_output = ls_nodes.get("Material Output")
node_emission = ls_nodes.new(type='ShaderNodeEmission')

node_emission.inputs[0].default_value = (1.0, 1.0, 1.0, 1)
node_emission.inputs[1].default_value = 20.0 #strength

ls_links = light_source_material.node_tree.links
ls_new_link = ls_links.new(node_emission.outputs[0], ls_material_output.inputs[0])