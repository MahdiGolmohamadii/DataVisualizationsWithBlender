import csv
import bpy

filepath = 'C:/Users/mahdi/Desktop/data.csv'


#setting variables
bar_spacing = 1.5
bar_width = 1

x_axis_height = 0.2
y_axis_width = 0.2

x_axis_height_padding = 1
y_axis_height_padding = 1

bar_to_X_padding = 0.5



with open(filepath) as f:
    readout = list(csv.reader(f))
    #print(readout)





maxim = float(readout[0][1])
#print(maxim)
for a in readout:
    placement = readout.index(a)
    bpy.ops.mesh.primitive_plane_add(size=1)
    new_bar = bpy.context.object
    
    for vert in new_bar.data.vertices:
        vert.co[1] += 0.5
        vert.co[0] += placement * bar_spacing + 1 + y_axis_width
    
    new_bar.scale = (bar_width, float(a[1]), 1)
    new_bar.location.y += bar_to_X_padding
    if float(a[1]) > maxim : maxim = float(a[1])
    
    
    #add the text
    bpy.ops.object.text_add()
    bpy.context.object.data.align_x = 'RIGHT'
    bpy.context.object.data.align_y = 'CENTER'
    bpy.ops.transform.rotate(value=-1.5708)
    bpy.ops.transform.translate(value=(placement * bar_spacing + 0.5, -0.5, 0))
    bpy.context.object.data.body = a[0]
    
    
#Add bars

#X Axis
bpy.ops.mesh.primitive_plane_add(size=1)
bar = bpy.context.object
for vert in bar.data.vertices:
    vert.co[1] += 0.5
    vert.co[0] += 0.5
    
bar.scale = (((bar_width + (bar_spacing/2)) * (len(readout) - 1)) + x_axis_height_padding, x_axis_height, 1)


#Y Axis
bpy.ops.mesh.primitive_plane_add(size=1)
bar = bpy.context.object
for vert in bar.data.vertices:
    vert.co[1] += 0.5
    vert.co[0] += 0.5

bar.scale = (y_axis_width, maxim + y_axis_height_padding, 1)

