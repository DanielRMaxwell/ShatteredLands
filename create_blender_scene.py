import bpy
import math
from mathutils import Vector

# Start from an empty scene.
bpy.ops.wm.read_factory_settings(use_empty=True)
scene = bpy.context.scene
scene.render.engine = 'BLENDER_EEVEE'
scene.render.resolution_x = 640
scene.render.resolution_y = 640
scene.render.resolution_percentage = 100
scene.render.image_settings.file_format = 'PNG'
scene.render.filepath = '//glowing_orb.png'
scene.world = bpy.data.worlds.new('Midnight World')
scene.world.color = (0.008, 0.012, 0.028)

def material(name, color, metallic=0.0, roughness=0.5, emission=None):
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get('Principled BSDF')
    bsdf.inputs['Base Color'].default_value = (*color, 1)
    bsdf.inputs['Metallic'].default_value = metallic
    bsdf.inputs['Roughness'].default_value = roughness
    if emission:
        bsdf.inputs['Emission Color'].default_value = (*emission[0], 1)
        bsdf.inputs['Emission Strength'].default_value = emission[1]
    return mat

stone = material('Obsidian pedestal', (0.025, 0.035, 0.06), metallic=0.6, roughness=0.23)
glow = material('Azure energy', (0.02, 0.18, 0.6), metallic=0.15, roughness=0.2,
                emission=((0.02, 0.25, 1.0), 5.0))
gold = material('Inlaid gold', (0.42, 0.12, 0.015), metallic=0.9, roughness=0.22)

# A stepped, beveled pedestal.
for radius, height, z in [(2.55, 0.32, 0.16), (2.12, 0.30, 0.46), (1.64, 0.24, 0.73)]:
    bpy.ops.mesh.primitive_cylinder_add(vertices=96, radius=radius, depth=height, location=(0, 0, z))
    obj = bpy.context.object
    obj.data.materials.append(stone)
    bevel = obj.modifiers.new('Soft edges', 'BEVEL')
    bevel.width = 0.08
    bevel.segments = 3

# Golden ring inset above the pedestal.
bpy.ops.mesh.primitive_torus_add(major_radius=1.31, minor_radius=0.055, major_segments=96, minor_segments=16, location=(0, 0, 0.89))
bpy.context.object.data.materials.append(gold)

# Glowing sphere and a fine outer ring.
bpy.ops.mesh.primitive_uv_sphere_add(segments=96, ring_count=64, radius=0.87, location=(0, 0, 1.82))
orb = bpy.context.object
orb.name = 'Glowing Azure Orb'
orb.data.materials.append(glow)
bpy.ops.object.shade_smooth()

bpy.ops.mesh.primitive_torus_add(major_radius=1.08, minor_radius=0.028, major_segments=96, minor_segments=12, location=(0, 0, 1.82), rotation=(math.radians(68), 0, math.radians(18)))
bpy.context.object.data.materials.append(gold)

# Floor catches the light.
bpy.ops.mesh.primitive_plane_add(size=30, location=(0, 0, 0))
floor = bpy.context.object
floor.data.materials.append(material('Floor', (0.006, 0.009, 0.02), metallic=0.15, roughness=0.3))

# Lighting.
def point(name, location, color, energy, radius):
    bpy.ops.object.light_add(type='POINT', location=location)
    light = bpy.context.object
    light.name = name
    light.data.color = color
    light.data.energy = energy
    light.data.shadow_soft_size = radius

point('Blue glow', (0, 0, 2.0), (0.08, 0.35, 1.0), 650, 1.1)
point('Warm rim', (3.1, -2.5, 4.2), (1.0, 0.22, 0.04), 900, 2.0)
point('Cool fill', (-3.0, 1.5, 2.8), (0.06, 0.3, 1.0), 750, 2.0)

# Camera pointed at the orb.
bpy.ops.object.camera_add(location=(5.4, -6.6, 4.4))
camera = bpy.context.object
scene.camera = camera
target = Vector((0, 0, 1.2))
camera.rotation_euler = (target - camera.location).to_track_quat('-Z', 'Y').to_euler()
camera.data.lens = 53

scene.render.film_transparent = False
bpy.ops.wm.save_as_mainfile(filepath=bpy.path.abspath('//glowing_orb_scene.blend'))
bpy.ops.render.render(write_still=True)
