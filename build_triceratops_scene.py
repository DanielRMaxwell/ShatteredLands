import bpy
import math
from mathutils import Vector

# A stylized, fully editable one-minute loop made entirely from native Blender geometry.
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

scene = bpy.context.scene
scene.render.engine = 'BLENDER_EEVEE'
scene.render.resolution_x = 1280
scene.render.resolution_y = 720
scene.render.resolution_percentage = 50
scene.render.image_settings.file_format = 'PNG'
scene.render.ffmpeg.format = 'MPEG4'
scene.render.filepath = '//triceratops_river_loop.mp4'
scene.render.fps = 30
scene.frame_start, scene.frame_end = 1, 1800
scene.render.film_transparent = False
scene.world.color = (0.08, 0.12, 0.18)

def mat(name, color, metallic=0.0, rough=0.6):
    m = bpy.data.materials.new(name)
    m.diffuse_color = (*color, 1)
    m.use_nodes = True
    bsdf = m.node_tree.nodes.get('Principled BSDF')
    bsdf.inputs['Base Color'].default_value = (*color, 1)
    bsdf.inputs['Roughness'].default_value = rough
    bsdf.inputs['Metallic'].default_value = metallic
    return m

fern = mat('Triceratops moss green', (0.13, 0.32, 0.10), 0, .82)
cream = mat('Horn ivory', (0.82, 0.70, 0.46), 0, .52)
grass = mat('Meadow grass', (0.10, 0.34, 0.07), 0, 1)
soil = mat('Riverbank soil', (0.19, 0.08, 0.025), 0, 1)
water = mat('River water', (0.02, 0.20, 0.32), .15, .23)
stone = mat('Rock', (0.20, 0.18, 0.13), 0, .9)

def uv(name, loc, scale, material, parent=None):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=24, ring_count=12, location=loc)
    o = bpy.context.object; o.name=name; o.scale=scale; bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    o.data.materials.append(material)
    if parent: o.parent=parent
    bpy.ops.object.shade_smooth()
    return o

def cone(name, loc, radius1, depth, material, rotation=(0,0,0), parent=None):
    bpy.ops.mesh.primitive_cone_add(vertices=20, radius1=radius1, radius2=0.02, depth=depth, location=loc, rotation=rotation)
    o=bpy.context.object; o.name=name; o.data.materials.append(material)
    if parent: o.parent=parent
    return o

def cube(name, loc, scale, material):
    bpy.ops.mesh.primitive_cube_add(location=loc)
    o=bpy.context.object; o.name=name; o.scale=scale; bpy.ops.object.transform_apply(location=False, rotation=False, scale=True); o.data.materials.append(material); return o

# Meadow disk and a broad, curved-looking river built from a blue plane over banks.
bpy.ops.mesh.primitive_plane_add(size=120, location=(0,0,0))
field=bpy.context.object; field.name='Endless meadow'; field.data.materials.append(grass)

# river cuts diagonally through meadow
river = cube('River', (0,-10,0.05), (28,4.2,.06), water)
river.rotation_euler[2]=math.radians(-12)
bank_a=cube('Riverbank A', (0,-5.5,0.04), (28,.75,.08), soil); bank_a.rotation_euler[2]=math.radians(-12)
bank_b=cube('Riverbank B', (0,-14.5,0.04), (28,.75,.08), soil); bank_b.rotation_euler[2]=math.radians(-12)

# scatter low rocks and grass tufts (fixed scene detail)
for i in range(45):
    a=i*2.399; r=9+(i%7)*2.7
    x,y=r*math.cos(a), r*math.sin(a)
    if -16 < y < -4: continue
    rock=uv('Meadow stone', (x,y,.22), (.24+(i%3)*.12,.2,.18), stone)
    rock.rotation_euler=(0.3,0.2,a)
for i in range(130):
    a=i*1.731; r=4+(i%17)*1.45
    x,y=r*math.cos(a), r*math.sin(a)
    if -16<y<-4: continue
    bpy.ops.mesh.primitive_cone_add(vertices=5, radius1=.10, radius2=.015, depth=.45+(i%4)*.10, location=(x,y,.25))
    tuft=bpy.context.object; tuft.name='Grass tuft'; tuft.data.materials.append(grass); tuft.rotation_euler[2]=a

# Triceratops collection/parent.
bpy.ops.object.empty_add(type='PLAIN_AXES', location=(0,10,1.2))
dino=bpy.context.object; dino.name='TRICERATOPS_RIG_LOOP'
body=uv('Triceratops body', (0,0,0), (2.9,1.25,1.15), fern, dino)
neck=uv('Triceratops neck', (2.25,0,.35), (1.1,.92,.9), fern, dino)
head=uv('Triceratops head', (3.2,0,.45), (1.15,.82,.75), fern, dino)
frill=uv('Triceratops frill', (2.45,0,1.2), (1.1,1.02,.55), fern, dino)
tail=uv('Triceratops tail', (-3.25,0,.12), (2.3,.42,.38), fern, dino); tail.rotation_euler[1]=math.radians(-8)
# beak + horns: points forward in local +X
cone('Nasal horn', (4.0,0,.70), .22, 1.1, cream, (0,math.radians(90),0), dino)
cone('Brow horn L', (3.65,.58,1.20), .18, 1.35, cream, (0,math.radians(55),math.radians(-6)), dino)
cone('Brow horn R', (3.65,-.58,1.20), .18, 1.35, cream, (0,math.radians(55),math.radians(6)), dino)
for side in (-1,1):
    for j in range(4): cone('Frill spike', (2.1,side*(.68+.11*j),1.25+.16*j), .10, .45, cream, (0,math.radians(75),0), dino)

# Individual animated legs; simple joints designed to read clearly in a mid-distance camera.
legs=[]
for x, y, phase in [(1.55,.78,0), (1.55,-.78,15), (-1.65,.78,15), (-1.65,-.78,0)]:
    upper=uv('Walking leg', (x,y,-.72), (.38,.34,.95), fern, dino)
    foot=uv('Clawed foot', (x+.1,y,-1.52), (.62,.42,.26), fern, dino)
    legs.append((upper,foot,phase))

# Animate the one-minute cyclic walk. Frame 1801 repeats frame 1 to make interpolation loop-ready.
for f in range(1,1802,15):
    cyc=(f-1)/30.0 # two steps/sec
    for upper,foot,ph in legs:
        swing=math.radians(25)*math.sin(math.tau*(cyc+ph/30.0))
        lift=max(0, math.sin(math.tau*(cyc+ph/30.0))) * .20
        upper.rotation_euler[1]=swing; upper.keyframe_insert('rotation_euler', frame=f)
        foot.location.z=-1.52+lift; foot.rotation_euler[1]=-swing*.45; foot.keyframe_insert('location',frame=f); foot.keyframe_insert('rotation_euler',frame=f)
    dino.location.z=1.2 + .10*math.sin(math.tau*cyc); dino.keyframe_insert('location', frame=f)
    body.rotation_euler[1]=math.radians(2.4)*math.sin(math.tau*cyc); body.keyframe_insert('rotation_euler',frame=f)
    head.rotation_euler[2]=math.radians(2)*math.sin(math.tau*cyc); head.keyframe_insert('rotation_euler',frame=f)

# Long arc across the field, approaching the river at the front of each visible pass, with exact loop closure.
for f in range(1,1802,30):
    t=(f-1)/1800.0
    ang=math.radians(104 - 360*t)
    rad=15.5
    dino.location.x=rad*math.cos(ang)
    dino.location.y=-1.3+rad*math.sin(ang)
    dino.rotation_euler[2]=ang-math.pi/2
    dino.keyframe_insert('location',frame=f); dino.keyframe_insert('rotation_euler',frame=f)

# Camera follows with a stable composition, itself looped.
bpy.ops.object.empty_add(type='PLAIN_AXES', location=(0,0,0)); target=bpy.context.object; target.name='Camera target'
bpy.ops.object.camera_add(); cam=bpy.context.object; cam.name='Loop camera'; scene.camera=cam; cam.data.lens=50
for f in range(1,1802,30):
    t=(f-1)/1800.0; ang=math.radians(104-360*t); rad=15.5
    p=Vector((rad*math.cos(ang),-1.3+rad*math.sin(ang),1.2))
    forward=Vector((math.cos(ang-math.pi/2),math.sin(ang-math.pi/2),0))
    cam.location=p-forward*12+Vector((0,0,5.5))
    target.location=p+forward*2+Vector((0,0,.2))
    cam.keyframe_insert('location',frame=f); target.keyframe_insert('location',frame=f)
constraint=cam.constraints.new(type='TRACK_TO'); constraint.target=target; constraint.track_axis='TRACK_NEGATIVE_Z'; constraint.up_axis='UP_Y'

# Sun and soft world lighting.
bpy.ops.object.light_add(type='SUN', location=(0,0,20)); sun=bpy.context.object; sun.name='Late afternoon sun'; sun.data.energy=3.0; sun.rotation_euler=(math.radians(30),math.radians(-20),math.radians(25))
bpy.ops.object.light_add(type='AREA', location=(0,-4,12)); fill=bpy.context.object; fill.data.energy=850; fill.data.shape='DISK'; fill.data.size=12

scene.frame_set(420)
bpy.ops.wm.save_as_mainfile(filepath='D:/Repository folders/ShatteredLands/Triceratops_River_Loop.blend')
scene.render.image_settings.file_format='PNG'
scene.render.filepath='D:/Repository folders/ShatteredLands/triceratops_preview.png'
bpy.ops.render.render(write_still=True)
